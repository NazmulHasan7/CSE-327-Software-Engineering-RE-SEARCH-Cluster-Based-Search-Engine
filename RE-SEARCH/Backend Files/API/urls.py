from django.urls import path
from django.urls import include, path
from rest_framework import routers, views
from .views import ClusterAPI, URL_API, Register
from django.conf.urls import url
from rest_framework.authtoken import views as authviews


urlpatterns =[

    path('clusterapi/', ClusterAPI.as_view()),
    path('urlapi/', URL_API.as_view()),  
    #path('userapi/', UserAPI.as_view()),   
    path('registerapi/', Register.as_view()),

    #api authentication endpoint
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
]

