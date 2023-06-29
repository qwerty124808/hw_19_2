from catalog.models import Product, Category
import json
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Подготовка списка        
        new_data = [
            {'name': 'Продукты', 'description': 'Тут хранятся продукты'},            
            {'name': 'Бытовая техника', 'description': 'Тут хранится бытовая техника'},
            {'name': 'Аксессуары', 'description': 'Тут хранятся аксуссуары'},        
            ]
        
        # Очистка предыдущей базы данных        
        self.stdout.write('Clearing the database...')
        Category.objects.all().delete()        
        self.stdout.write(self.style.SUCCESS('Database cleared successfully.'))
        # Заполнение базы данных новыми данными
        self.stdout.write('Filling the database...')        
        categories_for_adding = []
        for category_item in new_data:            
            categories_for_adding.append(Category(**category_item))
            
        Category.objects.bulk_create(categories_for_adding)        
        self.stdout.write(self.style.SUCCESS('Database filled successfully.'))


