# Generated by Django 4.2.15 on 2024-08-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
