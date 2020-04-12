from rest_framework import routers
from .api import IngredientsViewSet, RecipesViewset, RecipeIngredientsViewset

router = routers.DefaultRouter()
router.register('api/ingredients', IngredientsViewSet, 'ingredients')
router.register('api/recipes', RecipesViewset, 'recipes')
router.register('api/recipeingredients', RecipeIngredientsViewset, 'recipeingredients')

urlpatterns = router.urls