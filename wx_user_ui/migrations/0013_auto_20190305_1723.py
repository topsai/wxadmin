# Generated by Django 2.1.7 on 2019-03-05 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wx_user_ui', '0012_commodity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='mix_price',
            new_name='max_price',
        ),
    ]