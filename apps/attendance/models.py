from django.db import models


class Attendance(models.Model):

    enrollment = models.ForeignKey(
        "enrollments.Enrollment",
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    date = models.DateField()

    present = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["enrollment", "date"],
                name="unique_attendance_per_day",
            )
        ]

    def __str__(self):
        status = "Present" if self.present else "Absent"

        return (
            f"{self.enrollment.student.user.username} - "
            f"{self.enrollment.course_offering.course.code} - "
            f"{self.date} - "
            f"{status}"
        )