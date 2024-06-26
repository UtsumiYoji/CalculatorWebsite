# Generated by Django 5.0 on 2023-12-29 19:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_about_remove_user_creater_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='units',
            field=models.CharField(choices=[('SI', 'SI'), ('US', 'US')], default='SI', max_length=2),
        ),
        migrations.AlterField(
            model_name='creater',
            name='about',
            field=models.TextField(help_text='About yourself and your background'),
        ),
        migrations.AlterField(
            model_name='creater',
            name='user_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
