# Generated by Django 4.2.2 on 2023-07-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.FloatField(verbose_name='номер версии'),
        ),
    ]
