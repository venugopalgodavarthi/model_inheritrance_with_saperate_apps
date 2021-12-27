# Generated by Django 3.2.9 on 2021-12-27 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('adhaar', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pdesc', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transcation',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('totalprice', models.FloatField()),
                ('date', models.DateField()),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo7.customer')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo7.product')),
            ],
        ),
    ]
