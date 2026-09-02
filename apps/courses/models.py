from django.db import models


class Course(models.Model):

    department = models.ForeignKey(
        "academics.Department",
        on_delete=models.PROTECT,
        related_name="courses",
    )

    semester = models.PositiveIntegerField()

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=30,
    )

    credit_hours = models.PositiveIntegerField(
        default=3,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["semester", "code"]
        constraints = [
            models.UniqueConstraint(
                fields=["department", "semester", "code"],
                name="unique_course_per_department_semester",
            )
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"
class CourseOffering(models.Model):

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.PROTECT,
        related_name="offerings",
    )

    teacher = models.ForeignKey(
        "accounts.TeacherProfile",
        on_delete=models.PROTECT,
        related_name="course_offerings",
    )

    academic_year = models.CharField(
        max_length=20,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "teacher", "academic_year"],
                name="unique_course_offering",
            )
        ]

    def __str__(self):
        return (
            f"{self.course.code} - "
            f"{self.teacher.user.get_full_name() or self.teacher.user.username} "
            f"({self.academic_year})"
        )