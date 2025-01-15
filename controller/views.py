from django.shortcuts import redirect, render

# Create your views here.
def signup(request):
    return render(request,"authentication/signup.html")

def handlelogin(request):
    return render(request,"authentication/login.html")

def handlelogout(request):
    return redirect("/controller/login")