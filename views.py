from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        c = Contact(name = name, email = email, number = number, desc = desc)
        c.save()
        messages.success(request, "Your response has been sent.") 
    return render(request,'contact.html')