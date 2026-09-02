from django.urls import path

from .views import (
    teacher_attendance,
    student_attendance,
)

urlpatterns = [

    path(
        "teacher/classes/<int:offering_id>/attendance/",
        teacher_attendance,
        name="teacher_attendance",
    ),

    path(
        "student/courses/<int:enrollment_id>/attendance/",
        student_attendance,
        name="student_attendance",
    ),

]