from django.urls import path
from . import views

urlpatterns = [
    path('<int:item_id>/', views.item, name='item'),
    path('create/', views.create, name='create')
]