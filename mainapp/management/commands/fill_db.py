import json
import os

from django.contrib.auth.models import User
from django.core.management import BaseCommand


from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH,file_name + '.json'), 'r') as infile:
        return json.load(infile)



class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category =ProductCategory.objects.create(**category)
            # new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']

            #получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)

            #заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

            #создаем суперпользователя при помощи менеджера модели
            super_user = User.objects.create_superuser('django', 'django@geekshop.local','geekbrains', age =33)

