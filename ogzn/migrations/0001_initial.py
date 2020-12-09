# Generated by Django 3.1.3 on 2020-11-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('feedback_kad_num', models.CharField(max_length=20, verbose_name='Кадастровый номер')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph_path_id', models.CharField(max_length=20, verbose_name='Идентификаторы ответов (откуда куда) пр: q1,q2')),
                ('graph_q_id', models.CharField(max_length=3, verbose_name='Ответ yes или no')),
            ],
            options={
                'verbose_name': 'Граф соответствий',
                'verbose_name_plural': 'Граф соответствий',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_id', models.CharField(max_length=30, verbose_name='Идентификатор вопроса')),
                ('quest_text', models.TextField(verbose_name='Текст вопроса')),
                ('quest_comment', models.TextField(blank=True, verbose_name='Текст подсказки')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.CharField(max_length=10, verbose_name='Идентификатор ответа')),
                ('result_text', models.TextField(verbose_name='Рекомендация')),
            ],
            options={
                'verbose_name': 'Рекомендация',
                'verbose_name_plural': 'Рекомендации',
            },
        ),
    ]
