# Generated by Django 5.1.5 on 2025-01-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='experience',
            field=models.PositiveIntegerField(),
        ),
    ]
