# Generated by Django 2.2.6 on 2019-10-12 09:02

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser_name', models.CharField(max_length=50)),
                ('browser_version', models.CharField(max_length=30)),
                ('device_ip', models.CharField(max_length=50)),
                ('device_uid', models.UUIDField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Login Credential',
                'verbose_name_plural': 'User Login Credentials',
            },
        ),
        migrations.AddIndex(
            model_name='logincredential',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['id', 'created_at', 'updated_at'], name='whats_app_l_id_1f3950_brin'),
        ),
    ]
