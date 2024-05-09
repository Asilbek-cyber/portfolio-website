from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from .bot import send_message
# Create your views here.
def home_view(request):
    if request.method== "GET":
        form = ContactForm()
    else:
            # contact = Contact.objects.all()
            form = ContactForm(request.POST)
            if form.is_valid():
                name =  form.cleaned_data["name"]
                email =  form.cleaned_data["email"]
                subject =  form.cleaned_data["subject"]
                message =  form.cleaned_data["message"]
                send_message(name,email,subject,message)
                form.save()
                form = ContactForm()
    context = {"form":form}

    return render(request,"index.html",context)

def inner_view(request):
    return render(request,"inner-page.html")

def portfolio_view(request):
    return render(request,"portfolio-details.html")