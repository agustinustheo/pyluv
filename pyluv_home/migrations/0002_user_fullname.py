# Generated by Django 2.1.5 on 2019-02-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyluv_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='', max_length=200),
        ),
    ]