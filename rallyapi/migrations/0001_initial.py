# Generated by Django 5.0.3 on 2024-05-01 00:46

import django.db.models.deletion
import location_field.models.plain
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rallyapi.community')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonorNeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rallyapi.donor')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rallyapi.need')),
            ],
        ),
        migrations.AddField(
            model_name='donor',
            name='needs',
            field=models.ManyToManyField(related_name='donors', through='rallyapi.DonorNeed', to='rallyapi.need'),
        ),
        migrations.AddField(
            model_name='donor',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rallyapi.type'),
        ),
    ]
