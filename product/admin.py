from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_title",
        "product_price",
    )
    search_fields=(
        "product_title",
    )
    