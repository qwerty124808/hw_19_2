# Generated by Django 4.2.2 on 2023-07-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]