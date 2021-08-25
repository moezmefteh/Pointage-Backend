from django.contrib import admin

# Register your models here.
from users.models import *

admin.site.register(User)
admin.site.register(pointage)
admin.site.register(salaire)
admin.site.register(mission)