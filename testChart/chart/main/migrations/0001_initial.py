# Generated by Django 4.2.2 on 2023-06-22 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fruit",
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
                ("f_name", models.CharField(max_length=10)),
                ("value", models.BigIntegerField()),
            ],
        ),
    ]
