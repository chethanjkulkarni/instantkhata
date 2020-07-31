# Generated by Django 3.0.6 on 2020-07-31 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0008_product_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('provider', models.ImageField(upload_to='uploads/providers/')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=512)),
                ('account_id', models.CharField(max_length=512)),
                ('is_bank', models.BooleanField(default=False)),
                ('ifsc', models.CharField(blank=True, max_length=512, null=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributors.Distributor')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributors.PaymentMode')),
            ],
        ),
    ]