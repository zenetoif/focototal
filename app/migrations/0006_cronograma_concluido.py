# Generated by Django 5.2 on 2025-07-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cronograma_descricao_recompensa_pontos_custo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronograma',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]
