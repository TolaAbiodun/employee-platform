# Generated by Django 3.1.7 on 2022-05-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
