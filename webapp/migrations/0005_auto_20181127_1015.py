# Generated by Django 2.0.3 on 2018-11-27 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20181105_2111'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=4000),
        ),
    ]