from django.shortcuts import render, redirect
from .firebase_config import auth, db
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')

        try:
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            # Firestore-ге жазу
            db.collection('users').document(uid).set({
                'name': name,
                'email': email,
                'city': city,
                'role': 'student'  # немесе 'teacher', 'moderator' – ролдерге қарай
            })
            messages.success(request, 'Тіркелу сәтті аяқталды. Енді жүйеге кіріңіз.')
            return redirect('login')
        except:
            messages.error(request, 'Тіркелу кезінде қате шықты.')
    return render(request, 'register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
import pyrebase

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            request.session['uid'] = user['localId']
            return render(request, 'base.html')  # 🔁 redirect емес, render
        except:
            messages.error(request, 'Қате email немесе құпиясөз')

    return render(request, 'login.html')  # немесе 'login.html' нақты жолыңыз қандай болса

def base_view(request):
    return render(request, 'base.html')

def home(request):
    uid = request.session.get('uid')
    if uid:
        user_doc = db.collection('users').document(uid).get()
        user_data = user_doc.to_dict() if user_doc.exists else {}
        return render(request, 'home.html', {'user': user_data})
    return redirect('login')


def logout_view(request):
    request.session.flush()
    return redirect('login')

def courses_view(request):
    return render(request, 'courses.html')

def tests_view(request):
    return render(request, 'tests.html')