from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from apps.accounts.decorators import role_required
from .models import CourseOffering


@login_required
@role_required("teacher")
def teacher_classes(request):

    teacher = request.user.teacher_profile

    offerings = (
        CourseOffering.objects
        .filter(teacher=teacher)
        .select_related(
            "course",
            "course__department",
        )
        .order_by(
            "course__semester",
            "course__code",
        )
    )

    return render(
        request,
        "teacher/classes.html",
        {
            "offerings": offerings,
        },
    )


@login_required
@role_required("teacher")
def teacher_class_detail(request, offering_id):

    offering = get_object_or_404(
        CourseOffering.objects.select_related(
            "course",
            "course__department",
            "teacher__user",
        ),
        id=offering_id,
        teacher=request.user.teacher_profile,
    )

    return render(
        request,
        "teacher/class_detail.html",
        {
            "offering": offering,
        },
    )


@login_required
@role_required("teacher")
def teacher_class_students(request, offering_id):

    offering = get_object_or_404(
        CourseOffering.objects.select_related(
            "course",
            "course__department",
            "teacher__user",
        ),
        id=offering_id,
        teacher=request.user.teacher_profile,
    )

    students = (
        offering.enrollments
        .select_related(
            "student__user",
            "student__department",
        )
        .order_by(
            "student__registration_no",
        )
    )

    return render(
        request,
        "teacher/students.html",
        {
            "offering": offering,
            "students": students,
        },
    )