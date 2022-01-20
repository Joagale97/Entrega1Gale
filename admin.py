from django.contrib import admin
from .models import Celulares
# Register your models here.

class CelularesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celulares, CelularesAdmin)