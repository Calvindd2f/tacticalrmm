# Generated by Django 3.1.7 on 2021-04-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210329_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalKVStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('value', models.TextField()),
            ],
        ),
    ]