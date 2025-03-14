# Generated by Django 4.2.20 on 2025-03-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubRepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'repo',
            },
        ),
    ]
