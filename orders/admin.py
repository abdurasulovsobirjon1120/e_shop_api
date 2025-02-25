from django.contrib import admin
from .models import Product, Order, OrderDetail
from e_shop_api.account.models import CustomUser

# class OrderDetailInline(admin.TabularInline):
#     model = OrderDetail
#     extra = 1

# class OrderAdmin(admin.ModelAdmin):
#     inlines = [OrderDetailInline]

admin.site.register(CustomUser)
admin.site.register(Order)
admin.site.register(OrderDetail)