# Generated by Django 3.2 on 2021-04-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type_account',
            field=models.BooleanField(default=False, verbose_name='Премиум'),
        ),
    ]