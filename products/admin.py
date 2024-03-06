from django.contrib import admin
from products.models import Category, MainFeatured, ProductDetail, AvailableSize, ProductImage, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'featured_image',
        'is_deleted',
        
    )

admin.site.register(Category, CategoryAdmin)

admin.site.register(MainFeatured)

admin.site.register(ProductDetail)

admin.site.register(AvailableSize)

admin.site.register(ProductImage)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'is_available',
        'is_featured',
        'is_trend',
        'is_deleted',



        
    )

admin.site.register(Product, ProductAdmin)

