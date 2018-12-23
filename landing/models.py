from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)
