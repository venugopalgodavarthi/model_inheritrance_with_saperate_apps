# Generated by Django 3.2.9 on 2021-12-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0003_auto_20211216_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]