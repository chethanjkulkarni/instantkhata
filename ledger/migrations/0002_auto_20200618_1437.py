# Generated by Django 3.0.6 on 2020-06-18 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('retailers', '0001_initial'),
        ('ledger', '0001_initial'),
        ('salesman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailers.Retailer'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.Sale'),
        ),
        migrations.AddField(
            model_name='balancesheet',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesman.Salesman'),
        ),
        migrations.AddField(
            model_name='balancesheet',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.Invoice'),
        ),
    ]