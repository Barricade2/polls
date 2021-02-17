# Generated by Django 3.1.6 on 2021-02-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210216_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice',
        ),
        migrations.AddField(
            model_name='question',
            name='choice',
            field=models.ManyToManyField(blank=True, to='polls.Choice', verbose_name='Перечни'),
        ),
    ]
