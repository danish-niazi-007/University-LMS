from django.db import models


class Enrollment(models.Model):

    student = models.ForeignKey(
        "accounts.StudentProfile",
        on_delete=models.PROTECT,
        related_name="enrollments",
    )

    course_offering = models.ForeignKey(
        "courses.CourseOffering",
        on_delete=models.PROTECT,
        related_name="enrollments",
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course_offering"],
                name="unique_student_course_offering",
            )
        ]

    def __str__(self):
        return (
            f"{self.student.user.username} - "
            f"{self.course_offering.course.code} - "
            f"{self.course_offering.academic_year}"
        )