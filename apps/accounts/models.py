
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        TEACHER = "teacher", "Teacher"
        HOD = "hod", "HOD"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )

    department = models.ForeignKey(
        "academics.Department",
        on_delete=models.PROTECT,
        related_name="students",
    )

    registration_no = models.CharField(
        max_length=30,
        unique=True,
    )

    phone_no = models.CharField(
        max_length=11,
        blank=True,
    )

    address = models.CharField(
        max_length=200,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    semester = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    degree_program = models.CharField(
        max_length=100,
        blank=True,
    )

    campus = models.CharField(
        max_length=100,
        blank=True,
    )

    profile_pic = models.ImageField(
        upload_to="profiles/students/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username} - Student"


class TeacherProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
    )

    department = models.ForeignKey(
        "academics.Department",
        on_delete=models.PROTECT,
        related_name="teachers",
    )

    employee_id = models.CharField(
        max_length=30,
        unique=True,
    )

    phone_no = models.CharField(
        max_length=11,
        blank=True,
    )

    address = models.CharField(
        max_length=200,
        blank=True,
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    cnic = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
    )

    profile_pic = models.ImageField(
        upload_to="profiles/teachers/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username} - Teacher"


class HODProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="hod_profile",
    )

    department = models.OneToOneField(
        "academics.Department",
        on_delete=models.PROTECT,
        related_name="hod_profile",
    )

    phone_no = models.CharField(
        max_length=11,
        blank=True,
    )

    profile_pic = models.ImageField(
        upload_to="profiles/hods/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username} - HOD"