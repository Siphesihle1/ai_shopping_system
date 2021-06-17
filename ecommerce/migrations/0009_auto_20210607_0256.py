# Generated by Django 3.2.4 on 2021-06-07 00:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20210606_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='address',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='date',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='order',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='state',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='total',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='user',
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.customer'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterModelTable(
            name='purchasehistory',
            table='ecommerce_purchasehistory',
        ),
    ]
