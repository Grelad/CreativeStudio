from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    # context = {"index_page": "active"}
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/index.html', locals())


def contacts(request):
    context = {"contacts_page": "active"}
    return render(request, 'landing/contacts.html', context)


def about(request):
    context = {"about_page": "active"}
    return render(request, 'landing/about.html', context)


def schedule(request):
    context = {"schedule_page": "active"}
    return render(request, 'landing/schedule.html', context)
