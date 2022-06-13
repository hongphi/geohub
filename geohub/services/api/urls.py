from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServicesView.as_view(), name="api-services"),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service-details'),
]
