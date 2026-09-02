from django.contrib import admin

from .models import Course, CourseOffering

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "department",
        "semester",
        "credit_hours",
    )

    search_fields = (
        "code",
        "name",
    )

    list_filter = (
        "department",
        "semester",
    )

@admin.register(CourseOffering)
class CourseOfferingAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "teacher",
        "academic_year",
    )

    search_fields = (
        "course__code",
        "course__name",
        "teacher__user__username",
        "teacher__employee_id",
    )

    list_filter = (
        "academic_year",
        "course__department",
        "course__semester",
    )