from django.urls import path
from .import views

urlpatterns = [
    path('', views.bookList, name="books"),
    path('book/<str:pk>/', views.bookId, name="book"),
    path('create', views.bookCreate, name="create"),
    path('update/<str:pk>/', views.bookUpdate, name="update"),
    path('delete/<str:pk>/', views.bookDelete, name="delete"),
]