from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural ='Категории'

    def __str__(self):
        return self.name
