from django.conf import settings
from django.db import models


class Report(models.Model):

    #Community choices
    ST_DUNSTANS = ("NCSD", "St. Dunstan's")
    HILLTOP = ("NCHT", "Hilltop")
    CARRIAGE_HOUSE = ("NCCH", "Carriage House")
    COMMUNITY_CARE = ("CCCC", "Community Care")
    OTHER = ("OTHR", "Other")
    COMMUNITY_CHOICES = [
        CARRIAGE_HOUSE,
        COMMUNITY_CARE,
        HILLTOP,
        ST_DUNSTANS,
        OTHER
    ]
    community = models.CharField(
        max_length=4,
        choices=COMMUNITY_CHOICES,
        default=None,
        blank=True,
        null=True,
        verbose_name='Community'
    )

    #Individuals involved
    residents = models.TextField(default='', blank=True, verbose_name='Resident(s) Involved')
    staff = models.TextField(default='', blank=True, verbose_name='Staff Member(s) Involved')
    others = models.TextField(default='', blank=True, verbose_name='Other Individual(s) Involved')

    #Basic Incident Information
    name_of_writer = models.CharField(max_length=120, default='', blank=True, verbose_name='Name of Report Writer')
    incident_location = models.CharField(max_length=120, default='', blank=True, verbose_name='Incident Location')
    date_of_incident = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Date of Incident')

    #Radio Buttons
    fall_risk_assessment = models.BooleanField(default=False, null=True, verbose_name='Fall Risk Assessment Performed')
    employee_wcb_form = models.BooleanField(default=False, null=True, verbose_name='Employee WCB Form Submitted')
    employer_wcb_form = models.BooleanField(default=False, null=True, verbose_name='Employer WCB Form Submitted')

    #Type of Incident
    near_miss = models.BooleanField(default=False, null=True, verbose_name='Near Miss')
    fall = models.BooleanField(default=False, null=True, verbose_name='Fall')
    medication_error = models.BooleanField(default=False, null=True, verbose_name='Medication Error')
    treatment_error = models.BooleanField(default=False, null=True, verbose_name='Treatment Error')
    loss_of_property = models.BooleanField(default=False, null=True, verbose_name='Loss of Property')
    death = models.BooleanField(default=False, null=True, verbose_name='Death')
    other_type_of_incident = models.BooleanField(default=False, null=True, verbose_name='Other Type of Incident')
    staff_injury = models.BooleanField(default=False, null=True, verbose_name='Staff Injury')

    #Reason for Medication Error
    incorrect_resident = models.BooleanField(default=False, null=True, verbose_name='Incorrect Resident')
    incorrect_route = models.BooleanField(default=False, null=True, verbose_name='Incorrect Route')
    incorrect_dose = models.BooleanField(default=False, null=True, verbose_name='Incorrect Dose')
    incorrect_label = models.BooleanField(default=False, null=True, verbose_name='Incorrect Label')
    incorrect_name = models.BooleanField(default=False, null=True, verbose_name='Incorrect Name')
    incorrect_time = models.BooleanField(default=False, null=True, verbose_name='Incorrect Time')
    incorrect_drug = models.BooleanField(default=False, null=True, verbose_name='Incorrect Drug')
    drug_missing = models.BooleanField(default=False, null=True, verbose_name='Drug Missing')
    extra_dose_given = models.BooleanField(default=False, null=True, verbose_name='Extra Dose Given')
    dose_omitted = models.BooleanField(default=False, null=True, verbose_name='Dose Omitted')
    pharmacy_error = models.BooleanField(default=False, null=True, verbose_name='Pharmacy Error')
    other_medication_error = models.BooleanField(default=False, null=True, verbose_name='Other Medication Error')

    #Incident description
    incident_description = models.TextField(default='', blank=True, verbose_name='Incident Description')
    action_taken = models.TextField(default='', blank=True, verbose_name='Action Taken')

    #Condition of involved individual
    CONDITION_NORMAL = ("N", "Normal")
    CONDITION_UNCONSCIOUS = ("U", "Unconscious")
    CONDITION_SEDATED = ("S", "Sedated")
    CONDITION_DISORIENTED = ("D", "Disoriented")
    CONDITION_OTHER = ("O", "Other")
    CONDITION_CHOICES = [
        CONDITION_NORMAL,
        CONDITION_UNCONSCIOUS,
        CONDITION_SEDATED,
        CONDITION_DISORIENTED,
        CONDITION_OTHER
    ]
    condition = models.CharField(
        max_length=1,
        choices=CONDITION_CHOICES,
        default=None,
        blank=True,
        null=True,
        verbose_name='Condition'
    )
    condition_other_description = models.TextField(default='', blank=True, verbose_name='Other Condition Description')

    #Vital Signs
    T = models.IntegerField(default=0, blank=True, null=True)
    P = models.IntegerField(default=0, blank=True, null=True)
    R = models.IntegerField(default=0, blank=True, null=True)
    BP = models.IntegerField(default=0, blank=True, null=True)
    SpO2 = models.IntegerField(default=0, blank=True, null=True)
    blood_sugar = models.IntegerField(default=0, blank=True, null=True, verbose_name='Blood Sugar')

    #Neurovital Signs
    pupil_size_L = models.IntegerField(default=0, blank=True, null=True, verbose_name='Pupil Size Left')
    pupil_size_R = models.IntegerField(default=0, blank=True, null=True, verbose_name='Pupil Size Right')
    CS = models.IntegerField(default=0, blank=True, null=True)

    #Required Notifications
    family_notified = models.BooleanField(default=False, null=True, verbose_name='Family Notified')
    family_name = models.CharField(max_length=120, default='', blank=True, verbose_name='Family Name')
    family_notification_date = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Family Notification Date')

    physician_notified = models.BooleanField(default=False, null=True, verbose_name='Physician Notified')
    physician_name = models.CharField(max_length=120, default='', verbose_name='Physician Name', blank=True)
    physician_notification_date = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Physician Notification Date')

    supervisor_notified = models.BooleanField(default=False, null=True, verbose_name='Supervisor Notified')
    supervisor_name = models.CharField(max_length=120, default='', verbose_name='Supervisor Name', blank=True)
    supervisor_notification_date = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Supervisor Notification Date')

    #Post Incident
    incident_documented_on_chart = models.BooleanField(default=False, null=True, verbose_name='Incident Documented On Chart')
    post_incident_huddle_held = models.BooleanField(default=False, null=True, verbose_name='Post Incident Huddle Held')
    post_incident_huddle_charted = models.BooleanField(default=False, null=True, verbose_name='Post Incident Huddle Charted')

    #Notes
    follow_up_notes = models.TextField(default='', blank=True, verbose_name='Follow Up Notes')
    physician_comments = models.TextField(default='', blank=True, verbose_name='Physician\'s Comments')

    #Automatically Generated Information
    report_submission_date = models.DateTimeField(auto_now_add=True, verbose_name='Report Submission Date')
    reporter_account = models.TextField(default='', blank=True, verbose_name='Reporter Account Username')
    #Report Statuses
    COMPLETE = ('CO', 'Complete')
    PARTIALLY_COMPLETED = ('PC', 'Partially Completed')
    PENDING_PHYSICIAN = ('PP', 'Pending Physician\'s Signature')
    SUBMITTED = ('SU', 'Submitted')
    STATUS_CHOICES = [
        COMPLETE,
        PARTIALLY_COMPLETED,
        PENDING_PHYSICIAN,
        SUBMITTED
    ]
    report_status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='PC',
        blank=True,
        verbose_name='Report Status'
    )
