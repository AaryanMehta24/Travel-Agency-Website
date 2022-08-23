from django.contrib import admin
from .models import * 
from django.contrib.auth.models import User, auth
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(DestinationDetails)
admin.site.register(TravelDetails)
admin.site.register(TravellerDetails)
admin.site.register(PaymentDetails)
# admin.site.register(auth.UserAdmin)