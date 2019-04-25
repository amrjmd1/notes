from django.db import models


def up_img(User, filename):
    name, ext = filename.split(".")
    return "avatar/%s/%s.%s" % (User.userName, User.userName, ext)


class User(models.Model):
    name = models.CharField(max_length=60)
    userName = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to=up_img, default='avatar/account.png')
    active = models.BooleanField(default=True)
    timeSignUp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    UpdateUser = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, null=True)
    textNote = models.TextField()
    background = models.CharField(max_length=7, default="#ffffff")
    timePost = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    timeEditPost = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.title
