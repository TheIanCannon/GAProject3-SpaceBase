# Generated by Django 3.2.8 on 2021-11-05 18:13

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
            name='SpaceObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('so_type', models.CharField(max_length=50)),
                ('mass', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.spaceobject')),
            ],
        ),
    ]
