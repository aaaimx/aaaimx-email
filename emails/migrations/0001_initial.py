# Generated by Django 3.0.2 on 2020-01-20 05:20

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('name', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='templates')),
                ('keys', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=200, null=True), default=list, size=20)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, default='', max_length=200)),
                ('message', models.CharField(blank=True, default='', max_length=200)),
                ('sent', models.IntegerField(blank=True, default=0)),
                ('context', django.contrib.postgres.fields.jsonb.JSONField()),
                ('recipients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=200, null=True), default=list, size=20)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emails.Template')),
            ],
        ),
    ]
