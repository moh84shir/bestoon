# Generated by Django 3.2.11 on 2022-02-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'خبر', 'verbose_name_plural': 'اخبار'},
        ),
        migrations.AddField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرغعال'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=250, verbose_name='عنوان'),
        ),
    ]
