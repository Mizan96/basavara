from django.shortcuts import render, redirect

from app_account.forms import SignupForm, LoginForm, ContactForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as login_user, logout as logout_user

from app_account.models import ContactModel


def login(request):
    context = {
        'login': LoginForm,
        'error': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('/')
        else:
            context['error'] = 'username or password doesn\'t match'
    return render(request, 'login.html', context)

def logout(request):
    logout_user(request)
    return redirect('/')



def signup(request):
    context = {
        'signup': SignupForm
    }
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
                )
            return redirect('login')
        else:
            context = {
                'signup': form
            }
    return render(request, 'signup.html', context)


def contact(request):
    context = {
        'contact': ContactForm
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactModel.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('/')
    return render(request, 'contact.html', context)




