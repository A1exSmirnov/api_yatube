# Generated by Django 2.2.16 on 2022-03-28 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20220328_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='author',
        ),
    ]
