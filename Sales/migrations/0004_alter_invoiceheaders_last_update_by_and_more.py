# Generated by Django 4.1.1 on 2022-10-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_invoicelines_item_orderlines_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceheaders',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoiceheaders',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoicelines',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoicelines',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderheaders',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderheaders',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderheaders',
            name='status',
            field=models.BooleanField(choices=[(1, 'Entered'), (2, 'Booked'), (3, 'Canceled'), (4, 'Complete')], max_length=1),
        ),
        migrations.AlterField(
            model_name='orderlines',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderlines',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderlines',
            name='status',
            field=models.BooleanField(choices=[(1, 'Entered'), (2, 'Booked'), (3, 'Canceled'), (4, 'Complete')], max_length=1),
        ),
        migrations.AlterField(
            model_name='orderlines',
            name='wasted_flag',
            field=models.BooleanField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pricelistheaders',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pricelistheaders',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pricelistlines',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pricelistlines',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='Last_update_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='created_by',
            field=models.IntegerField(),
        ),
    ]
