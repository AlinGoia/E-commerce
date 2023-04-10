from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = 'E-commerce Site'
admin.site.site_title = 'XYZ Shopping'
admin.site.index_title = 'Manage XYZ Shopping'

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')
    
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discounted_price','category','description')
    search_fields = ('title','category')
    actions = ('change_category_to_default',)
    fields = ('title','category','description')
    list_editable = ('price','discounted_price')

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)