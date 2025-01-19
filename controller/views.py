from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.core.exceptions import ValidationError

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        #accessing the values and checking the conditions
        if password1 != password2:
            messages.error(request,"Passwords do no match")
            return redirect('/controller/signup')
        try:
            #checking if the user already exists
            if User.objects.filter(username=email).exists():
                messages.error(request,"Account already exists")
                return redirect("/controller/signup")
            
            #creating user same as email
            new_user = User.objects.create_user(username=email,password=password1,email=email)
            new_user.save()
            login(request,new_user)
            messages.success(request,"Account created successfully")
            return redirect("/controller/login")
        
        except ValidationError as e:
            messages.error(request,e.message)

        
    return render(request,"authentication/signup.html")
        
def handlelogin(request):
    if request.method == "POST":
        user_email=request.POST['email']
        user_password=request.POST['pass1']
        #authenticate user
        user = authenticate(request,username=user_email,password=user_password)
        if user is not None:
            #if user exists log in
            login(request,user)
            user.is_active = True
            return redirect('/')
        else:
            #authenticate fails
            messages.error(request,"Invalid email or password")
            return redirect("/controller/login")
    return render(request,"authentication/login.html")

def handlelogout(request):
    logout(request)
    
    messages.success(request,"LogOut Success")
    return redirect("/controller/login")