from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending","Pending"),
        ("processing","Processing"),
        ("shipped","Shipped"),
        ("delivered","Delivered"),
        ("cancelled","Cancelled"),
    ]
    user = models.ForeignKey(
        User,
        related_name="orders",
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id}"
    
    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    @property
    def subtotal(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f"{self.product.product_title} x {self.quantity}"