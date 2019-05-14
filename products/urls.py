from django.urls import path
from . import views

urlpatterns = [
    path('<int:item_id>/', views.item, name='item'),
    path('<int:item_id>/upvote', views.upvote, name='upvote'),
    path('create/', views.create, name='create'),
]