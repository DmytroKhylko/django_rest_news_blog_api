# Generated by Django 3.2.5 on 2021-07-15 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog_app', '0002_rename_coment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pubcic_id',
            new_name='public_id',
        ),
    ]
