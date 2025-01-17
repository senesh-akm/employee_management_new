# Generated by Django 5.1.4 on 2024-12-19 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryProcessing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deduction', models.TextField()),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('no_pay', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('days', models.PositiveIntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_processings', to='emp_management.employee')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to='emp_management.employee')),
                ('salary_processing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to='payroll_management.salaryprocessing')),
            ],
        ),
        migrations.CreateModel(
            name='TaxManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax', models.DecimalField(decimal_places=2, max_digits=3)),
                ('social_security', models.TextField()),
                ('other_taxes', models.DecimalField(decimal_places=2, max_digits=3)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxes', to='emp_management.employee')),
            ],
        ),
    ]
