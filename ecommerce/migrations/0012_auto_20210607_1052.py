# Generated by Django 3.2.4 on 2021-06-07 08:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20210607_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasehistory',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='product',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.customer'),
        ),
    ]
