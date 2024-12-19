
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
def superuser_login(request):
    # Si l'utilisateur est déjà connecté et est un superutilisateur, le rediriger vers la page d'administration
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/dashbord/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Tenter d'authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)
        # Si l'utilisateur est un superutilisateur
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin')  # Redirection vers la page de dashbord
        else:
            return HttpResponseForbidden("Accès interdit. Vous devez être un superutilisateur.")
    return render(request, 'login.html')
