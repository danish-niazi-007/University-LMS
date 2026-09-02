from django.db import models


class Marks(models.Model):

    enrollment = models.OneToOneField(
        "enrollments.Enrollment",
        on_delete=models.CASCADE,
        related_name="marks",
    )

    sessional = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    midterm = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    final = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ["enrollment"]

    @property
    def total(self):
        return self.sessional + self.midterm + self.final

    def __str__(self):
        return (
            f"{self.enrollment.student.user.username} - "
            f"{self.enrollment.course_offering.course.code}"
        )