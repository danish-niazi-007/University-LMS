from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from apps.accounts.decorators import role_required
from apps.courses.models import CourseOffering
from apps.attendance.models import Attendance


@login_required
@role_required("teacher")
def teacher_attendance(request, offering_id):

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

    selected_date = (
        request.POST.get("date")
        or request.GET.get("date")
        or timezone.localdate().isoformat()
    )

    for enrollment in enrollments:

        record = Attendance.objects.filter(
            enrollment=enrollment,
            date=selected_date,
        ).first()

        enrollment.is_present = record.present if record else True

    if request.method == "POST":

        for enrollment in enrollments:

            present = request.POST.get(
                f"present_{enrollment.id}"
            ) == "on"

            Attendance.objects.update_or_create(
                enrollment=enrollment,
                date=selected_date,
                defaults={
                    "present": present,
                },
            )

        return redirect(
            "teacher_attendance",
            offering_id=offering.id,
        )

    return render(
        request,
        "teacher/attendance.html",
        {
            "offering": offering,
            "enrollments": enrollments,
            "selected_date": selected_date,
        },
    )


@login_required
@role_required("student")
def student_attendance(request, enrollment_id):

    enrollment = get_object_or_404(
        request.user.student_profile.enrollments.select_related(
            "course_offering__course",
        ),
        id=enrollment_id,
    )

    records = enrollment.attendance_records.all()

    total_classes = records.count()

    present_classes = records.filter(
        present=True
    ).count()

    absent_classes = records.filter(
        present=False
    ).count()

    if total_classes > 0:
        attendance_percentage = (
            present_classes / total_classes
        ) * 100
    else:
        attendance_percentage = 0

    return render(
        request,
        "student/attendance.html",
        {
            "enrollment": enrollment,
            "records": records,
            "total_classes": total_classes,
            "present_classes": present_classes,
            "absent_classes": absent_classes,
            "attendance_percentage": round(
                attendance_percentage,
                2,
            ),
        },
    )