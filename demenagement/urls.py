from django.urls import path
from . views import *
urlpatterns = [
 path('client/', ClientListCreate.as_view(), name="list and create client")
 path('client/<int:pk>', ClienttupdateDelete.as_view(), name="list and update client"),
 path('Categories/', CategoriesListCreate.as_view(), name="list and create Categories"),
 path('Categories/<int:pk>', CategoriesupdateDelete.as_view(), name="list and update Categories"),
 path('produit', ProduitListCreate.as_view(), name="list and create produit"),
 path('produit/<int:pk>', ProduitupdateDelete.as_view(), name="list and update produit"),
 


]