# Generated by Django 2.2.5 on 2019-10-14 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='reportdoner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.TextField(blank=True, max_length=10)),
                ('mobile', models.TextField(blank=True, max_length=10)),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('reportinfo', models.TextField(blank=True, max_length=400)),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]