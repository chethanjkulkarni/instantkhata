# Generated by Django 3.0.6 on 2020-08-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0014_auto_20200815_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='order_id',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='payment_id',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='payment_signature',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='transaction_id',
            field=models.UUIDField(unique=True),
        ),
    ]