# Generated by Django 3.1.7 on 2021-03-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activism_finder', '0002_source_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='website',
            field=models.URLField(max_length=512),
        ),
    ]