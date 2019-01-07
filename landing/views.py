from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    # context = {"index_page": "active"}
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, '../templates/index.html', locals())


def contacts(request):
    context = {"contacts_page": "active"}
    return render(request, '../templates/contacts.html', context)


def about(request):
    context = {"about_page": "active"}
    return render(request, '../templates/about.html', context)


def schedule(request):
    context = {"schedule_page": "active"}
    return render(request, '../templates/schedule.html', context)
