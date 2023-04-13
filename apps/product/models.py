from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from datetime import datetime

User = get_user_model()

class Product(models.Model):
    slug = models.SlugField(primary_key=True , max_length=150, blank=True)
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='image')
    category = models.ForeignKey('category.Category',on_delete=models.SET_NULL,null=True,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)+datetime.now().strftime('_%d_%M_%H_%S') 
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусель'

    def __str__(self):
        return f'image to{self.product.title}'