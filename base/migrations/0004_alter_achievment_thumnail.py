# Generated by Django 4.0.2 on 2022-02-19 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_achievment_thumnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievment',
            name='thumnail',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', null=True, upload_to='static/img'),
        ),
    ]
