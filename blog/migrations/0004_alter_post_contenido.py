# Generated by Django 4.0.6 on 2022-07-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(max_length=500),
        ),
    ]
