# Generated by Django 5.1.3 on 2024-11-16 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_documento_person_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.person')),
            ],
        ),
    ]
