from django.db import models

class ezrecipe(models.Model):
    ingredients = models.TextField()

    def _str_(self):
        return self.ingredients
