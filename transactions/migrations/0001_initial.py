# Generated by Django 4.1.5 on 2023-01-29 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stores", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.PositiveIntegerField()),
                ("date", models.DateField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=8)),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.DateTimeField()),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="stores.store",
                    ),
                ),
            ],
        ),
    ]
