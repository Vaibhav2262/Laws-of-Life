from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def about(request):
    return render(request,'about.html')
    
def home(request):
    return render(request,'home.html')  # First Page

def index(request):
     print('result is :',request.user.is_authenticated)
     return render(request,'index.html') # Second page

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        context={}  # empty dectionary
        if uname=="" or upass=="" or ucpass=="":  # check the those thick
            context['errmsg']="Fields cannot be Empty"    # pass key and value to dectonary
        elif upass != ucpass:
            context['errmsg']="Password & confirm password didn't match"
        # pass value in database
        else:
            try:
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)  # pass word is not visible in database
                u.save()
                context['success']="User Created Successfully, Please Login"
            except Exception:
                context['errmsg']='user with same username already exists!!!!!!!'
        #return HttpResponse("User created successfully!!")
        return render(request,'register.html',context)
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        #print (uname, '-,upass')

        context={}
        if uname=="" or upass=="":  # check the those thick
            context['errmsg']="Fields cannot be Empty"    # pass key and value to dectonary
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/index')
            else:
                context['errmsg']="Invallid user and password"
                return render(request,'login.html',context)

            #print(u) #object  ==>> sell the record on terminal 
            #print(u.password)
            #print(u.is_superuser)  #0- false
            return HttpResponse("Data is fetched")
    else:
        return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')