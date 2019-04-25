from django.contrib import admin
from . import models as m

# Register your models here.

admin.site.register(m.logHistory)
admin.site.register(m.noteHistory)
