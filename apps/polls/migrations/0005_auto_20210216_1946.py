# Generated by Django 3.1.6 on 2021-02-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210216_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='plot',
            field=models.CharField(blank=True, max_length=512, verbose_name='Описание'),
        ),
    ]
