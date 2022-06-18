from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns=[
     path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editProfile,name='editprofile'),
    path('accounts/register/',views.register,name='register'),
    path('post/',views.post,name='post'),
    path('accounts/login/',views.loginpage,name='login'),
    path('neighbor/',views.neighbor,name='neighbor'),
    path('hood/',views.hood,name='hood'),
    path('accounts/logout/',views.logoutUser,name='logout'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]