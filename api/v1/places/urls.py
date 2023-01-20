from django.urls import path
from api.v1.places import views


urlpatterns = [
    path('', views.places),
    path('view/<int:pk>', views.place),
    path('protected/<int:pk>', views.protected),
    path('comments/lists/<int:pk>', views.comment),
    path('comments/create/<int:pk>/', views.comment_create),
    path('like/<int:pk>/', views.like),
]
