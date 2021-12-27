from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout


def isValid(password):

    # for checking if password length
    # is between 8 and 16
    if (len(password) < 8 or len(password) > 16):
        return False

    # to check space
    if (" " in password):
        return False

    if (True):
        count = 0

        # check digits from 0 to 9
        arr = ['0', '1', '2', '3',
        '4', '5', '6', '7', '8', '9']

        for i in password:
            if i in arr:
                count = 1
                break
        if count == 0:
            return False

    # for special characters
    if True:
        count = 0
        arr = ['#','!','~','$','%','^',
                '&','*','(',',','-','+','/',
                ':','.',',','<','>','?','|']

        for i in password:
            if i  in arr:
                return False

    if True:
        count = 0

        # checking capital letters
        for i in range(65, 91):
            if chr(i) in password:
                count = 1
        if (count == 0):
            return False

    if True:
        count = 0

        # checking '@
        if '@' in password:
            count = 1
        if (count == 0):
            return False

    if (True):
        count = 0

        # checking small letters
        for i in range(90, 123):
            if chr(i) in password:
                count = 1
        if (count == 0):
            return False

    # if all conditions fails
    return True


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name =request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = username
        if password1 == password2:
            if not isValid([i for i in password1]):
                messages.error(request,"USe only alpha, nums, Capital and @")
                return redirect('/account/register/')
            elif User.objects.filter(username=username).exists():
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



