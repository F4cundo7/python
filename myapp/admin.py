from django.contrib import admin
from .models import Obra
# Register your models here.

class ObraAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

admin.site.register(Obra, ObraAdmin)