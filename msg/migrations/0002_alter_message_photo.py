# Generated by Django 4.1.4 on 2023-03-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
