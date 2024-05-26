# Generated by Django 5.0.4 on 2024-05-26 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Anketa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "anketa_title",
                    models.CharField(max_length=200, verbose_name="Заголовок"),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "anketa_author",
                    models.CharField(max_length=200, verbose_name="Автор теста"),
                ),
            ],
            options={
                "verbose_name": "Анкета",
                "verbose_name_plural": "Анкеты",
            },
        ),
        migrations.CreateModel(
            name="Questions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=200, verbose_name="Вопрос")),
                (
                    "ank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="creator.anketa"
                    ),
                ),
            ],
            options={
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
            },
        ),
        migrations.CreateModel(
            name="Answers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.CharField(max_length=200, verbose_name="Ответ")),
                (
                    "ank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="creator.anketa"
                    ),
                ),
                (
                    "quest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="creator.questions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ",
                "verbose_name_plural": "Ответы",
            },
        ),
    ]
