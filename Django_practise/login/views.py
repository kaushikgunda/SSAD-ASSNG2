from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponseRedirect,reverse,render_to_response
from .forms import SignupForm, LoginForm,UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext


def home(request):
    context = {

    }
    return render(request, "login/home.html", context)


def signup(request):
    title = 'Welcome '
    if request.user.is_authenticated():
        title += str(request.user)
    else:
        title += "Guest"

    form = SignupForm(request.POST or None)

    context = {
        "title": "Signup",
        "form": form,
        "formname": "Register",
    }
    if form.is_valid():
        instance = form.save()
        instance.set_password(instance.password)
        instance.save()
        return redirect("/")
    return render(request,"login/form.html", context)



def form_login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
        "formname": "Login",
        "title":"Login",
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")

    return render(request, "login/form.html", context)

@login_required
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/editprofile')
    else:
        form = UpdateProfileForm(instance=request.user)

    args['form'] = form
    return render(request, 'login/update_profile.html', args)

def form_logout(request):
    logout(request)
    return redirect("/")