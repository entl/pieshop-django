# Generated by Django 4.1.3 on 2022-11-11 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_pie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pie',
            name='image',
            field=models.ImageField(default='../media/images/base-pie.png', upload_to='images/'),
        ),
    ]
