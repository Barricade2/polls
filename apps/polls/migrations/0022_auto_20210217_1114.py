# Generated by Django 3.1.6 on 2021-02-17 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20210217_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userchoiceid',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelTable(
            name='userchoiceid',
            table='myuser',
        ),
    ]
