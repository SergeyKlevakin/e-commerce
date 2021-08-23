from django.db import models
from applications.shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Номер заказа - {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.id}'
    
    def get_cost(self):
        return self.price * self.quantity
    
    
    
    
