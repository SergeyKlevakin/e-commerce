from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at')
    list_filter = ('available', 'created_at', 'category')
    search_fields = ('name', 'price', 'description')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}



