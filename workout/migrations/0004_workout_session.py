# Generated by Django 5.0.3 on 2024-04-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0003_alter_exercise_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="workout",
            name="session",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
