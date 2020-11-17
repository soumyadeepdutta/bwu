from django.urls import path
from .views import home, webhook
from django.conf.urls.static import settings
from django.conf.urls.static import static

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
    path('', home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)