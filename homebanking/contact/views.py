

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
# Create your views here.
def contact(request):
    contact_form = ContactForm
    
    if request.method == "POST":
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
        return redirect(reverse('contact')+"?ok")
    return render(request, "contact/contact.html", {'form':contact_form})