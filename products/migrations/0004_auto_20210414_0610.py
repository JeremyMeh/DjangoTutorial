# Generated by Django 2.0.7 on 2021-04-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210414_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='this is cool!'),
        ),
    ]
