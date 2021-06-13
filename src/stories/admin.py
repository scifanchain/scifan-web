from django.contrib import admin
from .models import Stage


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status', 'maturity', 'content', 'version')
