from django.urls import path
from .views import listar_frutas, vista_error

urlpatterns = [
    path('', listar_frutas, name='inicio'),
    path('error/', vista_error, name='error')
]