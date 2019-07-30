
from django.urls import path,re_path,include
from updates.api.views import (
                UpdateModelDetaiApiView,
                UpdateModelListApiView,
)

urlpatterns = [
    path('',UpdateModelListApiView.as_view()),
    re_path(r'^(?P<id>\d+)/$',UpdateModelDetaiApiView.as_view()),
    ]