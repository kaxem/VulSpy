from django.urls import path

from . import views

urlpatterns = [
    path('api/scan',views.Scan.as_view() , name='scan'),
]
