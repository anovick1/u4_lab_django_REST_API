# Generated by Django 4.1 on 2022-08-31 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conference",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="team",
            name="conference",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="nba.conference",
            ),
            preserve_default=False,
        ),
    ]