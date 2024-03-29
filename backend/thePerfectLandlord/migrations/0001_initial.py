# Generated by Django 4.2.dev20230112122347 on 2023-01-27 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=100)),
                ('weekly_price', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=30)),
                ('landlord_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thePerfectLandlord.user')),
                ('property_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thePerfectLandlord.type')),
            ],
        ),
    ]
