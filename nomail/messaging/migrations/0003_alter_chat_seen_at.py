# Generated by Django 5.0.6 on 2024-10-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_alter_chat_user_alter_deletedmessages_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='seen_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
