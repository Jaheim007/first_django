# Generated by Django 4.0.4 on 2022-04-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='indice',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
