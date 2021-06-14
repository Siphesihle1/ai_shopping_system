# Generated by Django 3.2 on 2021-05-24 05:52

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_auto_20210524_0722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorybase',
            options={},
        ),
        migrations.AddField(
            model_name='categorybase',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorybase',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorybase',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorybase',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorybase',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ecommerce.categorybase'),
        ),
        migrations.AlterUniqueTogether(
            name='categorybase',
            unique_together=set(),
        ),
    ]