# Generated by Django 4.0 on 2022-04-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
