from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

def home(request):
    return render(request, 'users/home.html',{'title':'Home'})

def about(request):
    return render(request, 'users/about.html',{'title':'About us'})

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfully created !')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'title':'Sign up',
            'form': form
        }
    )

@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if  updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Your account has been successfully updated !')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm,
        'title':'User account'
    }
    return render(request, 'users/profile.html', data)

