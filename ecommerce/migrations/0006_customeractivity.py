# Generated by Django 3.2 on 2021-05-10 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20210501_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('A', 'add'), ('V', 'view')], default='A', max_length=1)),
                ('count', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
            ],
        ),
    ]