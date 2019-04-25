from django.db import models
from note.models import User


class logHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    agent = models.CharField(max_length=120)
    status = models.BooleanField()

    def __str__(self):
        return str(self.time)


class noteHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    agent = models.CharField(max_length=120)
    status = models.BooleanField()

    def __str__(self):
        return str(self.time)
