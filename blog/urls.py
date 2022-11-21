from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addtrip/', views.CreateTrip.as_view(), name='addtrip'),
    path('tripedit/<int:pk>', views.EditTrip.as_view(), name='tripedit'),
    path('tripdelete/<int:pk>', views.DeleteTrip.as_view(), name='tripdelete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
