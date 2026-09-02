from django.urls import path

from .views import student_courses
from .views import student_courses, student_course_detail


urlpatterns = [
    path(
        "student/courses/",
        student_courses,
        name="student_courses",
    ),
    path(
    "student/courses/<int:enrollment_id>/",
    student_course_detail,
    name="student_course_detail",
),
]