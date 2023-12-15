# from django.contrib.auth.forms import UserCreationForm
# from .forms import CreationUserForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login,logout
# from .models import CustomUser


# def register(request):
#     form = CreationUserForm()
#     if request.method == 'POST':
#         form = CreationUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account  was created for' + user)
            
#             return redirect('login')
#     context = {
#         'form': form,
#     }
#     return render(request, 'register.html',context)

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')

      
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
        
#             auth_login(request, user)
#             messages.success(request, 'Create successful account')
#             return redirect('home')
#         # else:
#         #     messages.error(request, 'Invalid username or password. Please try again.')

#     context = {}
#     return render(request, 'login.html', context)



# class View
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.views import View
# from .forms import CreationUserForm  # Import your custom form

# class RegisterView(View):
#     template_name = 'register.html'
#     form_class = CreationUserForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         context = {'form': form}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#             return redirect('login')

#         context = {'form': form}
#         return render(request, self.template_name, context)

# class LoginView(View):
#     template_name = 'login.html'

#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password. Please try again.')

#         context = {}
#         return render(request, self.template_name, context)


