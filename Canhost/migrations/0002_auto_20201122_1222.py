# Generated by Django 3.1.3 on 2020-11-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Canhost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='father_mbl_no',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_mbl_no',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
