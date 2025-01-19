from django.urls import path
from .views import EndpointList

urlpatterns = [
    path('',view=EndpointList.as_view(),name='endpoints')
]
