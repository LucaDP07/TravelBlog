from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.ProfileList.as_view(), name='profile'),
    path('edit_profile/', views.edit_profile, name='profile_edit'),
    path(
      'profile/<str:username>',
      views.ProfileDetail.as_view(),
      name='profile_detail'),
    path('addtrip/', views.CreateTrip.as_view(), name='addtrip'),
    path('tripedit/<int:pk>', views.EditTrip.as_view(), name='tripedit'),
    path('tripdelete/<int:pk>', views.DeleteTrip.as_view(), name='tripdelete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    ]
