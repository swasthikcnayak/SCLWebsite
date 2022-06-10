from django.contrib import admin

from .models import Profile, Request


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "role", "batch", "phone", "name", "college")
    search_fields = ("user__username", "role", "batch")
    list_filter = ("role", "batch")
    list_display_links = ("user", "id")


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("requested_by", "team", "mentor")
    search_fields = ("requested_by", "team", "mentor")
    list_filter = ("team", "mentor")
