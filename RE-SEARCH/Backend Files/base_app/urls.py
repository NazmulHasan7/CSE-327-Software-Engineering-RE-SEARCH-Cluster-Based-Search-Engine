from django.urls import path
from .views import (
    ClusterList, ClusterDetail, ClusterCreate, ClusterUpdate, 
    ClusterDelete, UrlList, UrlCreate, SearchView, search
)

urlpatterns = [
    path('', ClusterList.as_view(), name='clusters'),
    path('cluster-create/', ClusterCreate.as_view(), name='cluster-create'),
    path('<int:pk>/<str:slug>/', ClusterDetail.as_view(), name='cluster'),
    path('cluster-update/<int:pk>/<str:slug>/', ClusterUpdate.as_view(), name='cluster-update'),
    path('cluster-delete/<int:pk>/<str:slug>/', ClusterDelete.as_view(), name='cluster-delete'),
    #path('cluster-search/<int:pk>/<str:slug>/', SearchView.as_view(), name='cluster-search'),
    path('cluster-search/<int:pk>/<str:slug>/', search, name='cluster-search'),

    # for urls
    path('url-list/', UrlList.as_view(), name='url-list'),
    path('cluster-url/<int:pk>/', UrlCreate.as_view(), name='add-url'),
]