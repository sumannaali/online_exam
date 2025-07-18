from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Invigilator(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.employee_id})"


class Exam(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Midterm", "Final"
    date = models.DateField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='exams',
        null=True, blank=True
    )
    invigilator = models.ForeignKey(
        Invigilator, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='exams'
    )

    def __str__(self):
        if self.subject:
            return f"{self.name} - {self.subject.name}"
        return f"{self.name} - No Subject"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, null=True, blank=True)  # ✅ CORRECT!

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Question(models.Model):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name='questions'
    )
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='results'
    )
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name='results'
    )
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()

    class Meta:
        unique_together = ('student', 'exam')
        verbose_name_plural = 'Results'

    def __str__(self):
        return f"{self.student.name} - {self.exam.name}"

    def percentage(self):
        if self.total_marks:
            return (self.marks_obtained / self.total_marks) * 100
        return 0