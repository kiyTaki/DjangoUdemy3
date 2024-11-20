# Generated by Django 5.1.3 on 2024-11-20 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_venda_nfe_emitida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
        migrations.CreateModel(
            name='ItensDoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.venda')),
            ],
        ),
    ]
