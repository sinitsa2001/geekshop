from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.TextField(verbose_name='описание',blank=True)
    # is_active = models.BooleanField(verbose_name='активна',default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural ='Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # is_active = models.BooleanField(verbose_name='категория активна', default=True)

    class Meta:
        verbose_name ='Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return f'{self.name} {self.category.name}'

    @staticmethod
    def get_items():
        return Product.objects.order_by('category', 'name')

        # return Product.objects.filter(is_active =True).order_by('category', 'name')
