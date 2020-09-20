from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.PostDraftListView, name='post_draft_list'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='add_comment_to_post'),
    path('comment/list/<int:pk>/', views.CommentListView.as_view(), name='comment_list'),
    path('comment/detail/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
]