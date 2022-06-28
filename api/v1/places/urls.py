from django.urls import path
from api.v1.places import views


urlpatterns = [
    path('', views.places),
    path('view/<int:pk>', views.places),
    path('protected/<int:pk>', views.protected),
]
