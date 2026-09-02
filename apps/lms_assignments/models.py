from django.db import models


class Assignment(models.Model):

    course_offering = models.ForeignKey(
        "courses.CourseOffering",
        on_delete=models.CASCADE,
        related_name="assignments",
    )

    title = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    due_date = models.DateTimeField()

    assignment_file = models.FileField(
        upload_to="assignments/teacher/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return (
            f"{self.course_offering.course.code} - "
            f"{self.title}"
        )


class Submission(models.Model):

    assignment = models.ForeignKey(
        "lms_assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    enrollment = models.ForeignKey(
        "enrollments.Enrollment",
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    submission_file = models.FileField(
        upload_to="assignments/student/",
        blank=True,
        null=True,
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["assignment", "enrollment"],
                name="unique_assignment_submission",
            )
        ]

    def __str__(self):
        return (
            f"{self.enrollment.student.user.username} - "
            f"{self.assignment.title}"
        )