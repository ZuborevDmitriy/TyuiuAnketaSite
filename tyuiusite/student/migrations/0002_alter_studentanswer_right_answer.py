# Generated by Django 5.0.4 on 2024-05-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentanswer",
            name="right_answer",
            field=models.BooleanField(default=False),
        ),
    ]