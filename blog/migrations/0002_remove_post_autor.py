# Generated by Django 4.0.6 on 2022-07-12 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
    ]
