# Generated by Django 3.2 on 2021-05-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_customeractivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeractivity',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]