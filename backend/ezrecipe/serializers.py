 # todo/serializers.py

from rest_framework import serializers
from ezrecipe.models import Ingredients, Recipes, RecipeIngredients, InputIngredients

#Ingredients Serializer
class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'

class RecipeIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredients
        fields = '__all__'

class IngredientsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputIngredients
        fields = '__all__'

    


