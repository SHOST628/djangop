from django.urls import path,re_path
from booktest import views

# /index
urlpatterns = [
    # url route configuration
    # path : match absolute path   , re_path : re match
    path('index', views.index),  # mapping /index and index view
    path('index2', views.index2),
    path('books', views.show_books),  # show book data
    re_path('^books/(\d+)$', views.detail),
]