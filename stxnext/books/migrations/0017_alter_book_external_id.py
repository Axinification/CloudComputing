# Generated by Django 4.0.4 on 2022-05-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_alter_book_authors_alter_book_published_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='external_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
