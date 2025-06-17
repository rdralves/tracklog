from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group_name in ['Motorista', 'Cliente']:
        Group.objects.get_or_create(name=group_name)


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
