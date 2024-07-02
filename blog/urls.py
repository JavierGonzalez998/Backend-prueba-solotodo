from .views import PostViewSet, PostDetail
from django.urls import path
urlpatterns = [
    path("posts/", PostViewSet.as_view()),
    path("posts/<int:id>", PostDetail.as_view())    
]
