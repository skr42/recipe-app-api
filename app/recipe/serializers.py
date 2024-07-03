"""serializers for Recipe apis"""

from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    '''RecipeSerializer for recipe'''
    class Meta:
        model=Recipe
        fields=['id','title','time_minutes','price','link']
        read_only_fields=['id']

class RecipeDetailSerializer(RecipeSerializer):
    '''RecipeDetailSerializer for Recipe Detial view'''
    class Meta(RecipeSerializer.Meta):
        fields=RecipeSerializer.Meta.fields + ["description"]