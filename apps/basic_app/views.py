from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "basic_app/index.html", {"nbar": "index"})

def register(request):
    registration_success = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # Get the data from the form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registration_success = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(
        request,
        "basic_app/registration.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registration_success": registration_success,
            "nbar": "register",
        },
    )

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("basic_app:index"))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("basic_app:index"))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login")
    else:
        return render(request, "basic_app/login.html", {"nbar": "login"})