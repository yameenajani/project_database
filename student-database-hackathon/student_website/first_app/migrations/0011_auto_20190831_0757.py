# Generated by Django 2.2.4 on 2019-08-31 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_auto_20190831_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='category',
            field=models.CharField(default='Mark Category', max_length=200),
        ),
    ]
