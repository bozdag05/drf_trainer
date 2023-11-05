# Generated by Django 4.2.6 on 2023-10-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muslim_heroes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'Пол', 'verbose_name_plural': 'Пол'},
        ),
        migrations.AddField(
            model_name='heroes',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]