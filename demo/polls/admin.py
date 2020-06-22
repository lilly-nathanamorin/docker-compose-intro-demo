from django.contrib import admin

from demo.polls.models import Poll

admin.site.register(Poll, admin.ModelAdmin)
