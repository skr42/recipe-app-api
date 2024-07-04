from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe

from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """retrive recipe for authourized user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serialzer_class(self):
        if self.action=="list":
            return serializers.RecipeSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):# I found some accounts that methods were called for a single post request the ModelViewSet's create() and serializer's create().
        """Create a new recipe."""
        serializer.save(user=self.request.user)