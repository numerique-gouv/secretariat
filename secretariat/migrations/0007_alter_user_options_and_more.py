# Generated by Django 4.2.7 on 2023-12-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("secretariat", "0006_membership_end_date_membership_start_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "estimé·e collègue",
                "verbose_name_plural": "estimé·e·s collègues",
            },
        ),
        migrations.AlterField(
            model_name="organisation",
            name="outline_group_uuid",
            field=models.UUIDField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="outline_uuid",
            field=models.UUIDField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AddConstraint(
            model_name="membership",
            constraint=models.CheckConstraint(
                check=models.Q(("end_date__gt", models.F("start_date"))),
                name="start_must_be_before_end",
            ),
        ),
    ]
