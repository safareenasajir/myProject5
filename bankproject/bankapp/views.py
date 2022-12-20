from django.contrib import auth,messages
from django.shortcuts import render, redirect
from . models import Bank

# Create your views here.
def home(request):

    return render(request,'home.html')
def register(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            cpassword=request.POST['cpassword']

            if password == cpassword:
                if Bank.objects.filter(username=username).exists():
                    messages.info(request, "username exist")
                    return redirect('register')

                else:

                    user = Bank(username=username, password=password)

                    user.save()
                    return redirect('login')

                # return redirect('/')
            else:
                messages.info(request, "password not match")
                return redirect('login')

    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return  redirect('/')
            else:
                messages.info(request, "invalid credential")
                return  redirect('bank')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def bank(request):
    return render(request,'bank.html')
def message(request):
    return render(request,'message.html')


