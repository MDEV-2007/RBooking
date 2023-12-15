from django.shortcuts import render,redirect
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user, created = User.objects.get_or_create(username=username, email=email, last_name=last_name)
                if created:
                    user.set_password(password)
                    user.save()
                    # messages.success(request, 'Registration successful. You can now log in.')
                    return redirect('login')
                else:
                    messages.error(request, 'An account with this email or username already exists.')
                    return redirect('register')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Username and password are required.')
    
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home') 

@login_required
def profile_page(request):
    return render(request, 'profile.html')