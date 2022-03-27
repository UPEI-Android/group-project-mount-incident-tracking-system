# Generated by Django 3.2.12 on 2022-03-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.CharField(blank=True, choices=[('NCCH', 'Carriage House'), ('CCCC', 'Community Care'), ('NCHT', 'Hilltop'), ('NCSD', "St. Dunstan's"), ('OTHR', 'Other')], default=None, max_length=4, null=True, verbose_name='Community')),
                ('residents', models.TextField(blank=True, default='', verbose_name='Resident(s) Involved')),
                ('staff', models.TextField(blank=True, default='', verbose_name='Staff Member(s) Involved')),
                ('others', models.TextField(blank=True, default='', verbose_name='Other Individual(s) Involved')),
                ('name_of_writer', models.CharField(blank=True, default='', max_length=120, verbose_name='Name of Report Writer')),
                ('incident_location', models.CharField(blank=True, default='', max_length=120, verbose_name='Incident Location')),
                ('date_of_incident', models.DateTimeField(blank=True, default='1999-12-31 11:59[:59[.999999]][America/Halifax]', null=True, verbose_name='Date of Incident')),
                ('fall_risk_assessment', models.BooleanField(default=False, null=True, verbose_name='Fall Risk Assessment Performed')),
                ('employee_wcb_form', models.BooleanField(default=False, null=True, verbose_name='Employee WCB Form Submitted')),
                ('employer_wcb_form', models.BooleanField(default=False, null=True, verbose_name='Employer WCB Form Submitted')),
                ('near_miss', models.BooleanField(default=False, null=True, verbose_name='Near Miss')),
                ('fall', models.BooleanField(default=False, null=True, verbose_name='Fall')),
                ('medication_error', models.BooleanField(default=False, null=True, verbose_name='Medication Error')),
                ('treatment_error', models.BooleanField(default=False, null=True, verbose_name='Treatment Error')),
                ('loss_of_property', models.BooleanField(default=False, null=True, verbose_name='Loss of Property')),
                ('death', models.BooleanField(default=False, null=True, verbose_name='Death')),
                ('other_type_of_incident', models.BooleanField(default=False, null=True, verbose_name='Other Type of Incident')),
                ('staff_injury', models.BooleanField(default=False, null=True, verbose_name='Staff Injury')),
                ('incorrect_resident', models.BooleanField(default=False, null=True, verbose_name='Incorrect Resident')),
                ('incorrect_route', models.BooleanField(default=False, null=True, verbose_name='Incorrect Route')),
                ('incorrect_dose', models.BooleanField(default=False, null=True, verbose_name='Incorrect Dose')),
                ('incorrect_label', models.BooleanField(default=False, null=True, verbose_name='Incorrect Label')),
                ('incorrect_name', models.BooleanField(default=False, null=True, verbose_name='Incorrect Name')),
                ('incorrect_time', models.BooleanField(default=False, null=True, verbose_name='Incorrect Time')),
                ('incorrect_drug', models.BooleanField(default=False, null=True, verbose_name='Incorrect Drug')),
                ('drug_missing', models.BooleanField(default=False, null=True, verbose_name='Drug Missing')),
                ('extra_dose_given', models.BooleanField(default=False, null=True, verbose_name='Extra Dose Given')),
                ('dose_omitted', models.BooleanField(default=False, null=True, verbose_name='Dose Omitted')),
                ('pharmacy_error', models.BooleanField(default=False, null=True, verbose_name='Pharmacy Error')),
                ('other_medication_error', models.BooleanField(default=False, null=True, verbose_name='Other Medication Error')),
                ('incident_description', models.TextField(blank=True, default='', verbose_name='Incident Description')),
                ('action_taken', models.TextField(blank=True, default='', verbose_name='Action Taken')),
                ('condition', models.CharField(blank=True, choices=[('N', 'Normal'), ('U', 'Unconscious'), ('S', 'Sedated'), ('D', 'Disoriented'), ('O', 'Other')], default=None, max_length=1, null=True, verbose_name='Condition')),
                ('condition_other_description', models.TextField(blank=True, default='', verbose_name='Other Condition Description')),
                ('T', models.IntegerField(blank=True, default=0, null=True)),
                ('P', models.IntegerField(blank=True, default=0, null=True)),
                ('R', models.IntegerField(blank=True, default=0, null=True)),
                ('BP', models.IntegerField(blank=True, default=0, null=True)),
                ('SpO2', models.IntegerField(blank=True, default=0, null=True)),
                ('blood_sugar', models.IntegerField(blank=True, default=0, null=True, verbose_name='Blood Sugar')),
                ('pupil_size_L', models.IntegerField(blank=True, default=0, null=True, verbose_name='Pupil Size Left')),
                ('pupil_size_R', models.IntegerField(blank=True, default=0, null=True, verbose_name='Pupil Size Right')),
                ('CS', models.IntegerField(blank=True, default=0, null=True)),
                ('family_notified', models.BooleanField(default=False, null=True, verbose_name='Family Notified')),
                ('family_name', models.CharField(blank=True, default='', max_length=120, verbose_name='Family Name')),
                ('family_notification_date', models.DateTimeField(blank=True, default='1999-12-31 11:59[:59[.999999]][America/Halifax]', null=True, verbose_name='Family Notification Date')),
                ('physician_notified', models.BooleanField(default=False, null=True, verbose_name='Physician Notified')),
                ('physician_name', models.CharField(blank=True, default='', max_length=120, verbose_name='Physician Name')),
                ('physician_notification_date', models.DateTimeField(blank=True, default='1999-12-31 11:59[:59[.999999]][America/Halifax]', null=True, verbose_name='Physician Notification Date')),
                ('supervisor_notified', models.BooleanField(default=False, null=True, verbose_name='Supervisor Notified')),
                ('supervisor_name', models.CharField(blank=True, default='', max_length=120, verbose_name='Supervisor Name')),
                ('supervisor_notification_date', models.DateTimeField(blank=True, default='1999-12-31 11:59[:59[.999999]][America/Halifax]', null=True, verbose_name='Supervisor Notification Date')),
                ('incident_documented_on_chart', models.BooleanField(default=False, null=True, verbose_name='Incident Documented On Chart')),
                ('post_incident_huddle_held', models.BooleanField(default=False, null=True, verbose_name='Post Incident Huddle Held')),
                ('post_incident_huddle_charted', models.BooleanField(default=False, null=True, verbose_name='Post Incident Huddle Charted')),
                ('follow_up_notes', models.TextField(blank=True, default='', verbose_name='Follow Up Notes')),
                ('physician_comments', models.TextField(blank=True, default='', verbose_name="Physician's Comments")),
                ('report_submission_date', models.DateTimeField(auto_now_add=True, verbose_name='Report Submission Date')),
                ('reporter_account', models.TextField(blank=True, default='', verbose_name='Reporter Account Username')),
                ('report_status', models.CharField(blank=True, choices=[('CO', 'Complete'), ('PC', 'Partially Completed'), ('PP', "Pending Physician's Signature"), ('SU', 'Submitted')], default='PC', max_length=2, verbose_name='Report Status')),
            ],
        ),
    ]