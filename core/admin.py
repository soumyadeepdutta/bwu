from django.contrib import admin
from .models import FindHome, GeneralEnquiry, BecomeAnAgent, SellHome, FindAgent


admin.site.register(FindHome)
admin.site.register(SellHome)
admin.site.register(GeneralEnquiry)
admin.site.register(FindAgent)
admin.site.register(BecomeAnAgent)
