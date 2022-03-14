from django import forms


class ReportForm(forms.Form):
    # Community choices
    """  ST_DUNSTANS = ("NRSD", "St. Dunstans")
    HILLTOP = ("NRHT", "Hilltop")
    CARRIAGE_HOUSE = ("NHCH", "Carriage House")
    COMMUNITY_CARE = ("CCCH", "Community Care")
    OTHER = ("OTHR", "Other")
    COMMUNITY_CHOICES = [
        ('', "-----"),
        CARRIAGE_HOUSE,
        COMMUNITY_CARE,
        HILLTOP,
        ST_DUNSTANS,
        OTHER
    ]"""

   # community = forms.ChoiceField(choices=COMMUNITY_CHOICES)

    #Individuals Involved
    residents = forms.CharField(strip=True, required=False)
    staff = forms.CharField(strip=True, required=False)
    others = forms.CharField(strip=True, required=False)
    """
    #Basic Incident Information
    name_of_writer = forms.CharField(max_length=120)
    incident_location = forms.CharField(max_length=120)
    date_of_incident = forms.DateTimeField()

    #Radio Buttons
    fall_risk_assessment = forms.BooleanField(required=False)
    employee_wcb_form = forms.BooleanField(required=False)
    employer_wcb_form = forms.BooleanField(required=False)

    # Type of Incident
     NEAR_MISS = ("N", "Near Miss")
    FALL = ("F", "Fall")
    MEDICATION_ERROR = ("M", "Medication Error")
    TREATMENT_ERROR = ("T", "Treatment Error")
    LOSS_OF_PROPERTY = ("L", "Loss of Property")
    DEATH = ("D", "Death")
    OTHER_TYPE_OF_INCIDENT = ("O", "Other Type of Incident")
    STAFF_INJURY = ("S", "Staff Injury")
    INCIDENT_TYPE_CHOICES = [
        ('', '-----'),
        NEAR_MISS, FALL, MEDICATION_ERROR, TREATMENT_ERROR,
        LOSS_OF_PROPERTY, DEATH, OTHER_TYPE_OF_INCIDENT, STAFF_INJURY] """

    #incident_type = forms.ChoiceField(choices=INCIDENT_TYPE_CHOICES)
    """
    # Reason for Medication Error
    INCORRECT_RESIDENT = ("IRE", "Incorrect Resident")
    INCORRECT_ROUTE = ("IRO", "Incorrect Route")
    INCORRECT_DOSE = ("IDO", "Incorrect Dose")
    INCORRECT_LABEL = ("ILA", "Incorrect Label")
    INCORRECT_NAME = ("INA", "Incorrect Name")
    INCORRECT_TIME = ("ITI", "Incorrect Time")
    INCORRECT_DRUG = ("IDR", "Incorrect Drug")
    DRUG_MISSING = ("DMI", "Drug Missing")
    EXTRA_DOSE_GIVEN = ("EDG", "Extra Dose Given")
    DOSE_OMITTED = ("DOM", "Dose Omitted")
    PHARMACY_ERROR = ("PER", "Pharmacy Error")
    OTHER_MEDICATION_ERROR = ("OME", "Other Medication Error")
    MEDICATION_ERROR_CHOICES = [
        ('', '-----'),
        INCORRECT_RESIDENT, INCORRECT_ROUTE, INCORRECT_DOSE, INCORRECT_LABEL,
        INCORRECT_NAME, INCORRECT_TIME, INCORRECT_DRUG, DRUG_MISSING,
        EXTRA_DOSE_GIVEN, DOSE_OMITTED, PHARMACY_ERROR, OTHER_MEDICATION_ERROR
    ]

   # medication_error = forms.MultipleChoiceField(choices=MEDICATION_ERROR_CHOICES)

    #Incident Description
    incident_description = forms.CharField(strip=True)
    action_taken = forms.CharField(strip=True)"""

    #Condition of Involved Individual
    """  CONDITION_NORMAL = ("N", "Condition Normal")
    CONDITION_UNCONSCIOUS = ("U", "Condition Unconscious")
    CONDITION_SEDATED = ("S", "Condition Sedated")
    CONDITION_DISORIENTED = ("D", "Condition Disoriented")
    CONDITION_OTHER = ("O", "Condition Other")
    CONDITION_CHOICES = [
        CONDITION_NORMAL,
        CONDITION_UNCONSCIOUS,
        CONDITION_SEDATED,
        CONDITION_DISORIENTED,
        CONDITION_OTHER
    ] 

    #condition = forms.ChoiceField(choices=CONDITION_CHOICES)
    condition_other_description = forms.CharField(strip=True, required=False)

    #Vital Signs
    T = forms.IntegerField()
    P = forms.IntegerField()
    R = forms.IntegerField()
    BP = forms.IntegerField()
    Sp02 = forms.IntegerField()
    blood_sugar = forms.IntegerField()

    #Neurovital Signs
    pupil_size_L = forms.IntegerField()
    pupil_size_R = forms.IntegerField()
    CS = forms.IntegerField()

    #Required Notifications
    family_notified = forms.BooleanField()
    family_name = forms.CharField(strip=True)
    family_notification_date = forms.DateTimeField()

    physician_notified = forms.BooleanField()
    physician_name = forms.CharField(strip=True)
    physician_notification_date = forms.DateTimeField()

    supervisor_notified = forms.BooleanField()
    supervisor_name = forms.CharField(strip=True)
    supervisor_notification_date = forms.DateTimeField()

    #Post Incident
    action_treatment_prescribed = forms.CharField(strip=True)
    cause_of_incident = forms.CharField(strip=True)
    prevention_of_incident = forms.CharField(strip=True)
    incident_documented_on_chart = forms.BooleanField()
    post_incident_huddle_held = forms.BooleanField()
    post_incident_huddle_charted = forms.BooleanField()

    #Notes
    follow_up_notes = forms.CharField()
    physician_comments = forms.CharField()

    #Signatures
    administrator_signature = forms.BooleanField()
    physician_signature = forms.BooleanField()"""

"""
    def clean(self):
        self.clean()
        form_data = self.cleaned_data
        if form_data['community'] == '':
            raise forms.ValidationError('Community must be selected', code='Empty Community')
        elif (form_data['residents'] == '') & (form_data['staff'] == '') & (form_data['others'] == ''):
            raise forms.ValidationError('Individuals Involved must be filled', code='No Individuals')
        elif form_data['incident_type'] == '':
            raise forms.ValidationError('Please select incident type', code='Empty Incident Type')
        elif (form_data['incident_type'] == 'M') & (form_data['medication_error'] == ''):
            raise forms.ValidationError('Medication Error Not Selected', code='Empty Medication Error')
        elif form_data['condition'] == '':
            raise forms.ValidationError('Please select individual\'s condition', code='Empty Condition')
        elif (form_data['condition'] == 'O') & (form_data['condition_other_description'] == ''):
            raise forms.ValidationError('Condition Not Properly Specified', code='No Condition Description')
        elif form_data['family_notified'] & \
                ((form_data['family_name'] == '') | (form_data['family_notification_date'] == '')):
            raise forms.ValidationError('Family Notification Error', code='No family name or date')
        elif form_data['physician_notified'] & \
                ((form_data['physician_name'] == '') | (form_data['physician_notification_date'] == '')):
            raise forms.ValidationError('Physician Notification Error', code='No physician name or date')
        elif form_data['supervisor_notified'] & \
                ((form_data['supervisor_name'] == '') | (form_data['supervisor_notification_date'] == '')):
            raise forms.ValidationError('Supervisor Notification Error', code='No supervisor name or date') """
