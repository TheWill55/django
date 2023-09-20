from django.urls import path
from .views import escolher_numero, pagina_inicial

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('escolher_numero/', escolher_numero, name='escolher_numero'),
]