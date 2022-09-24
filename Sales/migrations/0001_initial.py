# Generated by Django 4.1.1 on 2022-09-22 07:13

import Sales.models
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Party', '0001_initial'),
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceHeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('invoice_number', models.IntegerField()),
                ('discount_value', models.IntegerField()),
                ('discount_type', models.CharField(choices=[(1, 'percentage'), (2, 'Amount')], max_length=1)),
                ('total_order', models.ImageField(upload_to='')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Party.parties')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderHeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('order_number', models.IntegerField()),
                ('status', models.CharField(choices=[(1, 'Entered'), (2, 'Booked'), (3, 'Canceled'), (4, 'Complete')], max_length=1)),
                ('discount_value', models.IntegerField()),
                ('discount_type', models.CharField(choices=[(1, 'percentage'), (2, 'Amount')], max_length=1)),
                ('total_order', models.ImageField(upload_to='')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Party.parties')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PriceListHeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('price_name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('room_number', models.IntegerField()),
                ('room_name', models.CharField(max_length=200)),
                ('room_size', models.IntegerField()),
                ('room_image', models.ImageField(upload_to=Sales.models.upload_image)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PriceListLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('value', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('public_price', models.IntegerField()),
                ('unit_selling_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('wasted_flag', models.CharField(max_length=1, null=True)),
                ('status', models.CharField(choices=[(1, 'Entered'), (2, 'Booked'), (3, 'Canceled'), (4, 'Complete')], max_length=1)),
                ('discount_value', models.IntegerField()),
                ('discount_type', models.CharField(choices=[(1, 'percentage'), (2, 'Amount')], max_length=1)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.orderheaders')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items')),
                ('price_list_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.pricelistlines')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='orderheaders',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.pricelistheaders'),
        ),
        migrations.AddField(
            model_name='orderheaders',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.rooms'),
        ),
        migrations.CreateModel(
            name='InvoiceLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField(verbose_name=django.contrib.auth.models.User)),
                ('public_price', models.IntegerField()),
                ('unit_selling_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('discount_value', models.IntegerField()),
                ('discount_type', models.CharField(choices=[(1, 'percentage'), (2, 'Amount')], max_length=1)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.invoiceheaders')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.items')),
                ('order_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.orderheaders')),
                ('price_list_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.pricelistlines')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.rooms')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='invoiceheaders',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.pricelistheaders'),
        ),
    ]