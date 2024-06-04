from django.urls import path
from .views import ValidarTokenView, AuthView, Register

urlpatterns = [
    path('validar-token/', ValidarTokenView.as_view(), name='validar-token'),
    path('auth/', AuthView.as_view(), name='auth'),
    path('register/', Register.as_view(), name='register'),
]
