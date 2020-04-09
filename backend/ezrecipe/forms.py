from django import forms
from ezrecipe.models import ezrecipe

class EnterIngredientsForm(forms.form):
    ingredients = forms.CharField()
    