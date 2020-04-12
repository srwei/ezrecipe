from ezrecipe.models import Ingredients, Recipes, RecipeIngredients
from rest_framework import viewsets, permissions
from .serializers import IngredientsSerializer, RecipesSerializer, RecipeIngredientsSerializer

#Ingredient Viewset
class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    permissions.classes = [
        permissions.AllowAny
    ]
    serializer_class = IngredientsSerializer

#Recipe Viewset
class RecipesViewset(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    permissions.classes = [
        permissions.AllowAny
    ]
    serializer_class = RecipesSerializer


#Recipe Ingredients Viewset
class RecipeIngredientsViewset(viewsets.ModelViewSet):
    queryset = RecipeIngredients.objects.all()
    permissions.classes = [
        permissions.AllowAny
    ]
    serializer_class = RecipeIngredientsSerializer
    