# Generated by Django 3.2 on 2021-05-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_customeractivity_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]