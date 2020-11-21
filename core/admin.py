from django.contrib import admin
from .models import DummyProperty, User

admin.site.register(DummyProperty)
admin.site.register(User)