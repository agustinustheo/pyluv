# Generated by Django 2.1.5 on 2019-02-10 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyluv_api', '0005_auto_20190210_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiurl',
            name='api_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='apiurl',
            name='base_api',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyluv_api.API'),
        ),
    ]