from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import ContactMeForm


def about_me(request):
    if request.method == "POST":
        contact_form = ContactMeForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()

            return redirect('thanks')
        else:

            messages.error(
                request, 'There was an error sending your message.')
            return render(
                request, 'about/about.html', {'contact_form': contact_form})

    about = About.objects.first()
    contact_form = ContactMeForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "contact_form": contact_form}
    )


def thanks(request):
    return render(request, 'about/thanks.html')
