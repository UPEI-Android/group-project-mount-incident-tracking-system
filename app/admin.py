from django.contrib import admin
from . import models


# Creates a template to group fields together when you create, update, or view a report in the admin backend
class ReportAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Individuals Involved', {
            'fields': ('residents', 'staff', 'others', 'community')
        }),
        ('Basic Incident Information', {
            'fields': ('writer_first_name', 'writer_last_name', 'writer_position',
                       'incident_location', 'date_of_incident')
        }),
        ('Additional Forms', {
            'fields': ('fall_risk_assessment', 'employee_wcb_form', 'employer_wcb_form')
        }),
        ('Type of Incident', {
            'fields': (('near_miss', 'fall', 'medication_error', 'treatment_error'), ('loss_of_property',
                       'death', 'other_type_of_incident', 'staff_injury'))
        }),
        ('Reason for Medication Error', {
            'fields': (('incorrect_resident', 'incorrect_route', 'incorrect_dose', 'incorrect_label'),
                       ('incorrect_name', 'incorrect_time', 'incorrect_drug', 'drug_missing'),
                       ('extra_dose_given', 'dose_omitted', 'pharmacy_error', 'other_medication_error'))
        }),
        ('Incident Description', {
            'fields': ('condition', 'condition_other_description')
        }),
        ('Vital Signs', {
            'fields': (('T', 'P', 'R'), ('BP', 'SpO2', 'blood_sugar', 'NVS_report_completed'))
        }),
        ('Required Notifications', {
            'fields': (('family_notified', 'family_name', 'family_notification_date'),
                       ('physician_notified', 'physician_name', 'physician_notification_date'),
                       ('supervisor_notified', 'supervisor_name', 'supervisor_notification_date'))
        }),
        ('Post Incident', {
            'fields': ('incident_documented_on_chart', 'post_incident_huddle_held', 'post_incident_huddle_charted')
        }),
        ('Notes', {
            'fields': ('follow_up_notes', 'physician_comments')
        }),
        #TODO Add fields tracking submission account and completed account
        ('Automatically Generated Information', {
            'fields': ('report_status', 'reporter_account')
        })
    )


admin.site.register(models.Report, ReportAdmin)
