from django.contrib.auth.views import login, logout
from django.urls import path, reverse_lazy, include
from speedvisionx.views import HomePageView, MatrixDetailsView, ListVideosView, DetailsofVideoView

from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns =[
    path('login/', login, {'template_name':'login.html'}, name='login'),
    path('logout/', logout, {'next_page': reverse_lazy('login')}, name='logout'),
    path('home/', HomePageView.as_view(), name='home'),
    path('myvideos/', ListVideosView.as_view(), name="myvideos"),
    # path('videodetails/', DetailsofVideoView.as_view(), name="videodetails"),
    # path('videodetails', DetailsofVideoView.as_view(), name="videodetails"),
    # path(r'^(videodetails/<name=>[a-zA-Z0-9-]+)/$', DetailsofVideoView.as_view(), name = 'videodetails'),
    path('', include(router.urls)),
]

