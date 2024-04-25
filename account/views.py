from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import RegisterForm


def loginUser(request):
    page = "login"

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('gallery')
        else:
            messages.error(request, 'User does not exist, check username or password and try again')
    context={
        'page': page
    }
    return render(request, 'account/loginRegister.html', context)

def registerUser(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery')
    return render(request, 'account/loginRegister.html')

def logoutUser(request):
    logout(request)
    return redirect('welcome')

def deactivateUser(request):
    return render(request, 'account/deactivate.html')

