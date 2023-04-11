from django.contrib import admin

from pages.models import Donation

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ('fullname','number','email',)
    list_per_page = 20
    
admin.site.register(Donation, DonationAdmin)