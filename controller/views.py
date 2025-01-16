from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,"authentication/signup.html")
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email is taken")
                return render(request,"authentication/signup.html")
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active = False
        user.save()
    return render(request,"authentication/signup.html")

def handlelogin(request):
    return render(request,"authentication/login.html")

def handlelogout(request):
    return redirect("/controller/login")