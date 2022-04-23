from django.urls import path
from .views import *

urlpatterns = [
    path('', StoryHome.as_view(), name='home'),
    path('about-us/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('post/<int:pk>/', ShowPost.as_view(), name='post'),
    path('news_home/', news_home, name='news_home'),
    path('send/', send_mail),
    path('post/<int:pk>/update', NewsUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', NewsDeleteView.as_view(), name='delete_post'),
    path('category/<int:cat_id>/', StoryCategory.as_view(), name='category'),
    path("register", register_request, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', logout_user, name='logout'),
]