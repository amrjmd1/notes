from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from dashboard.models import noteHistory, logHistory
from note.models import User, Note


def index(request):
    if request.session.get('user', None):
        return HttpResponseRedirect("/" + request.session['user'])
    return HttpResponseRedirect(reverse('chLogin'))


def note(request, username):
    if request.session.get('user', None):
        if request.session['user'] == username:
            user = User.objects.get(userName=username)
            notes = Note.objects.filter(user=user)
            context = {
                "name": user,
                "note": notes
            }
            return render(request, 'note.html', context)
        else:
            return render(request, 'pageNotFound.html')
    return render(request, 'pageNotFound.html')


def ch_login(request):
    if not request.session.get('user', None):
        if request.method == "POST":
            user = request.POST.get('userName')
            password = request.POST.get('password')
            username = User.objects.filter(userName=user).first()
            if username and username.password == password:
                request.session['user'] = user
                agent = request.META['HTTP_USER_AGENT'].split()
                login = logHistory(user=username, agent=agent[len(agent) - 1], status=True)
                login.save()
                user = user
                message = "Done"
            else:
                message = "null"
        else:
            return render(request, "login.html", {})
        return JsonResponse({'login': message, 'username': user})
    else:
        return HttpResponseRedirect(reverse('index'))


def ch_signup(request):
    if request.method == "POST":
        username = request.POST.get('username').replace(' ', '')
        name = request.POST.get('name')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if User.objects.filter(userName=username).first():
            message = 'account'
        elif username and name and password and repassword:
            if len(str(password)) > 7:
                if password != repassword:
                    message = 'repassword'
                else:
                    newUser = User(userName=username, name=name, password=password)
                    newUser.save()
                    agent = request.META['HTTP_USER_AGENT'].split()
                    login = logHistory(user=newUser, agent=agent[len(agent) - 1], status=True)
                    login.save()
                    request.session['user'] = username
                    message = 'done'
            else:
                message = 'length'
        else:
            message = 'null'
    else:
        return HttpResponseRedirect(reverse('chLogin'))
    return JsonResponse({'signup': message, 'username': username})


def del_session(request):
    if request.session.get('user', None):
        agent = request.META['HTTP_USER_AGENT'].split()
        logout = logHistory(user=User.objects.filter(userName=request.session['user']).first(),
                            agent=agent[len(agent) - 1], status=False)
        logout.save()
        del request.session['user']
        return HttpResponseRedirect(reverse('chLogin'))
    return HttpResponseRedirect(reverse('chLogin'))


def disableAccount(request):
    if request.session.get('user', None):
        userSession = request.session.get('user')
        if User.objects.filter(userName=userSession).filter():
            username = User.objects.filter(userName=userSession).first()
            if username.active:
                username.active = False
                status = False
            else:
                username.active = True
                status = True
            username.save()
            return JsonResponse({'active': 'done', 'status': status})
        return HttpResponseRedirect(reverse('chLogin'))
    return HttpResponseRedirect(reverse('chLogin'))


def addNote(request):
    if request.method == "POST":
        user = request.session['user']
        username = User.objects.get(userName=user)
        if username.active:
            background = request.POST.get('colors')
            title = request.POST.get('title')
            cont = request.POST.get('cont')
            if title != '' or cont != '':
                addNew = Note(user=username, title=title, textNote=cont, background=background)
                addNew.save()
                agent = request.META['HTTP_USER_AGENT'].split()
                history = noteHistory(user=username, agent=agent[len(agent) - 1], status=True)
                history.save()
                msg = 'done'
                renote = [title, cont, background]
            else:
                msg = 'nop'
                renote = 'null'
        return JsonResponse({
            'msg': msg,
            'renote': renote
        })


def deleteNote(request, id):
    if request.session.get('user', None):
        note = Note.objects.filter(id=id).first()
        if note:
            if note.user.userName == request.session.get('user'):
                if note.user.active:
                    if note.delete():
                        agent = request.META['HTTP_USER_AGENT'].split()
                        history = noteHistory(user=note.user, agent=agent[len(agent) - 1], status=False)
                        history.save()
                        msg = 'done'
                    else:
                        msg = 'null'
                else:
                    msg = 'null'
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        msg = 'null'
    return JsonResponse({'msg': msg})


def avatar(request):
    if request.method == 'POST':
        if request.FILES:
            av = request.FILES['avatar']
            user = User.objects.filter(userName=request.session['user']).first()
            user.avatar = av
            user.save()
    # if user.save():
    #         msg = 'done'
    #     else:
    #         msg = 'non'
    # else:
    #     msg = 'notPost'
    # return JsonResponse({'msg': msg})
    return HttpResponseRedirect(reverse("index"))
