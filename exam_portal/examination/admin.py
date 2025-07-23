from django.contrib import admin
from .models import Profile, Student, Invigilator, Subject, Exam, Question, Result

# Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'otp']

# Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'roll_number', 'department']
    search_fields = ['roll_number', 'user__username', 'department']

# Invigilator
@admin.register(Invigilator)
class InvigilatorAdmin(admin.ModelAdmin):
    list_display = ['user', 'staff_id', 'department']
    search_fields = ['staff_id', 'user__username', 'department']

# Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

# Exam
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'date', 'duration', 'total_marks']
    list_filter = ['subject', 'date']
    search_fields = ['title']

# Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['exam', 'question_text', 'correct_option']
    list_filter = ['exam']
    search_fields = ['question_text']

# Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'marks_obtained', 'submitted_at']
    list_filter = ['exam', 'submitted_at']
    search_fields = ['student__user__username', 'exam__title']