# Generated by Django 4.2.3 on 2023-07-17 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0009_maker_test3_pmodel_test3"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product2",
            name="nickname",
            field=models.CharField(default="超值二手機", max_length=15, verbose_name="摘要"),
        ),
        migrations.AlterField(
            model_name="product2",
            name="pmodel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mysite.pmodel",
                verbose_name="型號",
            ),
        ),
        migrations.AlterField(
            model_name="product2",
            name="price",
            field=models.PositiveBigIntegerField(default=0, verbose_name="價格"),
        ),
        migrations.AlterField(
            model_name="product2",
            name="year",
            field=models.PositiveIntegerField(default=2016, verbose_name="出場年份"),
        ),
    ]
