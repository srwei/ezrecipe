from rest_framework import routers
from .api import IngredientsViewSet, RecipesViewset, RecipeIngredientsViewset, InputIngredientsViewset

router = routers.DefaultRouter()
router.register('api/ingredients', IngredientsViewSet, 'ingredients')
router.register('api/recipes', RecipesViewset, 'recipes')
router.register('api/recipeingredients', RecipeIngredientsViewset, 'recipeingredients')
router.register('api/inputingredients', InputIngredientsViewset, 'inputingredients')

urlpatterns = router.urls