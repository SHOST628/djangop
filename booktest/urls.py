from django.urls import path
from booktest import views

# /index
urlpatterns = [
    # url route configuration
    # path : match absolute path   , re_path : re match
    path('index', views.index),  # mapping /index and index view
    path('index2', views.index2)
]