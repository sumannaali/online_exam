from django.urls import path
from . import views  # <-- this imports your app's views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('questions/', views.question_list, name='question_list'),
    path('exam/<int:exam_id>/', views.exam_questions, name='exam_questions'),
    path('auth-success/', views.auth_success_view, name='auth_success'),
]

