from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
)  # new

urlpatterns = [
    path("path/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("path/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),  # new
    path("", BlogListView.as_view(), name="home"),
]