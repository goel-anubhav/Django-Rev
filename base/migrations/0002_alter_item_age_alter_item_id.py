# Generated by Django 5.0.6 on 2024-06-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
