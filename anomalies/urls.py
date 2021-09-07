from django.urls import path, include
from anomalies import views

urlpatterns = [
    path('anomalies/', views.AccelerationLocationView.as_view()),
    path('threshold/', views.set_threshold),
]
