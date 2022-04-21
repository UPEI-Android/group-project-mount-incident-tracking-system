from django.test import SimpleTestCase
from app.forms import ReportForm


class TestReportForms(SimpleTestCase):
    # test to check if a form is validated (with data)
    def test_report_form(self):
        form = ReportForm(data={
            'community': 'NRSD',

            'residents': 'resident1',
            'staff': 'staff1',
            'others': 'others1',

            'writer_first_name': 'first_name',
            'writer_last_name': 'last_name',
            'writer_position': 'postion',
            'date_of_incident': '2006-10-25 14:30:59',
            'incident_location': 'BA',
            'incident_location_other': 'test',

            'fall_risk_assessment': 'fall_risk_assessment1',
            'employee_wcb_form': 'employee_wcb_form1',
            'employer_wcb_form': 'employer_wcb_form1',

            'near_miss': 'True',
            'fall': 'True',
            'medication_error': 'True',
            'treatment_error': 'True',
            'loss_of_property': 'True',
            'death': 'True',
            'other_type_of_incident': 'True',
            'staff_injury': 'True',

            'incorrect_resident': 'True',
            'incorrect_route': 'True',
            'incorrect_dose': 'True',
            'incorrect_label': 'True',
            'incorrect_name': 'True',
            'incorrect_time': 'True',
            'incorrect_drug': 'True',
            'drug_missing': 'True',
            'extra_dose_giving': 'True',
            'pharmacy_error': 'True',
            'other_medication_error': 'True',

            #
            'incident_description': 'incident_description1',
            'action_taken': 'action_taken1',
            #
            'condition': 'N',
            'condition_other_description': 'condition1',
            #
            'T': 10,
            'P': 10,
            'B': 10,
            'R': 10,
            'BP': 10,
            'Sp02': 10,
            'blood_sugar': 10,
            #
            'NVS_report_completed': 'True',
            #
            'family_notified': 'True',
            'family_name': 'family_name1',
            'family_notification_date': '2006-10-25 14:30:59',
            #
            'physician_notified': 'True',
            'physician_name': 'physician_name1',
            'physician_notification_date': '2006-10-25 14:30:59',
            #
            'supervisor_notified': 'True',
            'supervisor_name': 'supervisor_name1',
            'supervisor_notification_date': '2006-10-25 14:30:59',
            #
            'action_treatment_prescribed': 'action_treatment_prescribed1',
            'cause_of_incident': 'cause_of_incident1',
            'prevention_of_incident': 'prevention_of_incident1',
            'incident_documented_on_chart': 'True',
            'post_incident_huddle_held': 'True',
            'post_incident_huddle_charted': 'True',
            #
            'follow_up_notes': 'follow_up_notes1',
            'physician_comments': 'physician_comments1',
            #
            'administrator_signature': 'administrator_signature1',
            'physician_signature': 'physician_signature1',

            'report_submission_date': '2006-10-25 14:30:59',
            'reporter_account': 'username',
            'completing_account': 'username',
            'physician_review_account': 'physician'

        })
        self.assertTrue(form.is_valid())

    # test to see if a form is valid without data
    def test_report_form_no_data(self):
        form = ReportForm(data={})
        self.assertFalse(form.is_valid())
        # test to confirm form length
        self.assertEquals(len(form.errors), 67)
