# Generated by Django 4.0.4 on 2022-05-16 02:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
