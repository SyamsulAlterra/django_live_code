# Generated by Django 2.2.3 on 2019-07-25 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toko_online', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='deskripsi2',
        ),
    ]
