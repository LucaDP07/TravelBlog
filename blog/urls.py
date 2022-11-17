from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('mytrips/', views.MyTripList.as_view(), name='mytrips'),
    path('tripcreate/', views.TripCreate.as_view(), name='tripcreate'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
