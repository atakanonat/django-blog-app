from .views import index
from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('createArticle/', views.createArticle, name="createArticle"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('<int:id>/', views.details, name="details"),
    path('editArticle/<int:id>/', views.editArticle, name="editArticle"),
    path('deleteArticle/<int:id>/', views.deleteArticle, name="deleteArticle"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="comment"),
]
