from django.shortcuts import render

def home_login(request):
    return render(request, 'usuarios/login_page.html')

def register(request):
    return render(request, 'usuarios/register_page.html')