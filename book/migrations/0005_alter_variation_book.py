# Generated by Django 4.0 on 2022-04-08 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
