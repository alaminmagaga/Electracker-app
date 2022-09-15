from django.urls import path, include
from . import views
from .views import index


urlpatterns = [
    path('', index.as_view(), name="home"),
    path('result/', views.result, name="result"),
    path('satisfaction/', views.satisfaction, name="satisfaction")
]
