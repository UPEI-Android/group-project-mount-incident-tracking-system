from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator

# Creates template for database fields and specify requirements.
class Report(models.Model):

    # Community choices
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

    # Individuals involved
    residents = models.TextField(default='', blank=True, verbose_name='Resident(s) Involved')
    staff = models.TextField(default='', blank=True, verbose_name='Staff Member(s) Involved')
    others = models.TextField(default='', blank=True, verbose_name='Other Individual(s) Involved')

    # Basic Incident Information
    writer_first_name = models.CharField(max_length=60, default='', blank=True, verbose_name='First Name of Report Writer')
    writer_last_name = models.CharField(max_length=60, default='', blank=True, verbose_name='Last Name of Report Writter')
    writer_position = models.CharField(max_length=40, default='', blank=True, verbose_name='Position of Report Writer')
    date_of_incident = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Date of Incident')
    INCIDENT_LOCATION_BATHROOM = ("BA", "Bathroom")
    INCIDENT_LOCATION_BEDROOM = ("BE", "Bedroom")
    INCIDENT_LOCATION_HALLWAY = ("HA", "Hallway")
    INCIDENT_LOCATION_STAIRS = ("ST", "Stairs")
    INCIDENT_LOCATION_OTHER = ("OT", "Other")
    INCIDENT_LOCATIONS = [
        INCIDENT_LOCATION_BATHROOM,
        INCIDENT_LOCATION_BEDROOM,
        INCIDENT_LOCATION_HALLWAY,
        INCIDENT_LOCATION_STAIRS,
        INCIDENT_LOCATION_OTHER
    ]
    incident_location = models.CharField(max_length=2, choices=INCIDENT_LOCATIONS, default=None, blank=True, null=True, verbose_name="Incident Location")
    incident_location_other = models.CharField(max_length=80, default='', blank=True, verbose_name='Incident Location Description')

    # Radio Buttons
    fall_risk_assessment = models.BooleanField(default=False, null=True, verbose_name='Fall Risk Assessment Performed')
    employee_wcb_form = models.BooleanField(default=False, null=True, verbose_name='Employee WCB Form Submitted')
    employer_wcb_form = models.BooleanField(default=False, null=True, verbose_name='Employer WCB Form Submitted')

    # Type of Incident
    near_miss = models.BooleanField(default=False, null=True, verbose_name='Near Miss')
    fall = models.BooleanField(default=False, null=True, verbose_name='Fall')
    medication_error = models.BooleanField(default=False, null=True, verbose_name='Medication Error')
    treatment_error = models.BooleanField(default=False, null=True, verbose_name='Treatment Error')
    loss_of_property = models.BooleanField(default=False, null=True, verbose_name='Loss of Property')
    death = models.BooleanField(default=False, null=True, verbose_name='Death')
    other_type_of_incident = models.BooleanField(default=False, null=True, verbose_name='Other Type of Incident')
    staff_injury = models.BooleanField(default=False, null=True, verbose_name='Staff Injury')

    # Reason for Medication Error
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

    # Incident description
    incident_description = models.TextField(default='', blank=True, verbose_name='Incident Description')
    action_taken = models.TextField(default='', blank=True, verbose_name='Action Taken')

    # Condition of involved individual
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

    # Vital Signs
    T = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(50)], blank=True, null=True)
    P = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(500)], blank=True, null=True)
    R = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(500)], blank=True, null=True)
    BP = models.CharField(default=0, max_length=7, validators=[RegexValidator('\\d{1,3}\\/\\d{1,3}')], blank=True, null=True)
    SpO2 = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], blank=True, null=True)
    blood_sugar = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Blood Sugar')

    # Neurovital Signs
    NVS_report_completed = models.BooleanField(default=False, null=True, verbose_name='Neuro Vital Signs Report Completed')

    # Required Notifications
    family_notified = models.BooleanField(default=False, null=True, verbose_name='Family Notified')
    family_name = models.CharField(max_length=120, default='', blank=True, verbose_name='Family Name')
    family_notification_date = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Family Notification Date')

    physician_notified = models.BooleanField(default=False, null=True, verbose_name='Physician or Provider Notified')
    physician_name = models.CharField(max_length=120, default='', verbose_name='Physician or Provider\'s Name', blank=True)
    physician_notification_date = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Physician or Provider Notification Date')

    supervisor_notified = models.BooleanField(default=False, null=True, verbose_name='Supervisor Notified')
    supervisor_name = models.CharField(max_length=120, default='', verbose_name='Supervisor Name', blank=True)
    supervisor_notification_date = models.DateTimeField(default='1999-12-31 11:59[:59[.999999]][America/Halifax]', blank=True, null=True, verbose_name='Supervisor Notification Date')

    # Incident Prevention
    action_treatment_prescribed = models.TextField(default='', blank=True, verbose_name='Action or Treatment Prescribed')
    cause_of_incident = models.TextField(default='', blank=True, verbose_name='Cause of Incident')
    prevention_of_incident = models.TextField(default='', blank=True, verbose_name='Actions to Prevent Incidents')

    # Post Incident
    incident_documented_on_chart = models.BooleanField(default=False, null=True, verbose_name='Incident Documented On Chart')
    post_incident_huddle_held = models.BooleanField(default=False, null=True, verbose_name='Post Incident Huddle Held')
    post_incident_huddle_charted = models.BooleanField(default=False, null=True, verbose_name='Post Incident Huddle Charted')

    # Notes
    follow_up_notes = models.TextField(default='', blank=True, verbose_name='Follow Up Notes')
    physician_comments = models.TextField(default='', blank=True, verbose_name='Physician\'s Comments')

    # Automatically Generated Information
    report_submission_date = models.DateTimeField(auto_now_add=True, verbose_name='Report Submission Date')
    reporter_account = models.TextField(default='', blank=True, verbose_name='Reporter Account Username')
    completing_account = models.TextField(default='', blank=True, verbose_name='Reviewing Account Username')
    physician_review_account = models.TextField(default='', blank=True, verbose_name='Physician Review Account Username')

    # Report Statuses
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
