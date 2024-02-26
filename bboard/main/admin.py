from django.contrib import admin

from main.forms import ApplicationForm
from main.models import *


class ApplicationAdmin(admin.ModelAdmin):
    form = ApplicationForm
    list_display = ('name', 'date', 'username', 'status')
    fields = ('status', 'img', 'comment')
    list_filter = ('status', 'categories')


admin.site.register(Categorise)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(User)
