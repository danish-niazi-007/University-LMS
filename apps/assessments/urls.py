from django.urls import path

from .views import teacher_marks, student_marks

urlpatterns = [
    path(
        "teacher/classes/<int:offering_id>/marks/",
        teacher_marks,
        name="teacher_marks",
    ),

    path(
        "student/courses/<int:enrollment_id>/marks/",
        student_marks,
        name="student_marks",
    ),
]