from django.shortcuts import render,redirect
from .forms import student
from .models import entry
from django.db.models import Q
from .forms import singup
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        data=entry.objects.all()
    else:
        return redirect('login')
    return render(request, "index.html", {'data': data})
def form(request):
    if request.user.is_authenticated:
        fm = student()
        if request.method == 'POST':
            fm = student(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('index')
        else:
            fm = student()
    else:
        return redirect('login')
    return render(request, "form.html", {'form': fm})
def delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            d = entry.objects.get(pk=id)
            d.delete()
            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('login')
def edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            d = entry.objects.get(pk=id)
            fm = student(request.POST, instance=d)
            if fm.is_valid():
                fm.save()
                return redirect('index')
        else:
            d = entry.objects.get(pk=id)
            fm = student(instance=d)
    else:
        return redirect('login')
    return render(request, "edit.html", {'form': fm})
def search(request):
    if request.user.is_authenticated:
        d=request.GET['name' or 'contact']
        se = entry.objects.filter(name__icontains=d)
        return render(request, "search.html", {"se": se})
    else:
        return redirect('login')
def user_sign(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = singup(request.POST)
            if fm.is_valid():
                user= fm.save()
                grp = Group.objects.grt(name='student')
                user.groups.add(grp)
                return redirect('index')
        else:
            fm = singup()
        return render(request, "signup.html", {'form': fm})
    else:
        return redirect('index')
def user_logout(request):
    logout(request)
    return redirect('login')
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('index')
        else:
            fm = AuthenticationForm()
        return render(request, "login.html", {'form': fm})
    else:
        return redirect('index')
