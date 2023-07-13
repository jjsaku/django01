# Generated by Django 4.2.3 on 2023-07-13 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0007_maker_test_pmodel_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="Maker_test2",
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
                ("country", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="PModel_test2",
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
                ("name", models.CharField(max_length=20)),
                ("url", models.URLField()),
                (
                    "maker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mysite.maker_test2",
                    ),
                ),
            ],
        ),
    ]
