from django.conf.urls import url
from dashboard import views as v

urlpatterns = [
    url('^$', v.index, name='indexDashboard')
]
