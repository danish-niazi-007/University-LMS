from django.contrib import admin

from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "enrollment",
        "date",
        "present",
    )

    list_filter = (
        "present",
        "date",
    )

