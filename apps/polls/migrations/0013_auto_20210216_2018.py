# Generated by Django 3.1.6 on 2021-02-16 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20210216_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.poll', verbose_name='Опрос'),
        ),
    ]