from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipes/', views.recipes, name='recipe'),
    path('register/', views.register, name='register'),
]
