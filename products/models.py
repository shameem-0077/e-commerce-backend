from django.db import models


class MainFeatured(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    feature_image = models.ImageField(upload_to="featured/images/")
    product_image = models.ImageField(upload_to="featured/product/")

    def __str__(self):
        return str(id)


class Category(models.Model):
    title = models.CharField(max_length=155)
    featured_image = models.ImageField(upload_to='category/featured/')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class ProductDetail(models.Model):
    material = models.CharField(max_length=155, null=True, blank=True)
    care = models.CharField(max_length=155, null=True, blank=True)
    made_in = models.CharField(max_length=155, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class AvailableSize(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    size = models.CharField(max_length=155)
    stock = models.CharField(max_length=155)
    is_available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class ProductImage(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class Product(models.Model):
    name = models.CharField(max_length=155)
    featured_image = models.ImageField(upload_to='products/featured/')
    price = models.CharField(max_length=155)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    description = models.TextField()
    detail = models.ForeignKey('products.ProductDetail', on_delete=models.CASCADE)
    stock = models.CharField(max_length=125)
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_trend = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
