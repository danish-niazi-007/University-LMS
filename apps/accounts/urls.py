from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    UserLoginView,
    student_dashboard,
    teacher_dashboard,
    hod_dashboard,
)


urlpatterns = [

    # Authentication
    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),

    # Student
    path(
        "student/dashboard/",
        student_dashboard,
        name="student_dashboard",
    ),

    # Teacher
    path(
        "teacher/dashboard/",
        teacher_dashboard,
        name="teacher_dashboard",
    ),

    # HOD Dashboard
    path(
        "hod/dashboard/",
        hod_dashboard,
        name="hod_dashboard",
    ),
]