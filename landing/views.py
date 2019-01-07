from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *


def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, '../templates/index.html', locals())


def contacts(request):
    title = Contact.objects.all()
    content = Contact.objects.all()
    data = {
        "title": title,
        "content": content,
    }
    return render(request, '../templates/contacts.html', data)


def about(request):
    title = About.objects.all()
    content = About.objects.all()
    data = {
        "title": title,
        "content": content,
    }
    return render(request, '../templates/about.html', data)


def schedule(request):
    title = Schedule.objects.all()
    content = Schedule.objects.all()
    data = {
        "title": title,
        "content": content,
    }
    return render(request, '../templates/schedule.html', data)
