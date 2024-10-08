from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autores/', views.AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('livros/', views.LivroList.as_view(), name='livro-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),
]
