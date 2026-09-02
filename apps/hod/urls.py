
from django.urls import path

from .views import (
    hod_dashboard,
    hod_teachers,
    hod_students,
    hod_courses,
    hod_course_offerings,
    hod_create_course_offering,
)


urlpatterns = [
    path(
        "dashboard/",
        hod_dashboard,
        name="hod_dashboard",
    ),

    path(
        "teachers/",
        hod_teachers,
        name="hod_teachers",
    ),

    path(
        "students/",
        hod_students,
        name="hod_students",
    ),

    path(
        "courses/",
        hod_courses,
        name="hod_courses",
    ),

    path(
        "course-offerings/",
        hod_course_offerings,
        name="hod_course_offerings",
    ),

    path(
        "course-offerings/create/",
        hod_create_course_offering,
        name="hod_create_course_offering",
    ),
]

