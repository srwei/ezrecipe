from django.contrib import admin
from .models import ezrecipe

class ezrecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(ezrecipe, ezrecipeAdmin)
