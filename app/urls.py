from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('post/',views.post,name='post'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
]