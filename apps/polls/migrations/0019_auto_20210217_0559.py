# Generated by Django 3.1.6 on 2021-02-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20210217_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(blank=True, max_length=256, verbose_name='Перечни'),
        ),
    ]
