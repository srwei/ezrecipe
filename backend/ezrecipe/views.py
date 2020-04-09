from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import ezrecipeSerializer      # add this
from .models import ezrecipe                     # add this
from .forms import EnterIngredientsForm

class ezrecipeView(viewsets.ModelViewSet):       # add this
    serializer_class = ezrecipeSerializer          # add this
    queryset = ezrecipe.objects.all()              # add this


'''
def search(request):
    if request.GET:
'''