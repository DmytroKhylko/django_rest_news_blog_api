# Generated by Django 3.2.5 on 2021-07-15 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("news_blog_app", "0003_auto_20210715_1449"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 7, 15, 14, 51, 31, 99053, tzinfo=utc),
                verbose_name="date joined",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 7, 15, 14, 51, 31, 99069, tzinfo=utc),
                verbose_name="last login",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="upvote",
            unique_together={("post", "author")},
        ),
    ]
