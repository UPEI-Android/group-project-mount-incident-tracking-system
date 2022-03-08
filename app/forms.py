from django import forms
from app.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def clean(self):
        form_data = super().clean()

        #Check if at least one of the individuals involved fields has an input
        if (form_data.get('residents') == '') & (form_data.get('staff') == '') & (form_data.get('others') == ''):
            self.add_error('residents',
                           forms.ValidationError('Individuals Involved must be filled', code='No Individuals'))
            self.add_error('staff',
                           forms.ValidationError('Individuals Involved must be filled', code='No Individuals'))
            self.add_error('others',
                           forms.ValidationError('Individuals Involved must be filled', code='No Individuals'))

        #Check if the community field has been selected if the incident involves a resident
        if (form_data.get('residents') is not None) & (form_data.get('community') is None):
            self.add_error('community', forms.ValidationError('Resident\'s Community Must Be Selected',
                                                              code='Empty Community'))

        #Check if the community field has been selected and the incident doesn't involve a resident
        if (form_data.get('residents') == '') & (form_data.get('community') is not None):
            self.add_error('residents',
                           forms.ValidationError('Resident\'s name not provided after selecting resident\'s community',
                                                 code='Empty Resident'))

        #Check if the incident type has been selected
        if (not form_data.get('near_miss')) & (not form_data.get('fall')) & \
                (not form_data.get('medication_error')) & (not form_data.get('treatment_error')) & \
                (not form_data.get('loss_of_property')) & (not form_data.get('death')) & \
                (not form_data.get('other_type_of_incident')) & (not form_data.get('staff_injury')):
            self.add_error('other_type_of_incident',
                           forms.ValidationError('Please select incident type', code='Empty Incident Type'))

        #Check if the medication error has been selected
        if form_data.get('medication_error') & (not form_data.get('incorrect_resident')) & \
                (not form_data.get('incorrect_route')) & (not form_data.get('incorrect_dose')) & \
                (not form_data.get('incorrect_label')) & (not form_data.get('incorrect_name')) & \
                (not form_data.get('drug_missing')) & (not form_data.get('incorrect_time')) & \
                (not form_data.get('extra_dose_given')) & (not form_data.get('incorrect_drug')) & \
                (not form_data.get('dose_omitted')) & (not form_data.get('pharmacy_error')) & \
                (not form_data.get('other_medication_error')):
            self.add_error('medication_error',
                           forms.ValidationError('Medication Error Not Selected', code='Empty Medication Error'))

        #Check that the condition is listed and if other check that a description is given
        if form_data.get('condition') is None:
            self.add_error('condition',
                           forms.ValidationError('Please select individual\'s condition', code='Empty Condition'))
        elif (form_data.get('condition') == 'O') & (form_data.get('condition_other_description') == ''):
            self.add_error('condition_other_description',
                           forms.ValidationError('Other Condition Not Properly Specified',
                                                 code='No Condition Description'))

        #Check if the family of the resident involved has been notified correctly
        if form_data.get('family_notified') is None:
            self.add_error('family_notified',
                           forms.ValidationError('Family Notification Status Not Selected', code='No Option Selected'))
        elif form_data.get('family_notified') == 'True':
            if form_data.get('family_name') == '':
                self.add_error('family_name', forms.ValidationError('No Family Notification Name Provided',
                                                                    code='No Family Name'))
            if form_data.get('family_notification_date') is None:
                self.add_error('family_notification_date', forms.ValidationError('No Family Notification Date Provided',
                                                                                 code='No Family Date'))

        # Check if a physician has been notified correctly
        if form_data.get('physician_notified') is None:
            self.add_error('physician_notified',
                           forms.ValidationError('Physician Notification Status Not Selected',
                                                 code='No Option Selected'))
        elif form_data.get('physician_notified') == 'True':
            if form_data.get('physician_name') == '':
                self.add_error('physician_name', forms.ValidationError('No Physician Notification Name Provided',
                                                                       code='No Physician Name'))
            if form_data.get('physician_notification_date') is None:
                self.add_error('physician_notification_date',
                               forms.ValidationError('No Physician Notification Date Provided', code='No Physician Date'))

        # Check if a supervisor has been notified correctly
        if form_data.get('supervisor_notified') is None:
            self.add_error('supervisor_notified',
                           forms.ValidationError('Supervisor Notification Status Not Selected',
                                                 code='No Option Selected'))
        elif form_data.get('supervisor_notified') == 'True':
            if form_data.get('supervisor_name') == '':
                self.add_error('supervisor_name', forms.ValidationError('No Supervisor Notification Name Provided',
                                                                        code='No Supervisor Name'))
            if form_data.get('supervisor_notification_date') is None:
                self.add_error('supervisor_notification_date',
                               forms.ValidationError('No Supervisor Notification Date Provided',
                                                     code='No Supervisor Date'))

