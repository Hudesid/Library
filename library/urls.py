from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('authors/', views.authors),
    path('book/authors/', views.authors),
    path('book/1', views.book_1),
    path('book/2', views.book_2),
    path('authors/author/1', views.author_1),
    path('authors/author/2', views.author_2),
    path('book/authors/author/1', views.author_1),
    path('book/authors/author/2', views.author_2),
]
