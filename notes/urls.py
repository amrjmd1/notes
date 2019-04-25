from django.conf.urls import url, include
from django.contrib import admin
from note import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.ch_login, name='chLogin'),
    url(r'^signup', views.ch_signup, name='chSignup'),
    url(r'^addnote', views.addNote, name='addNote'),
    url(r'^logout$', views.del_session, name='logout'),
    url(r'^disableaccount$', views.disableAccount, name='disableAccount'),
    url(r'^(?P<username>[\w]+)$', views.note, name='note'),
    url(r'^deletenote/(?P<id>\d+)/$', views.deleteNote, name='deleteNote'),
    url(r'^avatar/$', views.avatar, name='up-avatar'),
    url(r'^dashboard/', include('dashboard.urls'), name='dashboard')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
