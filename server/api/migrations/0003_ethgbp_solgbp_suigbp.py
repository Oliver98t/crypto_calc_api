# Generated by Django 5.2.3 on 2025-07-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_conversionsymbol_btcgbp_conversionsymbol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EthGbp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.BigIntegerField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('volumefrom', models.FloatField(blank=True, null=True)),
                ('volumeto', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('conversionType', models.TextField(blank=True, db_column='conversionType', null=True)),
                ('conversionSymbol', models.TextField(blank=True, db_column='conversionSymbol', null=True)),
            ],
            options={
                'db_table': 'eth_gbp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SolGbp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.BigIntegerField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('volumefrom', models.FloatField(blank=True, null=True)),
                ('volumeto', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('conversionType', models.TextField(blank=True, db_column='conversionType', null=True)),
                ('conversionSymbol', models.TextField(blank=True, db_column='conversionSymbol', null=True)),
            ],
            options={
                'db_table': 'sol_gbp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SuiGbp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.BigIntegerField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('volumefrom', models.FloatField(blank=True, null=True)),
                ('volumeto', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('conversionType', models.TextField(blank=True, db_column='conversionType', null=True)),
                ('conversionSymbol', models.TextField(blank=True, db_column='conversionSymbol', null=True)),
            ],
            options={
                'db_table': 'sui_gbp',
                'managed': True,
            },
        ),
    ]
