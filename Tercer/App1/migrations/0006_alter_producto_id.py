# Generated by Django 4.2 on 2023-05-17 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]