# Generated by Django 3.2 on 2021-04-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ld48', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default='no_name', max_length=30),
            preserve_default=False,
        ),
    ]
