from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('update/<int:todo_id>', views.update, name="update"),
    path('delete_all/', views.delete_all, name="delete_all"),
    path('complete_all/', views.complete_all, name="complete_all"),

]