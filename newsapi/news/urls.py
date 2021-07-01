from django.urls import path 
from news.views import JournalistListCreateAPIView, ArticleDetailAPIView, ArticleListCreateAPIView
# from news.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalists-list"),
    path("articles/", ArticleListCreateAPIView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail")
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail")
]