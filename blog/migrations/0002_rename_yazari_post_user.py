# Generated by Django 4.0.5 on 2022-06-04 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='yazari',
            new_name='user',
        ),
    ]
