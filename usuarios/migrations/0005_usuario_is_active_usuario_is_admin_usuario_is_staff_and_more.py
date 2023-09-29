# Generated by Django 4.2.5 on 2023-09-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0004_alter_usuario_idade"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]