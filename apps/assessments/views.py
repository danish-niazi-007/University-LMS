from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.courses.models import CourseOffering
from apps.assessments.models import Marks
from apps.accounts.decorators import role_required
@login_required
@role_required("teacher")
def teacher_marks(request, offering_id):

    offering = get_object_or_404(
        CourseOffering,
        id=offering_id,
        teacher=request.user.teacher_profile,
    )

    enrollments = (
        offering.enrollments
        .select_related("student__user")
        .order_by("student__registration_no")
    )

    if request.method == "POST":

        for enrollment in enrollments:

            sessional = request.POST.get(
                f"sessional_{enrollment.id}",
                0,
            )

            midterm = request.POST.get(
                f"midterm_{enrollment.id}",
                0,
            )

            final = request.POST.get(
                f"final_{enrollment.id}",
                0,
            )

            Marks.objects.update_or_create(
                enrollment=enrollment,
                defaults={
                    "sessional": sessional or 0,
                    "midterm": midterm or 0,
                    "final": final or 0,
                },
            )

        return redirect(
            "teacher_marks",
            offering_id=offering.id,
        )

    for enrollment in enrollments:

        enrollment.saved_marks = Marks.objects.filter(
            enrollment=enrollment
        ).first()

    return render(
        request,
        "teacher/marks.html",
        {
            "offering": offering,
            "enrollments": enrollments,
        },
    )
@login_required
@role_required("student")
def student_marks(request, enrollment_id):

    enrollment = get_object_or_404(
        request.user.student_profile.enrollments.select_related(
            "course_offering__course",
        ),
        id=enrollment_id,
    )

    marks = Marks.objects.filter(
        enrollment=enrollment
    ).first()

    return render(
        request,
        "student/marks.html",
        {
            "enrollment": enrollment,
            "marks": marks,
        },
    )