
from django.urls import path,re_path
from .views import  StatusAPIView,StatusDetailAPIView


urlpatterns = [
     path('',StatusAPIView.as_view() ),
     # path('create/',StatusCreateAPIView.as_view(),name='create'),
     # re_path(r'^(?P<id>\d+)/delete/$',StatusDeleteAPIView.as_view(),name='delete'),
     # re_path(r'^(?P<id>\d+)/update/$',StatusUpdateAPIView.as_view(),name='update'),
     re_path(r'^(?P<id>\d+)/$',StatusDetailAPIView.as_view(),name='detail'),
    # path('api/',include('updates.api.urls'))
   ]
