from django import forms
from app.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def validate(self):
        form_data = self.cleaned_data

        # Checks that required fields are apparent in data

        if form_data.get('writer_first_name') == '':
            self.add_error('writer_first_name',
                           forms.ValidationError('First Name of Writer is required', code='No First Name of Writer'))

        if form_data.get('writer_last_name') == '':
            self.add_error('writer_last_name',
                           forms.ValidationError('Last Name of Writer is required', code='No Last Name of Writer'))

        if form_data.get('writer_position') == '':
            self.add_error('writer_position',
                           forms.ValidationError('Position of Writer is required', code='No Position of Writer'))

        if form_data.get('incident_location') is None:
            self.add_error('incident_location',
                           forms.ValidationError('Incident Location is required', code='No Incident Location'))

        if form_data.get('date_of_incident') is None:
            self.add_error('date_of_incident',
                           forms.ValidationError('Date of Incident is required', code='No Date of Incident'))

        if form_data.get('incident_description') == '':
            self.add_error('incident_description',
                           forms.ValidationError('Incident Description is required', code='No Incident Description'))

        if form_data.get('action_taken') == '':
            self.add_error('action_taken', forms.ValidationError('Action Taken is required', code='No Action Taken'))

        if form_data.get('T') is None:
            self.add_error('T', forms.ValidationError('T Vital Sign is required', code='No T Vital Sign'))

        if form_data.get('P') is None:
            self.add_error('P', forms.ValidationError('P Vital Sign is required', code='No P Vital Sign'))

        if form_data.get('R') is None:
            self.add_error('R', forms.ValidationError('R Vital Sign is required', code='No R Vital Sign'))

        if form_data.get('BP') is None:
            self.add_error('BP', forms.ValidationError('BP Vital Sign is required', code='No BP Vital Sign'))

        if form_data.get('SpO2') is None:
            self.add_error('SpO2', forms.ValidationError('SpO2 Vital Sign is required', code='No SpO2 Vital Sign'))

        if form_data.get('blood_sugar') is None:
            self.add_error('blood_sugar',
                           forms.ValidationError('Blood Sugar Value is required', code='No Blood Sugar Value'))

        if form_data.get('pupil_size_L') is None:
            self.add_error('pupil_size_L',
                           forms.ValidationError('Pupil Size L Neuro-Vital Sign is required', code='No Pupil Size L'))

        if form_data.get('pupil_size_R') is None:
            self.add_error('pupil_size_R',
                           forms.ValidationError('Pupil Size R Neuro-Vital Sign is required', code='No Pupil Size R'))

        if form_data.get('CS') is None:
            self.add_error('CS',
                           forms.ValidationError('CS Neuro-Vital Sign is required', code='No CS Neuro-Vital Sign'))

        # Check if at least one of the individuals involved fields has an input
        if (form_data.get('residents') == '') & (form_data.get('staff') == '') & (form_data.get('others') == ''):
            self.add_error('residents',
                           forms.ValidationError('Individuals Involved must be filled', code='No Individuals'))
            self.add_error('staff',
                           forms.ValidationError('Individuals Involved must be filled', code='No Individuals'))
            self.add_error('others',
                           forms.ValidationError('Individuals Involved must be filled', code='No Individuals'))

        # Check if the community field has been selected if the incident involves a resident
        if (form_data.get('residents') != '') & (form_data.get('community') is None):
            self.add_error('community', forms.ValidationError('Resident\'s Community Must Be Selected',
                                                              code='Empty Community'))

        # Check if the community field has been selected and the incident doesn't involve a resident
        if (form_data.get('residents') == '') & (form_data.get('community') is not None):
            self.add_error('residents',
                           forms.ValidationError('Resident\'s name not provided after selecting resident\'s community',
                                                 code='Empty Resident'))

        # Check if the incident location has been selected and other location specified if necessary
        if form_data.get('incident_location') is None:
            self.add_error('incident_location', forms.ValidationError('Incident Location not specified',
                                                                      code='No Location'))
        elif (form_data.get('incident_location') == 'OT') & (form_data.get('incident_location_other') == ''):
            self.add_error('incident_location_other', forms.ValidationError('Other Incident Location Not Specified',
                                                                            code='No Incident Location Description'))

        # Check if the incident type has been selected
        if ((form_data.get('near_miss') is None) & (form_data.get('fall') is None) &
                (form_data.get('medication_error') is None) & (form_data.get('treatment_error') is None) &
                (form_data.get('loss_of_property') is None) & (form_data.get('death') is None) &
                (form_data.get('other_type_of_incident') is None) & (form_data.get('staff_injury') is None)):
            self.add_error('other_type_of_incident',
                           forms.ValidationError('Please select incident type', code='Empty Incident Type'))

        # Check if the medication error has been selected
        if ((form_data.get('medication_error') is not None) & (form_data.get('incorrect_resident') is None) &
                (form_data.get('incorrect_route') is None) & (form_data.get('incorrect_dose') is None) &
                (form_data.get('incorrect_label') is None) & (form_data.get('incorrect_name') is None) &
                (form_data.get('drug_missing') is None) & (form_data.get('incorrect_time') is None) &
                (form_data.get('extra_dose_given') is None) & (form_data.get('incorrect_drug') is None) &
                (form_data.get('dose_omitted') is None) & (form_data.get('pharmacy_error') is None) &
                (form_data.get('other_medication_error') is None)):
            self.add_error('medication_error',
                           forms.ValidationError('Medication Error Not Selected', code='Empty Medication Error'))

        # Check that the condition is listed and if other check that a description is given
        if form_data.get('condition') is None:
            self.add_error('condition',
                           forms.ValidationError('Please select individual\'s condition', code='Empty Condition'))
        elif (form_data.get('condition') == 'O') & (form_data.get('condition_other_description') == ''):
            self.add_error('condition_other_description',
                           forms.ValidationError('Other Condition Not Properly Specified',
                                                 code='No Condition Description'))

        # Check if the family of the resident involved has been notified correctly
        if form_data.get('family_notified') == 'True':
            if form_data.get('family_name') == '':
                self.add_error('family_name', forms.ValidationError('No Family Notification Name Provided',
                                                                    code='No Family Name'))
            if form_data.get('family_notification_date') is None:
                self.add_error('family_notification_date', forms.ValidationError('No Family Notification Date Provided',
                                                                                 code='No Family Date'))

        # Check if a physician has been notified correctly
        if form_data.get('physician_notified') == 'True':
            if form_data.get('physician_name') == '':
                self.add_error('physician_name', forms.ValidationError('No Physician Notification Name Provided',
                                                                       code='No Physician Name'))
            if form_data.get('physician_notification_date') is None:
                self.add_error('physician_notification_date',
                               forms.ValidationError('No Physician Notification Date Provided', code='No Physician Date'))

        # Check if a supervisor has been notified correctly
        if form_data.get('supervisor_notified') == 'True':
            if form_data.get('supervisor_name') == '':
                self.add_error('supervisor_name', forms.ValidationError('No Supervisor Notification Name Provided',
                                                                        code='No Supervisor Name'))
            if form_data.get('supervisor_notification_date') is None:
                self.add_error('supervisor_notification_date',
                               forms.ValidationError('No Supervisor Notification Date Provided',
                                                     code='No Supervisor Date'))
