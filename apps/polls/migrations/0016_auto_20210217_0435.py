# Generated by Django 3.1.6 on 2021-02-17 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_remove_poll_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('Ввод', 'Ввод'), ('Один', 'Один'), ('Много', 'Много')], max_length=32, verbose_name='Тип'),
        ),
    ]
