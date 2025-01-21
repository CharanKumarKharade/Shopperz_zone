from math import ceil
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
# Create your views here.
def index(request):
    allProds = []
    
    # Get distinct categories
    catProds = models.Product.objects.values('category','id')
    print(catProds)
    # Create a set of unique categories
    cats = {item['category'] for item in catProds}
    
    # Loop through each category
    for cat in cats:
        prod = models.Product.objects.filter(category=cat)
        n = len(prod)
        
        # Calculate the number of slides (pages) for each category
        nSlides = (n + 3) // 4  # Rounded up division by 4
        
        # Append the products and slide information to allProds
        allProds.append({
            'products': prod,
            'range': range(1, nSlides + 1),  # Range starts from 1 to nSlides
            'nSlides': nSlides
        })
    
    # Pass the data to the template
    params = {'allProds': allProds}
    return render(request, "index.html", params)


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





