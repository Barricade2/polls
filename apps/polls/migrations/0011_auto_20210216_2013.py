# Generated by Django 3.1.6 on 2021-02-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210216_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]
