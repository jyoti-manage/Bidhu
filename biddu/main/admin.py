from django.contrib import admin
from . models import Hostel, UserInfo
from . models import Contact
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Contact)
admin.site.register(Hostel)