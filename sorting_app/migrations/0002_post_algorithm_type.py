# Generated by Django 3.1.7 on 2021-03-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorting_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='algorithm_type',
            field=models.CharField(choices=[('BS', 'BUBBLE_SORT'), ('IS', 'INSERTIONS_SORT'), ('MS', 'MERGE_SORT')], default='BS', max_length=2),
        ),
    ]
