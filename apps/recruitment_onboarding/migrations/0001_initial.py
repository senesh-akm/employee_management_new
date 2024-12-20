# Generated by Django 5.1.4 on 2024-12-19 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('requirements', models.TextField()),
                ('work_type', models.CharField(choices=[('On-site', 'On-site'), ('Hybrid', 'Hybrid')], max_length=10)),
                ('employee_type', models.CharField(choices=[('Part-time', 'Part-time'), ('Full-time', 'Full-time')], max_length=10)),
                ('offers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CandidateScreening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.CharField(max_length=100)),
                ('members', models.TextField()),
                ('conduct_interviews', models.CharField(max_length=100)),
                ('job_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='recruitment_onboarding.jobposting')),
            ],
        ),
        migrations.CreateModel(
            name='OnboardingProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('offer_letter', models.TextField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onboardings', to='recruitment_onboarding.candidatescreening')),
            ],
        ),
    ]