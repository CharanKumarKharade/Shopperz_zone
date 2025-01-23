from math import ceil
from django.shortcuts import redirect, render

from . import models
from django.contrib import messages
# Create your views here.
def index(request):

    allProds = []
    catprods = models.Product.objects.values('category','id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= models.Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}

    return render(request,"index.html",params)

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





