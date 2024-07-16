from django.shortcuts import render
from rest_framework import generics
from .models import *
from demenagement.serializers import *
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from . views import *
from rest_framework import status
from rest_framework.response import Response

#list & create
class ClientListCreate(generics.ListCreateAPIView):
    queryset=Client.objects.filter(parent__isnull = True)
    serializer_class=ClientSerializer
# selected & update & delete 
class ClientupdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#list & create
class CategoriesListCreate(generics.ListCreateAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer
# selected & update & delete 
class CategoriesupdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer

#list & create
class ProduitListCreate(generics.ListCreateAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer
# selected & update & delete 
class ProduitupdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer