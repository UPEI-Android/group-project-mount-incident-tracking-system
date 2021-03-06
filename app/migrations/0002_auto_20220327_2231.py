# Generated by Django 3.2.12 on 2022-03-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='action_treatment_prescribed',
            field=models.TextField(blank=True, default='', verbose_name='Action or Treatment Prescribed'),
        ),
        migrations.AddField(
            model_name='report',
            name='cause_of_incident',
            field=models.TextField(blank=True, default='', verbose_name='Cause of Incident'),
        ),
        migrations.AddField(
            model_name='report',
            name='completing_account',
            field=models.TextField(blank=True, default='', verbose_name='Reviewing Account Username'),
        ),
        migrations.AddField(
            model_name='report',
            name='physician_review_account',
            field=models.TextField(blank=True, default='', verbose_name='Physician Review Account Username'),
        ),
        migrations.AddField(
            model_name='report',
            name='prevention_of_incident',
            field=models.TextField(blank=True, default='', verbose_name='Actions to Prevent Incidents'),
        ),
    ]
