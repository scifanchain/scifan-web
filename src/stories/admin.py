from django.contrib import admin
from .models import Place, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status', 'maturity', 'content', 'version')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status', 'maturity', 'content', 'version')
