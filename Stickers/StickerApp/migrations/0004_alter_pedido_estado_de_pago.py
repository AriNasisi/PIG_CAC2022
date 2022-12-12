# Generated by Django 4.1.2 on 2022-12-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StickerApp', '0003_alter_item_pedido_cantidad_alter_item_pedido_tamaño_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado_de_pago',
            field=models.CharField(choices=[(1, 'Aceptado'), (2, 'Rechazado'), (3, 'Pendiente')], default='Pendiente', max_length=100),
        ),
    ]