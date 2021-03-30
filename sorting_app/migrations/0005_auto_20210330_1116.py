# Generated by Django 3.1.7 on 2021-03-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorting_app', '0004_auto_20210329_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='algorithm_type',
            field=models.CharField(choices=[('BS', 'BUBBLE_SORT'), ('IS', 'INSERTIONS_SORT'), ('MS', 'MERGE_SORT'), ('SS', 'SELECTION_SORT')], default='BS', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='sorted_list',
            field=models.TextField(default=[]),
        ),
    ]
