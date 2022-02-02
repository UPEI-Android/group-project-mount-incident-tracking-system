from django.db import models

# Database configuration here

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
    )

    #Individuals involved
    residents = models.TextField(default='')
    staff = models.TextField(default='')
    others = models.TextField(default='')

    #Basic Incident Information
    name_of_writer = models.CharField(max_length=120, default='')
    incident_location = models.CharField(max_length=120, default='')
    date_of_incident = models.DateTimeField(default=None)

    #Radio Buttons
    fall_risk_assessment = models.BooleanField(default=False)
    employee_wcb_form = models.BooleanField(default=False)
    employer_wcb_form = models.BooleanField(default=False)

    #Type of Incident
    near_miss = models.BooleanField(default=False)
    fall = models.BooleanField(default=False)
    medication_error = models.BooleanField(default=False)
    treatment_error = models.BooleanField(default=False)
    loss_of_property = models.BooleanField(default=False)
    death = models.BooleanField(default=False)
    other_type_of_incident = models.BooleanField(default=False)
    staff_injury = models.BooleanField(default=False)

    #Reason for Medication Error
    incorrect_resident = models.BooleanField(default=False)
    incorrect_route = models.BooleanField(default=False)
    incorrect_dose = models.BooleanField(default=False)
    incorrect_label = models.BooleanField(default=False)
    incorrect_name = models.BooleanField(default=False)
    incorrect_time = models.BooleanField(default=False)
    incorrect_drug = models.BooleanField(default=False)
    drug_missing = models.BooleanField(default=False)
    extra_dose_given = models.BooleanField(default=False)
    dose_omitted = models.BooleanField(default=False)
    pharmacy_error = models.BooleanField(default=False)
    other_medication_error = models.BooleanField(default=False)

    #Incident description
    incident_description = models.TextField(default='')
    action_taken = models.TextField(default='')

    #Condition of involved individual
    condition_normal = models.BooleanField(default=False)
    condition_unconscious = models.BooleanField(default=False)
    condition_sedated = models.BooleanField(default=False)
    condition_disoriented = models.BooleanField(default=False)
    condition_other = models.BooleanField(default=False)
    condition_other_description = models.TextField(default='')

    #Vital Signs
    T = models.IntegerField(default=0)
    P = models.IntegerField(default=0)
    R = models.IntegerField(default=0)
    BP = models.IntegerField(default=0)
    SpO2 = models.IntegerField(default=0)
    blood_sugar = models.IntegerField(default=0)

    #Neurovital Signs
    pupil_size_L = models.IntegerField(default=0)
    pupil_size_R = models.IntegerField(default=0)
    CS = models.IntegerField(default=0)

    #Required Notifications
    family_notified = models.BooleanField(default=False)
    family_name = models.CharField(max_length=120, default='')
    family_notification_date = models.DateTimeField(default=None)

    physician_notified = models.BooleanField(default=False)
    physician_name = models.CharField(max_length=120, default='')
    physician_notification_date = models.DateTimeField(default=None)

    supervisor_notified = models.BooleanField(default=False)
    supervisor_name = models.CharField(max_length=120, default='')
    supervisor_notification_date = models.DateTimeField(default=None)

    #Post Incident
    incident_documented_on_chart = models.BooleanField(default=False)
    post_incident_huddle_held = models.BooleanField(default=False)
    post_incident_huddle_charted = models.BooleanField(default=False)

    #Notes
    follow_up_notes = models.TextField(default='')
    physician_comments = models.TextField(default='')

    #Automatically Generated Information
    report_submission_date = models.DateTimeField(auto_now_add=True)
