# Generated by Django 2.2.12 on 2021-11-11 06:24

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 11, 11, 6, 24, 56, 577209, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 11, 11, 6, 24, 56, 577774, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=True, related_name='comments', to='blog.Post')),
            ],
        ),
    ]
