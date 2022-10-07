from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView, 
    PostDeleteView,
    LikeView,
    CreateCommentView
)
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('comment/<int:pk>/', CreateCommentView.as_view(), name='create_comment')
]