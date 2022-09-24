# Generated by Django 4.1.1 on 2022-09-22 07:08

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchHeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('code', models.CharField(max_length=10)),
                ('active_flag', models.CharField(max_length=1)),
                ('max_production', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=400)),
                ('item_type', models.IntegerField(choices=[(1, 'Row Material'), (2, 'Finished Goods'), (3, 'Game')])),
                ('order_flag', models.CharField(max_length=1)),
                ('batch_flag', models.CharField(max_length=1)),
                ('complete_flag', models.CharField(max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subinventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionsTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('qty', models.IntegerField()),
                ('transaction_type', models.IntegerField(choices=[(1, 'Dept Transaction'), (2, 'Credit Transaction')])),
                ('batch_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.batchheaders')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items')),
                ('subinventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.subinventory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('qty', models.IntegerField()),
                ('transaction_type', models.IntegerField(choices=[(1, 'Dept Transaction'), (2, 'Credit Transaction')])),
                ('batch_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.batchheaders')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items')),
                ('subinventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.subinventory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BatchLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('qty', models.IntegerField()),
                ('batch_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.batchheaders')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='batchheaders',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items'),
        ),
    ]