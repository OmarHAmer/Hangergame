# Generated by Django 4.1.1 on 2022-09-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_navbar_child_list_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='app_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
