# Generated by Django 2.2.10 on 2020-04-15 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0017_imageset_zip_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageset',
            name='path',
        ),
    ]