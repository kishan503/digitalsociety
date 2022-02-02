from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(user)
admin.site.register(watchman)
admin.site.register(chairman)
admin.site.register(s_member)
admin.site.register(visitor)
admin.site.register(comp_details)
admin.site.register(sugg_details)
admin.site.register(notice_details)
admin.site.register(event_details)