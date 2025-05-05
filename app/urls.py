from django.urls import path
from app.views import home_view, ramais_json

urlpatterns = [
    path('', home_view, name='home'),
    path('api/ramais/', ramais_json, name='ramais_json'),
]
