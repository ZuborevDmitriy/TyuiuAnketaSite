# Generated by Django 5.0.4 on 2024-05-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentanswer",
            name="answer_text",
            field=models.CharField(max_length=200, verbose_name="Ответ"),
        ),
    ]
