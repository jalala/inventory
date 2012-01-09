from inventory.models import Section, Room, Item

__author__ = 'jalal'
from django.contrib import admin
class RoomLine(admin.TabularInline):
    model = Room
class ItemLine(admin.TabularInline):
    model = Item
class SectionAdmin(admin.ModelAdmin):
    inlines = [RoomLine,]
    fields = ['name']
    list_display = ('name',)
class RoomAdmin(admin.ModelAdmin):
    inlines = [ItemLine,]
    fields = ['name']
    list_display = ('name',)


        


admin.site.register(Section, SectionAdmin)
admin.site.register(Room, RoomAdmin)