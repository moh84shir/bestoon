from django.contrib import admin
from .models import SiteSetting


class SettingsAdmin(admin.ModelAdmin):
    class Meta:
        model = SiteSetting

    list_display = ("title", "github_addr")


# Register models
admin.site.register(SiteSetting, SettingsAdmin)
