from django.urls import path
from core.views import index, piloto

urlpatterns = [
   path('', index, name='index'),
   path('piloto/', piloto, name='piloto'),
]

