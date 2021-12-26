from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name =request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("usernametaken")
                messages.error(request,"Username taken")
                return redirect('/account/register/')
            elif User.objects.filter(email=email).exists():
                print("email taken")
                messages.error(request,"Email taken")
                return redirect('/account/register/')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                messages.error(request,"User account created successfully!!!")
                return redirect('/account/login/')
        else:
            print("password not matching")
            messages.info(request,"password not matching")
        return redirect('/account/register/')

    else:
        return render(request,"account/register.html")


def login_(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        #check if user have entered correct credentials
        user = authenticate(username=username,password=password)

        print(request.user)
        if user is not None:
            login(request,user)
            return redirect('/account/')
        else:
            print("error ho gyi babu")
            messages.info(request,"invalid credentials")
            return redirect('/account/login/')

    else:
        return render(request,"account/login.html")


def logout_(request):
    logout(request)
    return redirect('/account/login/')

def index(request):
    context= {}#request.POST.get('context')
    return render(request,"account/index.html",context)



