# Generated by Django 4.1.3 on 2022-11-13 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_remove_order_location_alter_order_pie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True, default=''),
        ),
    ]
