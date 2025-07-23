from django.db import models
from django.contrib.auth.models import User

# Profile for OTP & phone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

# Invigilator (Teacher) Model
class Invigilator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

# Exam Model
class Exam(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.title

# Question Model
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=10)

    def __str__(self):
        return self.question_text[:50]

# Result Model
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.title}"