from ezrecipe.models import Ingredients, Recipes, RecipeIngredients, InputIngredients
from rest_framework import viewsets, permissions, status
from .serializers import IngredientsSerializer, RecipesSerializer, RecipeIngredientsSerializer, IngredientsInputSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
import re
import requests

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

class InputIngredientsViewset(viewsets.ModelViewSet):

    queryset = InputIngredients.objects.all()
    permissions.classes = [
        permissions.AllowAny
    ]
    serializer_class = IngredientsInputSerializer

    def create(self, request):
        print('#########creating')
        q = request.data
        ingredient_list = q["ingredients_str"]
        ingredient_list = str(ingredient_list).strip('[]')
        print(ingredient_list)
        if not ingredient_list:
            content = {"no ingredients found": "no recipes found"}
            return Response(content)

        #x = Recipes.objects.raw("select * f")
        #for o in x:
        #    print(o.recipe_id)

        query = """
                select * from recipes r 
                join ( 
                    select recipe_id, count(*) as available_ingredients 
                    from recipe_ingredients  
                    where ingredient_name in ({}) 
                    group by recipe_id 
                    ) s on r.recipe_id = s.recipe_id  
                where s.available_ingredients >= r.num_ingredients
            """.format(ingredient_list)

        content = []
        r = Recipes.objects.raw(query)
        print(r)
        for i in r:
            print(i.recipe_id, i.recipe_name)
            print("www.allrecipes.com/recipe/{}".format(i.recipe_id))
            recipes = {}
            recipes["recipe_name"] = i.recipe_name
            recipes["recipe_url"] = "http://www.allrecipes.com/recipe/{}".format(i.recipe_id)
            response = requests.get(recipes["recipe_url"])
            soup = BeautifulSoup(response.text, "html.parser")
            x = soup.find_all("img", class_= "rec-photo")
            if x:
                picture_url = re.findall(r'src="(.*?)"', str(x))[0]
                recipes["picture_url"] = picture_url
            if not x:
                recipes["picture_url"] = "no picture"

            content.append(recipes)

        #Getting Recipes that are almost available (missing one ingredient)
        almost_query = """
                select * from recipes r 
                join ( 
                    select recipe_id, count(*) as available_ingredients 
                    from recipe_ingredients  
                    where ingredient_name in ({}) 
                    group by recipe_id 
                    ) s on r.recipe_id = s.recipe_id  
                where s.available_ingredients = r.num_ingredients - 1
            """.format(ingredient_list)
        
        almost_content = []
        aq = Recipes.objects.raw(almost_query)
        print(aq)
        for a in aq:
            print(a.recipe_id, a.recipe_name)
            print("www.allrecipes.com/recipe/{}".format(a.recipe_id))
            almost_recipes = {}
            almost_recipes["recipe_name"] = a.recipe_name
            almost_recipes["recipe_url"] = "http://www.allrecipes.com/recipe/{}".format(a.recipe_id)
            response = requests.get(almost_recipes["recipe_url"])
            soup = BeautifulSoup(response.text, "html.parser")
            x = soup.find_all("img", class_= "rec-photo")
            if x:
                picture_url = re.findall(r'src="(.*?)"', str(x))[0]
                almost_recipes["picture_url"] = picture_url
            if not x:
                almost_recipes["picture_url"] = "no picture"
                
            almost_content.append(almost_recipes)

        json = {"recipes": content, "almost_recipes": almost_content}



        #print(x)

        '''
        ingredient_list = str(ingredient_list).strip('[]')
        x = 
        '''
        return Response(json)
