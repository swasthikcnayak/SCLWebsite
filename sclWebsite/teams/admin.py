from django.contrib import admin

from .models import Teams


@admin.register(Teams)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cookies", "points")
    search_fields = ("name", "id")
    list_filter = ("name", "id","cookies","points")
    list_display_links = ("cookies", "id")

