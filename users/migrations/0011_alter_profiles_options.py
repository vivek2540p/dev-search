# Generated by Django 5.1.4 on 2025-01-17 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiles',
            options={'ordering': ['-created']},
        ),
    ]
