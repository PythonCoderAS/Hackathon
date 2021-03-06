# Generated by Django 3.1.7 on 2021-03-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activism_finder', '0005_auto_20210320_1331'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='source',
            name='no_search_code',
        ),
        migrations.AddConstraint(
            model_name='keyword',
            constraint=models.UniqueConstraint(fields=('source', 'word'), name='No duplicate rows'),
        ),
        migrations.AddConstraint(
            model_name='source',
            constraint=models.CheckConstraint(check=models.Q(models.Q(_negated=True, code='search'), models.Q(_negated=True, code='list'), models.Q(_negated=True, code='tag'), models.Q(_negated=True, code='tags')), name='no_reserved_names_code'),
        ),
    ]
