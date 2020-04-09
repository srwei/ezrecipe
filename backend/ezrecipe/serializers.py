 # todo/serializers.py

from rest_framework import serializers
from .models import ezrecipe

class ezrecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ezrecipe
        fields = ['ingredients']