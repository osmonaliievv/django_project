# Generated by Django 5.1.4 on 2025-01-11 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_books_options_alter_books_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(verbose_name='Оставьте комментарий')),
                ('stars', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], default='⭐⭐⭐⭐⭐', max_length=10)),
                ('review_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.books')),
            ],
        ),
    ]
