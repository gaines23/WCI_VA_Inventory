# Generated by Django 3.2.4 on 2021-06-07 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': False, 'ordering': ('-dateadded',), 'verbose_name_plural': 'Employees'},
        ),
    ]