# Generated by Django 3.2 on 2021-06-14 12:11

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
            name='Test',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=20)),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
                ('fk_tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('explanation', models.TextField()),
                ('fk_tests', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=200)),
                ('fk_tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('right_answer', models.BooleanField(default=False)),
                ('answer', models.CharField(max_length=200)),
                ('fk_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
                ('fk_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
