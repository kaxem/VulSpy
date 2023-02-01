from django.urls import path

from vulspy import views 



urlpatterns = [
    path('api/scan',views.Scan.as_view() , name='scan'),
    path('api/result/<uuid:request_id>' ,views.Result.as_view(), name='result')
]
