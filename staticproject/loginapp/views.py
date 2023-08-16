from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user details')
            return redirect('userlogin')

    return render(request,'userlogin.html')

def credentials(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['password2']
        if password==conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('credentials')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken already')
                return redirect('credentials')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                return redirect('userlogin')
        else:
            print("password not matching")
        return redirect('/')
    return render(request,'login.html')
def userlogout(request):
    auth.logout(request)
    return redirect('/')
