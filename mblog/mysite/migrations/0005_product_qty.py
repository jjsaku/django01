# Generated by Django 4.2.3 on 2023-07-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_alter_product_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="qty",
            field=models.IntegerField(default=0),
        ),
    ]
