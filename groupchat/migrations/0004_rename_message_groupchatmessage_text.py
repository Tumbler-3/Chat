# Generated by Django 4.1.4 on 2023-04-09 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0003_alter_groupchat_groupname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupchatmessage',
            old_name='message',
            new_name='text',
        ),
    ]