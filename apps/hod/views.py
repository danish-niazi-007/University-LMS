from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.accounts.decorators import role_required
from apps.accounts.models import StudentProfile, TeacherProfile
from apps.courses.models import Course, CourseOffering


@login_required
@role_required("hod")
def hod_dashboard(request):

    hod = request.user.hod_profile

    students_count = StudentProfile.objects.filter(
        department=hod.department
    ).count()

    teachers_count = TeacherProfile.objects.filter(
        department=hod.department
    ).count()

    return render(
        request,
        "hod/dashboard.html",
        {
            "hod": hod,
            "students_count": students_count,
            "teachers_count": teachers_count,
        },
    )
@login_required
@role_required("hod")
def hod_courses(request):

    hod = request.user.hod_profile

    courses = (
        Course.objects
        .filter(
            department=hod.department
        )
        .select_related(
            "department"
        )
        .order_by(
            "semester",
            "code",
        )
    )

    return render(
        request,
        "hod/courses.html",
        {
            "hod": hod,
            "courses": courses,
        },
    )


@login_required
@role_required("hod")
def hod_teachers(request):

    hod = request.user.hod_profile

    teachers = (
        TeacherProfile.objects
        .filter(department=hod.department)
        .select_related(
            "user",
            "department",
        )
        .order_by(
            "user__first_name",
            "user__last_name",
        )
    )

    return render(
        request,
        "hod/teachers.html",
        {
            "hod": hod,
            "teachers": teachers,
        },
    )


@login_required
@role_required("hod")
def hod_students(request):

    hod = request.user.hod_profile

    students = (
        StudentProfile.objects
        .filter(department=hod.department)
        .select_related(
            "user",
            "department",
        )
        .order_by("registration_no")
    )

    return render(
        request,
        "hod/students.html",
        {
            "hod": hod,
            "students": students,
        },
    )


@login_required
@role_required("hod")
def hod_course_offerings(request):

    hod = request.user.hod_profile

    offerings = (
        CourseOffering.objects
        .filter(course__department=hod.department)
        .select_related(
            "course",
            "teacher__user",
            "teacher__department",
        )
        .order_by(
            "course__semester",
            "course__code",
            "academic_year",
        )
    )

    return render(
        request,
        "hod/course_offerings.html",
        {
            "hod": hod,
            "offerings": offerings,
        },
    )


@login_required
@role_required("hod")
def hod_create_course_offering(request):

    hod = request.user.hod_profile

    courses = (
        Course.objects
        .filter(department=hod.department)
        .order_by(
            "semester",
            "code",
        )
    )

    teachers = (
        TeacherProfile.objects
        .filter(department=hod.department)
        .select_related("user")
        .order_by("employee_id")
    )

    if request.method == "POST":

        course_id = request.POST.get("course")
        teacher_id = request.POST.get("teacher")
        academic_year = request.POST.get("academic_year")

        course = get_object_or_404(
            Course,
            id=course_id,
            department=hod.department,
        )

        teacher = get_object_or_404(
            TeacherProfile,
            id=teacher_id,
            department=hod.department,
        )

        if not academic_year:

            return render(
                request,
                "hod/create_course_offering.html",
                {
                    "hod": hod,
                    "courses": courses,
                    "teachers": teachers,
                    "error": "Academic year is required.",
                },
            )

        CourseOffering.objects.get_or_create(
            course=course,
            teacher=teacher,
            academic_year=academic_year,
        )

        return redirect(
            "hod_course_offerings"
        )

    return render(
        request,
        "hod/create_course_offering.html",
        {
            "hod": hod,
            "courses": courses,
            "teachers": teachers,
        },
    )

