from django.urls import path
from . import views

urlpatterns = [

    path('', views.get_links),
    path('posts/', views.get_posts),
    path('profiles/', views.get_profiles),
    path('post/<pk>', views.single_post),
    path('profile/<pk>', views.single_profile),
]

