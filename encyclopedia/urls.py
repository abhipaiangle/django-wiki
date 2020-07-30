from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create",views.create, name ="create"),
    path("wiki/search",views.search, name ="search"),
    path("wiki/<str:entry>", views.page, name="page"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/<str:title>/delete", views.delete, name="delete"),
    path("wiki/<str:title>/save", views.save, name="save"),
    path("wiki", views.random_page, name="random_page"),
 
]
