# Generated by Django 5.1.4 on 2025-01-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_librusec', '0002_remove_librusecparser_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='librusecparser',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
