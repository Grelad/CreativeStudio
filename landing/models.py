from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=13)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)


class Schedule(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Пользователь %s %s" % (self.title, self.content)


class About(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Пользователь %s %s" % (self.title, self.content)


class Contact(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Пользователь %s %s" % (self.title, self.content)

