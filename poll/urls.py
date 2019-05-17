from django.urls import path
from . import views

urlpatterns = [
    path('register.html', views.register, name="register.html"),
    path('farm.html/', views.farm, name="farm.html"),
    path('farm.html/performance.html', views.performance, name="farm.html/performance.html")
]