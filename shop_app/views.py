from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        pnumber = request.POST.get('pnumber')
        myquery = models.Contact(name=name,email=email,desc=desc,phone_number=pnumber)
        myquery.save()
        messages.success(request,"Query Sent")
        return redirect("/")
    return render(request,"contact.html")





