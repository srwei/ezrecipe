from django.contrib import admin
from .models import ezrecipe

class ezrecipeAdmin(admin.ModelAdmin):
    list_display = ['ingredients']

admin.site.register(ezrecipe, ezrecipeAdmin)


