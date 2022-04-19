# Generated by Django 4.0.4 on 2022-04-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('ingerdients', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('vegetrian', models.BooleanField(default=False)),
            ],
        ),
    ]
