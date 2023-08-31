from django.contrib import admin
from .models import Advert
# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'creation_date', 'last_updated', 'show_image']
    list_filter = ['auction']
    actions = ['make_auction_true', 'make_auction_false']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )
    
    
    @admin.action(description='Добавить возможность торга')
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)
    
    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)
    

admin.site.register(Advert, AdvertAdmin)
