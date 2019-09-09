# pages/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


def home_page_view(request):
    return HttpResponse("Hello, World!")


def home_page_view_with_render(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "test_form.html")


def contact_validate(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['name']
        envoi = True
        print(sujet)

    return render(request, 'name.html', locals())
