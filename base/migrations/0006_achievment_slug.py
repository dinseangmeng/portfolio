# Generated by Django 4.0.2 on 2022-02-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_achievment_thumnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievment',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
