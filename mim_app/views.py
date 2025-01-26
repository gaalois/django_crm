from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check if the user is logging in
    if request.method == 'POST':
        username = request.POST.get('username')  # Utilisez .get() pour éviter KeyError
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('home')  # Redirection après connexion réussie
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('home')  # Redirection après échec
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)  # Déconnexion de l'utilisateur
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
