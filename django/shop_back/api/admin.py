from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "count", "is_active", "rating", "category", "likes"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "likes",]