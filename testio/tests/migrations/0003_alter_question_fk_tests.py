# Generated by Django 3.2 on 2021-06-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_alter_question_fk_tests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='fk_tests',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.tests'),
        ),
    ]
