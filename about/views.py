from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactMeForm

def about_me(request):
    if request.method == "POST":
        contact_form = ContactMeForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Message received! I endeavour to respond within 2 working days.")

    about = About.objects.all()
    contact_form = ContactMeForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
        "contact_form": contact_form
        }
    )


