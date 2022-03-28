from django.test import SimpleTestCase
from app.forms import ReportForm


class TestReportForms(SimpleTestCase):

    def test_report_form(self):
        form = ReportForm(data={
            'community': 'NRSD',

            'residents': 'resident1',
            'staff': 'staff1',
            'others': 'others1',

            'name_of_writer': 'name_of_writer1',
            'incident_location': 'incident_location1',
            'date_of_incident': '2006-10-25 14:30:59',

            'fall_risk_assessment': 'fall_risk_assessment1',
            'employee_wcb_form': 'employee_wcb_form1',
            'employer_wcb_form': 'employer_wcb_form1',

            'incident_type': 'N',

            # 'medication_error': 'IRE'
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
             'pupil_size_L': 10,
             'pupil_size_R': 10,
             'CS': 10,
            #
             'family_notified': 'family_notified1',
             'family_name': 'family_name1',
             'family_notification_date': '2006-10-25 14:30:59',
            #
             'physician_notified': 'physician_notified1',
             'physician_name': 'physician_name1',
             'physician_notification_date': '2006-10-25 14:30:59',
            #
             'supervisor_notified': 'supervisor_notified1',
             'supervisor_name': 'supervisor_name1',
             'supervisor_notification_date': '2006-10-25 14:30:59',
            #
             'action_treatment_prescribed': 'action_treatment_prescribed1',
             'cause_of_incident': 'cause_of_incident1',
             'prevention_of_incident': 'prevention_of_incident1',
             'incident_documented_on_chart': 'incident_documented_on_chart1',
             'post_incident_huddle_held': 'post_incident_huddle_held1',
             'post_incident_huddle_charted': 'post_incident_huddle_charted1',
            #
             'follow_up_notes': 'follow_up_notes1',
             'physician_comments': 'physician_comments1',
            #
            'administrator_signature': 'administrator_signature1',
            'physician_signature': 'physician_signature1'

        })
        self.assertTrue(form.is_valid())

    def test_report_form_no_data(self):
        form = ReportForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 36)




