from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
# Register your models here.
class ProductGalleryInline(admin.TabularInline):
    model= ProductGallery
    extra= 1

class ProductAdmin(admin.ModelAdmin):
        list_display= ('product_name','price','stock','category','modified_date', 'is_available')
        list_editable= ('is_available',)
        list_filter= ('category', 'is_available')
        prepopulated_fields = {'slug': ('product_name',)}
        inlines =[ProductGalleryInline]
        list_per_page= 20

class VariationAdmin(admin.ModelAdmin):
        list_display= ('product','variation_category','variation_value','is_active')
        list_editable= ('is_active',)
        list_filter= ('product','variation_category','variation_value','is_active')
        list_per_page= 20

class ReviewRatingAdmin(admin.ModelAdmin):
        list_display= ('product','user','subject','rating')
        list_per_page= 20

class ProductGalleryAdmin(admin.ModelAdmin):
        list_display= ('product',)
        list_filter=('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery, ProductGalleryAdmin )
