# Generated by Django 3.1.7 on 2021-02-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
