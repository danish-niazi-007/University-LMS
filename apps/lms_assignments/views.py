from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .models import Assignment, Submission

from apps.courses.models import CourseOffering
from apps.enrollments.models import Enrollment
from apps.accounts.decorators import role_required
@login_required
@role_required("teacher")
def teacher_assignments(request, offering_id):

    offering = get_object_or_404(
        CourseOffering.objects.select_related(
            "course",
            "course__department",
            "teacher__user",
        ),
        id=offering_id,
        teacher=request.user.teacher_profile,
    )

    assignments = offering.assignments.all()

    return render(
        request,
        "teacher/assignments.html",
        {
            "offering": offering,
            "assignments": assignments,
        },
    )


@login_required
@role_required("teacher")
def create_assignment(request, offering_id):

    offering = get_object_or_404(
        CourseOffering.objects.select_related(
            "course",
            "teacher__user",
        ),
        id=offering_id,
        teacher=request.user.teacher_profile,
    )

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        assignment_file = request.FILES.get("assignment_file")

        Assignment.objects.create(
            course_offering=offering,
            title=title,
            description=description,
            due_date=due_date,
            assignment_file=assignment_file,
        )

        return redirect(
            "teacher_assignments",
            offering_id=offering.id,
        )

    return render(
        request,
        "teacher/create_assignment.html",
        {
            "offering": offering,
        },
    )


@login_required
@role_required("teacher")
def assignment_submissions(request, offering_id, assignment_id):

    offering = get_object_or_404(
        CourseOffering,
        id=offering_id,
        teacher=request.user.teacher_profile,
    )

    assignment = get_object_or_404(
        Assignment,
        id=assignment_id,
        course_offering=offering,
    )

    submissions = (
        Submission.objects
        .filter(assignment=assignment)
        .select_related(
            "enrollment__student__user",
        )
        .order_by("-submitted_at")
    )

    return render(
        request,
        "teacher/submissions.html",
        {
            "offering": offering,
            "assignment": assignment,
            "submissions": submissions,
        },
    )


@login_required
@role_required("student")
def submit_assignment(request, enrollment_id, assignment_id):

    enrollment = get_object_or_404(
        Enrollment.objects.select_related(
            "course_offering",
        ),
        id=enrollment_id,
        student=request.user.student_profile,
    )

    assignment = get_object_or_404(
        Assignment.objects.select_related(
            "course_offering",
        ),
        id=assignment_id,
    )

    if assignment.course_offering_id != enrollment.course_offering_id:
        return HttpResponseForbidden(
            "You are not enrolled in this course."
        )

    if request.method == "POST":

        submission_file = request.FILES.get("submission_file")

        if not submission_file:
            return render(
                request,
                "student/submit_assignment.html",
                {
                    "assignment": assignment,
                    "enrollment": enrollment,
                    "error": "Please select a file.",
                },
            )

        Submission.objects.update_or_create(
            assignment=assignment,
            enrollment=enrollment,
            defaults={
                "submission_file": submission_file,
            },
        )

        return redirect(
            "student_course_detail",
            enrollment_id=enrollment.id,
        )

    return render(
        request,
        "student/submit_assignment.html",
        {
            "assignment": assignment,
            "enrollment": enrollment,
        },
    )


@login_required
def download_submission(request, submission_id):

    submission = (
        Submission.objects
        .select_related(
            "assignment__course_offering__teacher__user",
            "enrollment__student__user",
        )
        .filter(id=submission_id)
        .first()
    )

    if not submission:
        raise Http404("Submission not found.")

    if not submission.submission_file:
        raise Http404("No file attached to this submission.")

    return FileResponse(
        submission.submission_file.open("rb"),
        as_attachment=True,
        filename=submission.submission_file.name.split("/")[-1],
    )