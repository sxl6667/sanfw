from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('test/', views.test),
    path('test_2/', views.test_json, name='hello'),

]