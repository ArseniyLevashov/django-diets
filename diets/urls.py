from django.urls import path
from .views import list_diets, create_diet, create_result
from django.contrib import admin


urlpatterns = [
    path('', list_diets, name='list_diets'),
    path('new', create_diet, name='create_diet'),
    path('new_result/<int:id>', create_result, name='create_result'),
    path('admin/', admin.site.urls, name='admin'),
]