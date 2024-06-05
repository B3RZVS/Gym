from django.contrib import admin
from django.urls import path
from .views import PlanAbm

urlpatterns = [
    path('plan/', PlanAbm.as_view(), name='plan'),
]