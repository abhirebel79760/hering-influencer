# Generated by Django 3.2.5 on 2021-07-22 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiretuber', '0002_rename_tuber_id_hiretuber_tubers_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiretuber',
            old_name='tubers_id',
            new_name='tuber_id',
        ),
    ]