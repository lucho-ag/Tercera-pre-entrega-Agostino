# Generated by Django 5.0.3 on 2024-04-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Restaurant", "0002_rename_capacidad_mesa_capacidad_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mesero",
            old_name="mesa_asignada",
            new_name="mesa",
        ),
    ]