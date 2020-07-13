# Generated by Django 3.0.8 on 2020-07-08 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picture_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictureblog',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pictureblog',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
    ]
