from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.core.mail import send_mail
import random
from django.http import HttpResponse


def login_view(request):
    return HttpResponse("Login page")

# ✅ Helper: Send OTP using email
def send_otp(email):
    otp = str(random.randint(100000, 999999))
    print(f"Generated OTP: {otp} for {email}")

    subject = "Your OTP Code"
    message = f"Your OTP is {otp}"
    from_email = 'your_email@gmail.com'  # Replace with your sender email
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return otp

# ✅ LOGIN VIEW (OTP via email)
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            email = user.email
            if email:
                otp = send_otp(email)
                request.session['otp'] = otp
                request.session['email'] = email
                return redirect('verify_otp')
            else:
                messages.error(request, "No email found for this user.")
                logout(request)
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'examination/auth.html', {'show_login': True})

# ✅ REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        role = request.POST.get('role')
        phone = request.POST.get('phone')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            Profile.objects.create(user=user, role=role, phone=phone)
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')

    return render(request, 'examination/auth.html', {'show_register': True})

# ✅ VERIFY OTP VIEW
def verify_otp_view(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        actual_otp = request.session.get('otp')

        if entered_otp == actual_otp:
            messages.success(request, "OTP verified successfully!")
            request.session.pop('otp', None)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'examination/auth.html', {'show_otp': True})
def teacher_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and hasattr(user, 'profile') and user.profile.role == 'teacher':
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid teacher credentials.")

    return render(request, 'examination/teacher_login.html')


# ✅ HOME VIEW
def home(request):
    return render(request, 'examination/home.html')

# ✅ DASHBOARD VIEW
def dashboard_view(request):
    return render(request, 'examination/dashboard.html')

# ✅ LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ QUESTION LIST VIEW
def question_list(request):
    return render(request, 'examination/question_list.html')

# ✅ EXAM QUESTIONS VIEW
def exam_questions(request, exam_id):
    context = {'exam_id': exam_id}
    return render(request, 'examination/exam_questions.html', context)

# ✅ AUTH SUCCESS VIEW
def auth_success_view(request):
    return render(request, 'examination/auth_success.html')

def login_view(request):
    return HttpResponse("Login Page")

def login_view(request):
    return render(request, 'examination/auth.html', {'show_login': True})



