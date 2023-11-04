from django.urls import path
from . import views
# car/urls.py
urlpatterns = [
    path('cars', views.ListCreateCarView.as_view()),
    path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]
