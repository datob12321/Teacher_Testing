from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user, logout as logout_user
from django.views.decorators.csrf import csrf_exempt


from .models import Status
from django.contrib import messages
from .testing_file import all_questions
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('register')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.teacher_status = False
            user.save()
            status = Status.objects.create(user=user)
            status.save()
            login_user(request, user)
            messages.success(request, 'User is created successfully!')
            return redirect('index')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('index')
    else:
        return render(request, 'login.html')


def logout(request):
    logout_user(request)
    return redirect('login')


@csrf_exempt
def test_page(request):

    if request.method == 'POST':
        #answers = json.loads(request.body)
        # request.body.get('answers_dict', '[]')
        answers = request.body.decode('utf-8')
        # python_dict = json.loads(answers)
        print(dict(answers))
        return redirect('index')
    questions = {'questions': all_questions}
    dict_answers = [{'answer': answer.correct_answer} for answer in questions['questions']]


    return render(request, 'test.html', {'questions': all_questions,
                                         'dict_answers': dict_answers})



