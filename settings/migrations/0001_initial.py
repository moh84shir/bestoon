# Generated by Django 3.2.11 on 2022-02-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان سایت')),
                ('about', models.TextField(verbose_name='درباره ی سایت')),
                ('github_addr', models.CharField(max_length=200, verbose_name='آدرس گیت هاب')),
            ],
        ),
    ]
