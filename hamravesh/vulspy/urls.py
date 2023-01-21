from django.urls import path

from vulspy import views 
from vulspy.views import Result




urlpatterns = [
    path('api/scan',views.Scan.as_view() , name='scan'),
    path('api/result/<uuid:id>' ,views.Result.as_view(), name='result')
]
