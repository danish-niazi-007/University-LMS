from django.contrib import admin

from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):


    list_display = (
        "student",
        "course_offering",
        "enrolled_at",
    )

    search_fields = (
        "student__user__username",
        "student__registration_no",
        "course_offering__course__code",
        "course_offering__course__name",
    )

    list_filter = (
        "course_offering__academic_year",
        "course_offering__course__department",
        "course_offering__course__semester",
    )

