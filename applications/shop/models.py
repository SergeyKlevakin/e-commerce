from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)
              
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    quantity = models.PositiveIntegerField(verbose_name='Колличество', null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='Есть в наличии?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])
