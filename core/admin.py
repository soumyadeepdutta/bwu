from django.contrib import admin
from .models import DummyProperty, User, Response

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('country', 'address', 'price')
    list_filter = ('price',)

admin.site.register(DummyProperty, PropertyAdmin)

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'contact_no', 'address', 'city', 'pin_code', 'state', 'country', 'date_of_birth')
    list_display = ('email', 'city', 'state', 'country', 'is_agent')
    list_filter = ('city', 'state', 'country', 'is_agent')

admin.site.register(User, UserAdmin)


class ResponseAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'query', 'age', 'bhk', 'typ', 'price', 'budget', 'specifications', 'limitations')
    list_display = ('user', 'price', 'bhk', 'query', 'specifications')
    list_filter = ('query',)
admin.site.register(Response, ResponseAdmin)