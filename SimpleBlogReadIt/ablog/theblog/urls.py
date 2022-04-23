from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]