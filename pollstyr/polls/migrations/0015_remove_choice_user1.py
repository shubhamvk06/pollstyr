# Generated by Django 3.0.2 on 2020-01-31 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_choice_user1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user1',
        ),
    ]
