from ezrecipe.models import Ingredients, Recipes, RecipeIngredients, InputIngredients
from rest_framework import viewsets, permissions, status
from .serializers import IngredientsSerializer, RecipesSerializer, RecipeIngredientsSerializer, IngredientsInputSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

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

        r = Recipes.objects.raw(query)
        print(r)
        for i in r:
            print(i.recipe_id, i.recipe_name)
            print("www.allrecipes.com/recipe/{}".format(i.recipe_id))

        #print(x)

        '''
        ingredient_list = str(ingredient_list).strip('[]')
        x = 
        '''
        return Response()
