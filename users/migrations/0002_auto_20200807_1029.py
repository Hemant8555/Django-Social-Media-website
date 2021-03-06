# Generated by Django 3.0.8 on 2020-08-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding_request',
            name='company',
            field=models.CharField(choices=[(1, 'Yes'), (2, 'No')], max_length=30),
        ),
        migrations.AlterField(
            model_name='funding_request',
            name='stage',
            field=models.CharField(choices=[(1, 'Idea'), (2, 'Concept'), (3, 'Established')], max_length=30),
        ),
    ]
