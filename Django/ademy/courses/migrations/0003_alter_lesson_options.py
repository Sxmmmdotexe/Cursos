# Generated by Django 5.1.4 on 2025-01-10 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order']},
        ),
    ]
