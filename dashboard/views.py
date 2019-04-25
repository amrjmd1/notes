from django.shortcuts import render, HttpResponseRedirect, reverse
from django.db.models import Q
from note.models import User, Note
from . import models
import datetime


# Create your views here.
def index(request):
    if request.session.get('user', None):
        user = User.objects.get(userName=request.session.get('user'))
        log = models.logHistory.objects.filter(user=user)
        noteHistory = models.noteHistory.objects.filter(user=user)
        note = Note.objects.filter(user=user)
        date = str(datetime.datetime.today()).split()[0]
        noteDay = Note.objects.filter(Q(timePost__startswith=date))
        print(date, '>>>>>>>>>>>>>>>>>>>>>>>>', noteDay.count())
        context = {
            'user': user,
            'noteCount': note.count(),
            'log': log,
            'noteHistory': noteHistory,
            'n': noteDay
        }
        return render(request, 'dashboard/dashboard.html', context)
    return HttpResponseRedirect(reverse('chLogin'))
