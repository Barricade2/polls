# Generated by Django 3.1.6 on 2021-02-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='plot',
            field=models.TextField(blank=True, max_length=512, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=256, verbose_name='Перечни'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='plot',
            field=models.CharField(blank=True, max_length=512, verbose_name='Описание'),
        ),
    ]
