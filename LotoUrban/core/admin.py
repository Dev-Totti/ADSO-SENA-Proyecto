from django.contrib import admin

from .models import Cart, CartItem, Order, OrderItem, Category, Product, ProductImage, Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "city", "state", "postal_code", "phone"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ["category", "name", "price"]


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    list_display = ["user", "order_date", "total"]


class CartItemAdmin(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ["user", "updated_at"]


admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
