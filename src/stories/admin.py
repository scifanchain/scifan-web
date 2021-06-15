from django.contrib import admin
from .models import Stage


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_time')
    fields = ('title', 'status', 'maturity', 'content', 'version', 'authors')
