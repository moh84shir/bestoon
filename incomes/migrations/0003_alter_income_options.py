# Generated by Django 3.2.11 on 2022-02-16 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0002_auto_20220212_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'دخل', 'verbose_name_plural': 'دخل ها'},
        ),
    ]