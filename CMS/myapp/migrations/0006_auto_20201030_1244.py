# Generated by Django 3.1.2 on 2020-10-30 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201030_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='lawyer_id',
            field=models.ForeignKey(db_column='lawyer_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.lawyer'),
        ),
    ]
