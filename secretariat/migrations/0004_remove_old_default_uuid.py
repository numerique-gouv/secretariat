# Generated by Django 4.2.5 on 2023-10-19 09:25
# @see https://docs.djangoproject.com/en/4.2/topics/migrations/#data-migrations

from django.db import migrations


def remove_old_default_uuid(apps, _):
    # We can't import the User model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    User = apps.get_model("secretariat", "User")
    for user in User.objects.filter(outline_uuid="not a valid uuid"):
        print(f"remove outline uuid of {user.email}")
        user.outline_uuid = None
        user.save()


def migrating_backwards(_, __):
    print("Nothing to do")


class Migration(migrations.Migration):
    dependencies = [
        ("secretariat", "0003_alter_user_outline_uuid"),
    ]

    operations = [migrations.RunPython(remove_old_default_uuid, migrating_backwards)]