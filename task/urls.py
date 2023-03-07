"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('display_product/',views.display_product,name="display_product"),
    path('add_product/',views.add_product,name="add_product"),
    path('edit_product/<str:pk>',views.edit_product,name="edit_product"),
    path('delete_product/<str:pk>',views.delete_product,name="delete_product"),


    path('display_location/',views.display_location,name="display_location"),
    path('add_location/',views.add_location,name="add_location"),
    path('edit_location/<str:pk>',views.edit_location,name="edit_location"),
    path('delete_location/<str:pk>',views.delete_location,name="delete_location"),

    path('product_movement/',views.product_movement,name="product_movement"),
    path('add_product_movement/',views.add_product_movement,name="add_product_movement"),
    path('edit_product_movement/<int:pk>',views.edit_product_movement,name="edit_product_movement"),
    path('product_balance/',views.product_balance,name="product_balance"),

    
]
