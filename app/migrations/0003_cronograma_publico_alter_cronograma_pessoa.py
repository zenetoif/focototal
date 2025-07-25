# Generated by Django 5.2.3 on 2025-07-22 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_materialapoio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronograma',
            name='publico',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cronograma',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pessoa'),
        ),
    ]
