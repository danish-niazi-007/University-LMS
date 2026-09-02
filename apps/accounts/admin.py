
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    StudentProfile,
    TeacherProfile,
    HODProfile,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "LMS Information",
            {
                "fields": ("role",),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "LMS Information",
            {
                "fields": ("role",),
            },
        ),
    )


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "registration_no",
        "department",
        "semester",
    )

    search_fields = (
        "user__username",
        "registration_no",
    )

    list_filter = (
        "department",
        "semester",
    )


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "employee_id",
        "department",
        "designation",
    )

    search_fields = (
        "user__username",
        "employee_id",
    )

    list_filter = (
        "department",
    )


@admin.register(HODProfile)
class HODProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "department",
    )

    search_fields = (
        "user__username",
        "department__name",
    )

