# Generated by Django 4.2.6 on 2023-11-10 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muslim_heroes', '0002_alter_category_options_alter_gender_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста'),
            preserve_default=False,
        ),
    ]
