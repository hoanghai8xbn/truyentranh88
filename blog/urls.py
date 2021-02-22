from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('detail/', detail2, name="detail2"),
    path('detail/<int:pk>/', detail3, name="detail3"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="update"),
    path('post/new/', PostCreateView.as_view(), name="new"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="delete"),
    path('<int:pk>/', viewlist, name="delete"),
]