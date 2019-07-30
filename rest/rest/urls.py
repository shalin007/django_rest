"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from updates.views import  JsnCBV,SearializedDetailView,SearializedListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',JsnCBV.as_view(),name='jsonview'),

    # path('api/auth/jwt/', obtain_jwt_token),
    # path('api/auth/jwt/refresh/', refresh_jwt_token),
    path('api/auth/',include('accounts.api.urls')),

    path('api/',include('updates.api.urls')),
    path('api/status/',include('status.api.urls'))
    # path('serlist/', SearializedDetailView.as_view()),
    # path('serdetail/', SearializedListView.as_view())
]
