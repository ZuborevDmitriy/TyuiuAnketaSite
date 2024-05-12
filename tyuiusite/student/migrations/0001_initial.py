# Generated by Django 5.0.4 on 2024-05-12 12:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("creator", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentAnswer",
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
                    "answer_text",
                    models.CharField(max_length=200, null=True, verbose_name="Ответ"),
                ),
                ("date_answered", models.DateTimeField(auto_now=True)),
                ("right_answer", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="creator.questions",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="creator.anketa",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ студента",
                "verbose_name_plural": "Ответы студента",
            },
        ),
        migrations.CreateModel(
            name="StudentResult",
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
                    "student_name",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Имя пользователя"
                    ),
                ),
                ("result", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="creator.anketa",
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат теста",
                "verbose_name_plural": "Результаты тестов",
            },
        ),
    ]