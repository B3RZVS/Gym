from django.urls import path
from .views import ValidarTokenView, AuthView

urlpatterns = [
    path('validar-token/', ValidarTokenView.as_view(), name='validar-token'),
    path('auth/', AuthView.as_view(), name='auth'),
]
