from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/scan',views.scan , name='scan'),
    path('api/result/{uuid}' , views.result , name='result')
]
