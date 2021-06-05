from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<category_id>', views.lists, name='lists'),
    path('tag/<tag_id>', views.lists, name='tag'),
    path('post/<id>', views.detail, name='detail'),
]
