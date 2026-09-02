


from django.urls import path

from .views import (
    teacher_classes,
    teacher_class_detail,
    teacher_class_students,
)


urlpatterns = [

    path(
        "teacher/classes/",
        teacher_classes,
        name="teacher_classes",
    ),

    path(
        "teacher/classes/<int:offering_id>/",
        teacher_class_detail,
        name="teacher_class_detail",
    ),

    path(
        "teacher/classes/<int:offering_id>/students/",
        teacher_class_students,
        name="teacher_class_students",
    ),
]