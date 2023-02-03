# Generated by Django 4.1.5 on 2023-02-01 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thePerfectLandlord', '0003_savedproperties_rename_type_choice_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IncomeDetails',
            new_name='EmploymentDetail',
        ),
        migrations.RenameModel(
            old_name='IdentityDetails',
            new_name='IdentityDetail',
        ),
        migrations.RenameModel(
            old_name='ResidentialDetails',
            new_name='IncomeDetail',
        ),
        migrations.RenameModel(
            old_name='PropertyFeatures',
            new_name='PropertyFeature',
        ),
        migrations.RenameModel(
            old_name='PublicDetails',
            new_name='PublicDetail',
        ),
        migrations.RenameModel(
            old_name='EmploymentDetails',
            new_name='ResidentialDetail',
        ),
        migrations.RenameModel(
            old_name='SavedProperties',
            new_name='SavedProperty',
        ),
        migrations.AlterField(
            model_name='employmentdetail',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thePerfectLandlord.employmentitem'),
        ),
        migrations.AlterField(
            model_name='incomedetail',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thePerfectLandlord.incomeitem'),
        ),
        migrations.AlterField(
            model_name='residentialdetail',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thePerfectLandlord.residentialitem'),
        ),
    ]
