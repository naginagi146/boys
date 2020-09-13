from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view, name='post_list'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view, name='post_detail'),
    path('post/create', views.PostCreateView.as_view, name='post_create'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view, name='post_update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]