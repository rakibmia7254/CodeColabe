from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('editor/<str:room_uuid>/', views.WorkspaceView.as_view(), name='editor')
]
