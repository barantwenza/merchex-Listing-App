from django.contrib import admin

from listings.models import Band
from listings.models import TitlesBand


class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed', 'genre')

class TitlesBandAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(TitlesBand, TitlesBandAdmin)
# Register your models here.
