# Generated by Django 3.0.5 on 2020-08-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamdb', '0005_auto_20200825_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
