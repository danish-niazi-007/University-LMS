from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Enrollment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Enrollment
from apps.lms_assignments.models import Assignment, Submission


@login_required
def student_courses(request):
    enrollments = (
        request.user.student_profile.enrollments
        .select_related(
            "course_offering__course",
            "course_offering__teacher__user",
        )
        .order_by(
            "course_offering__course__semester",
            "course_offering__course__code",
        )
    )

    return render(
        request,
        "student/courses.html",
        {
            "enrollments": enrollments,
        },
    )
@login_required
def student_course_detail(request, enrollment_id):

    enrollment = get_object_or_404(
        request.user.student_profile.enrollments.select_related(
            "course_offering__course",
            "course_offering__teacher__user",
        ),
        id=enrollment_id,
    )

    course_offering = enrollment.course_offering

    assignments = course_offering.assignments.all()

    for assignment in assignments:
        assignment.my_submission = Submission.objects.filter(
            assignment=assignment,
            enrollment=enrollment,
        ).first()

    return render(
        request,
        "student/course_detail.html",
        {
            "enrollment": enrollment,
            "course_offering": course_offering,
            "assignments": assignments,
        },
    )