# Generated by Django 2.2.4 on 2019-09-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190917_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]