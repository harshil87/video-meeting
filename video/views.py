from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request,"index.html")


def user_register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,"register.html",{'error':form.errors.as_text()})

    return render(request,"register.html")

def user_login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    return render(request,"login.html")

@login_required(login_url='login')
def video_call(request):
    return render(request,"videocall.html")

def join_room(request):
    if request.method == "POST":
        roomID = request.POST.get('roomid')
        return redirect('/meeting?roomID=' + roomID)
    return render(request, "joinroom.html")


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
