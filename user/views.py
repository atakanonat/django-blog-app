from django.contrib.auth.base_user import AbstractBaseUser
from django.forms.widgets import PasswordInput
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def register(request):
    # Check if request equals POST or GET
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")

        newUser = User(username=username, first_name=first_name,
                       email=email)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Welcome, " + username + "!")

        return redirect("index")
    else:
        context = {
            "form": form,
        }
        return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome, " + username + "!")
            return redirect("index")
        else:
            messages.warning(
                request, "Incorrect username or password!")
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


@login_required(login_url="user:login")
def logoutUser(request):
    logout(request)
    messages.info(request, "Account logged out.")
    return redirect("index")


@login_required(login_url="user:login")
def updateProfile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES or None, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user:updateProfile')
        else:
            messages.warning(request, "Please check the given informations.")
        return render(request, "userAccount.html", {'user_form': user_form, 'profile_form': profile_form})
    return render(request, "userAccount.html", {'user': user})
