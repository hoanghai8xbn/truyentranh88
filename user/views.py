from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import profile
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        f = UserRegisterForm(request.POST)
        if f.is_valid():
            user = f.save()
            p = profile.objects.create(user=user)
            p.save()
            username = f.cleaned_data['username']
            messages.success(request, f"Account Create For {username}")
            return redirect("home")
    else:
        f = UserRegisterForm()
    return render(request, 'user/register.html', {"f":f})

@login_required
def profile_user(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.save():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated successfully!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user/profile.html',{"u_form": u_form, "p_form": p_form})


