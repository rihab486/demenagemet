from rest_framework import serializers
from .models import *
from rest_framework import serializers
from rest_framework.views import APIView

class ClientSerializer(serializers.ModelSerializer):
      class Meta:
        model = Client
        fields=[
          'id',
          'name',
          'lastname',
          'adresse',
          'numberphone',
        ]

class CategoriesSerializer(serializers.ModelSerializer) : 
     class Meta : 
        model = Categories
        fields = [
          'id',
          'nom',
         
     
        ] 
class ProduitSerializer(serializers.ModelSerializer):
     class Meta : 
        model = Produit
        fields = [
          'id',
          'nomp',
          'description',
          'image',
     
        ]