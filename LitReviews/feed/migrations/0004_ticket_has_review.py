# Generated by Django 3.2.9 on 2021-11-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20211117_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='has_review',
            field=models.BooleanField(default=False),
        ),
    ]
