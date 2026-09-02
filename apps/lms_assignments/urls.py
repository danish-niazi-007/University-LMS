from django.urls import path

from .views import (
    teacher_assignments,
    create_assignment,
    assignment_submissions,
    submit_assignment,
    download_submission,
)


urlpatterns = [

    path(
        "teacher/classes/<int:offering_id>/assignments/",
        teacher_assignments,
        name="teacher_assignments",
    ),

    path(
        "teacher/classes/<int:offering_id>/assignments/create/",
        create_assignment,
        name="create_assignment",
    ),

    path(
        "teacher/classes/<int:offering_id>/assignments/<int:assignment_id>/submissions/",
        assignment_submissions,
        name="assignment_submissions",
    ),

    path(
        "student/courses/<int:enrollment_id>/assignments/<int:assignment_id>/submit/",
        submit_assignment,
        name="submit_assignment",
    ),

    path(
        "submissions/<int:submission_id>/download/",
        download_submission,
        name="download_submission",
    ),

]