from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, '../templates/index.html', locals())


def contacts(request):
    return render(request, '../templates/contacts.html', locals())


def about(request):
    return render(request, '../templates/about.html', locals())


def schedule(request):
    return render(request, '../templates/schedule.html', locals())
