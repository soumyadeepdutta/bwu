from django.urls import path
from .views import home, webhook, save

urlpatterns = [
    path('save', save, name='save'),
    path('webhook/', webhook, name='webhook'),
    path('', home, name='home'),
]
