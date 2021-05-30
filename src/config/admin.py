from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth import models
from .models import Link, Sidebar

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change) -> None:
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(Sidebar)
class SidebarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change) -> None:
        obj.owner = request.user
        return super(SidebarAdmin, self).save_model(request, obj, form, change) 