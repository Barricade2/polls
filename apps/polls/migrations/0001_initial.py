# Generated by Django 3.1.6 on 2021-02-16 16:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=64, null=True, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('plot', models.TextField(blank=True, verbose_name='Описание')),
                ('start_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Дата старта')),
                ('end_at', models.SlugField(blank=True, null=True, verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
                'db_table': 'poll',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(blank=True, verbose_name='Описание')),
                ('type', models.CharField(blank=True, choices=[('Ввод', 'Ввод'), ('Один', 'Один'), ('Много', 'Много')], max_length=32, verbose_name='Тип')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='ChoiceID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('choice', models.IntegerField(null=True)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='polls.question', verbose_name='Вопрос')),
            ],
        ),
    ]
