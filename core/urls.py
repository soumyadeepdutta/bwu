from django.urls import path
from .views import home, webhook

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
    path('', home, name='home'),
]
