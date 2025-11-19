from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_toggle, name='like_toggle'),
    path('post/<int:post_id>/share/', views.share_post, name='share_post'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
