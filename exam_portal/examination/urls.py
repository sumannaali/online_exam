from django.contrib import admin
from django.urls import path
from examination import views  # your app name is examination

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  # ✅ Add this line
    path('register/', views.register_view, name='register'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('questions/', views.question_list, name='question_list'),
    path('exam/<int:exam_id>/', views.exam_questions, name='exam_questions'),
    path('auth-success/', views.auth_success_view, name='auth_success'),
    path('teacher-login/', views.teacher_login_view, name='teacher_login'),
]
