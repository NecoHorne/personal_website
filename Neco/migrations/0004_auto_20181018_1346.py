# Generated by Django 2.1.2 on 2018-10-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Neco', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='google_play',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='web_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
