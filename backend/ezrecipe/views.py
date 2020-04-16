from django.shortcuts import render
from rest_framework import viewsets          # add this
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import IngredientsInputSerializer
from .models import *
from .api import InputIngredientsViewset

class ReturnRecipeList(APIView):
    
    #def get_queryset(self):
    #    return InputIngredients.objects.all()
    
    def post(self, request, format=None):
        serializer = IngredientsInputSerializer(data=request.data) 
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    


'''
def recipe_list(request):
    if request.method == 'POST':
        serializer = IngredientsInputSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''