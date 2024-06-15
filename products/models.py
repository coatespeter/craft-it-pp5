from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=32, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    weight_unit = models.CharField(max_length=10, default='oz')  # New field for unit of measure
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
