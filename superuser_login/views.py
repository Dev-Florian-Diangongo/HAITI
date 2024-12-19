
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
def superuser_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/dashbord/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin')  
        else:
            return HttpResponseForbidden("Accès interdit. Vous devez être un superutilisateur.")
    return render(request, 'login.html')
def deconnexion(request) :
    logout(request)
    return redirect("login")