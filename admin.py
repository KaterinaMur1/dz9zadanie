from django.contrib import admin
from .models import Advertisements
from django.utils.html import format_html

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_at', 'updated_at', 'thumbnail']

    list_filter = ['auction', 'created_at']

    actions = ['make_auction_as_false']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image', 'user'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.display(description='изображение')
    def thumbnail(self, adv):
        return format_html('<img src="{}" style="width: 130px; \
                           height: 100px"/>'.format(adv.image))


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)


admin.site.register(Advertisements, AdvertisementAdmin)
