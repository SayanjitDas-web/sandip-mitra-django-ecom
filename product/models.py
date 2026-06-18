from django.db import models

# Create your models here.
class Product(models.Model):
    product_title = models.CharField(max_length=150)
    product_details = models.TextField()
    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    product_image = models.ImageField(
        upload_to="products/"
    )
    
    def __str__(self):
        return self.product_title