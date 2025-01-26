from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str,force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.views import View
from django.contrib.auth.forms import SetPasswordForm


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

        
    return render(request,"signup.html")
        
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
    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    
    messages.success(request,"LogOut Success")
    return redirect("/controller/login")
            
class RequestPasswordResetView(View):
    def get(self, request):
        return render(request, 'request_password_reset.html')

    def post(self, request):
        email = request.POST.get('email')
        print(f"Received email: {email}")  
        try:
            request.session['reset_email'] = email
            return render(request,'set-new-password.html')
        except User.DoesNotExist:
            messages.error(request, "No user found with this email address.")
            return render(request, 'request_password_reset.html')


class SetNewPasswordView(View):
    def get(self, request):
        email = request.session.get('reset_email')
        if email:
            return render(request, 'set_new_password.html', {'email': email})
        else:
            messages.error(request, "No email address found.")
            return redirect('/controller/request-password-reset')

    def post(self, request):
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        email = request.session.get('reset_email')


        if not new_password or not confirm_password:
            messages.error(request, "Both password fields are required.")
            return render(request, 'set_new_password.html', {'email': email})

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'set_new_password.html', {'email': email})

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Your password has been successfully updated.")
            return redirect('/controller/login')  # Redirect to login or another page
        except User.DoesNotExist:
            messages.error(request, "User  not found.")
            return redirect('/controller/request-password-reset')