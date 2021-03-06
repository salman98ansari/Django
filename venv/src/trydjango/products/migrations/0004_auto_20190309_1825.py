# Generated by Django 2.1.7 on 2019-03-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190309_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100000),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
