from django.urls import path
from . import views

urlpatterns = [

    path('', views.get_links),
    path('posts/', views.get_posts),
    path('post/<pk>', views.single_post),
]

