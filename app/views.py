from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import Report
from app.forms import ReportForm
from django import forms
import csv
from app.decorators import allowed_users


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'Invalid Credentials')
            return render(request, 'index.html')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'index.html')


def form(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['submit'] == "submit":
                # Create Report from the POST data
                report = ReportForm(request.POST)
                report.full_clean()
                report.validate()
                if report.is_valid():
                    # Create an instance of the database object to add the report status to

                    report_data = report.save(commit=False)
                    # Check if the resident is in a Nursing Care community to indicate that a Physician must review the report
                    if 'NC' in report_data.community:
                        report_data.report_status = 'PP'
                    else:
                        report_data.report_status = 'SU'
                    # Adds the reporting accounts username to the data and saves the data to the database
                    report_data.reporter_account = request.user.username
                    report_data.save()
                    # Displays a success message to the user and redirects them to the form page.
                    messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Submitted')
                    return render(request, 'input_form.html', {"username": request.user.username})
                else:
                    # Displays an error message to the user and redirects them to the form page.
                    messages.add_message(request, messages.WARNING, 'Error in Form')
                    return render(request, 'input_form.html', {"username": request.user.username, "report": report})
            elif request.POST['submit'] == "save":
                # Save Model without checking for empty fields
                # Create Report from the POST data
                report = ReportForm(request.POST)

                if report.is_valid():
                    report_data = report.save(commit=False)
                    report_data.report_status = 'PC'
                    report_data.reporter_account = request.user.username
                    report_data.save()
                    messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Submitted')
                    return render(request, 'input_form.html', {"username": request.user.username})
                else:
                    messages.add_message(request, messages.WARNING, 'Error in Form')
                    return render(request, 'input_form.html', {"username": request.user.username})

        return render(request, 'input_form.html', {"username": request.user.username})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def read_report(request, report_id):
    if request.user.is_authenticated:
        report = Report.objects.filter(id=report_id)[0]
        return render(request, "read_only_report.html",
                      {"username": request.user.username, "report_id": report_id, "report": report})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


@allowed_users(allowed_roles={"admins"})
def edit_report(request, report_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            report_instance = Report.objects.get(id=report_id)
            report = ReportForm(request.POST, instance=report_instance)
            if request.POST['submit'] == 'submit':
                report.full_clean()
                report.validate()
                if report.is_valid():
                    # Create an instance of the database object to add the report status to

                    report_data = report.save(commit=False)
                    # Check if the resident is in a Nursing Care community to indicate that a Physician must review
                    # the report
                    if 'NC' in report_data.community:
                        report_data.report_status = 'PP'
                    else:
                        report_data.report_status = 'SU'
                    # Adds the reporting accounts username to the data and saves the data to the database
                    report_data.save()
                    messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Submitted')
                    return redirect('read_report', report_id=report_id)
                else:
                    messages.add_message(request, messages.WARNING, 'Error in Form')
                    return render(request, 'input_form.html', {"username": request.user.username, "report": report})
            elif request.POST['submit'] == "save":
                if report.is_valid():
                    report_data = report.save(commit=False)
                    report_data.report_status = 'PC'
                    report_data.save()
                    messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Saved')
                    return redirect('read_report', report_id=report_id)
                else:
                    messages.add_message(request, messages.WARNING, 'Error in Form')
                    return render(request, 'input_form.html', {"username": request.user.username, "report": report})
        else:
            report = Report.objects.filter(id=report_id)[0]
            return render(request, "edit_report.html", {"username": request.user.username, "report": report})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def dashboard_export(request):
    if request.user.is_authenticated:
        reports = Report.objects.all()
        displayReports = reports.reverse()[:50]
        return render(request, "dashboard-export.html",
                      {"username": request.user.username, "reports": displayReports, "count": displayReports.count()})


def mark_report_complete(request, report_id):
    if request.user.is_authenticated:
        report = Report.objects.filter(id=report_id)[0]
        if report.report_status == "SU":
            report.report_status = "CO"
            report.completing_account = request.user.username
            report.save()
            messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Marked as Complete')
            return redirect('read_report', report_id=report_id)
        else:
            messages.add_message(request, messages.WARNING,
                                 f'Incident Report Form Cannot be Marked as Complete, Report Status:  {report.report_status}')
            return redirect('read_report', report_id=report_id)
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def sign_off_report(request, report_id):
    if request.user.is_authenticated:
        report = Report.objects.filter(id=report_id)[0]
        if report.report_status == "PP":
            report.report_status = "SU"
            report.physician_review_account = request.user.username
            report.save()
            messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Signed Off')
            return redirect('read_report', report_id=report_id)
        else:
            messages.add_message(request, messages.WARNING,
                                 f'Incident Report Form Cannot be Signed Off, Report Status:  {report.report_status}')
            return redirect('read_report', report_id=report_id)
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def export(request):
    if request.method == "GET":
        count = int(request.GET.get("report_count"))
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="Reports.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(
            ['Community', 'Residents', 'Staff', 'Others', 'Writer', 'Location', 'Date', 'Fall Risk Assessment',
             'Employee WCB Form', 'Employer WCB Form', 'Incident Type', 'Reason For Medication Error',
             'Incident Description', 'Action Taken', 'Condition', 'Vitals: T', 'Vitals: P', 'Vitals: R', 'Vitals: BP',
             'Vitals: SpO2', 'Vitals: Blood Sugar', 'Neurovitals: Pupil Size L', 'Neurovitals: Pupil Size R',
             'Neurovitals: CS', 'Family Notified', 'Family Member Name', 'Family Notification Date',
             'Physician Notified', 'Physician Name', 'Physician Notification Date', 'Supervisor Notified',
             'Supervisor Name', 'Supervisor Notification Date', 'Action Treatment Prescribed', 'Cause of Incident',
             'Prevention Plan of Incident', 'Incident Documented on Chart', 'Post Incident Huddle Held',
             'Post Incident Huddle Charted', 'Follow Up Notes', 'Physician Comments', 'Report Submission Date',
             'Reporter Account', 'Completion Account', 'Physician Account', 'Report Status'])

        for i in range(count):
            print("I Value: " + str(i))
            report_id = request.GET.get("reportID" + str(i))
            # report_id = int(report_id)
            print("reportID:" + str(report_id) + " Count: " + str(count))
            if (report_id != None):
                report = Report.objects.filter(id=report_id)[0]
                print("Report Loaded From DataBase: " + str(report.id))
                medication_error_reason = ""
                if (report.medication_error):
                    if (report.incorrect_resident):
                        medication_error_reason += "Incorrect Resident.\n"
                    if (report.incorrect_route):
                        medication_error_reason += "Incorrect Route.\n"
                    if (report.incorrect_dose):
                        medication_error_reason += "Incorrect Dose.\n"
                    if (report.incorrect_label):
                        medication_error_reason += "Incorrect Label.\n"
                    if (report.incorrect_name):
                        medication_error_reason += "Incorrect Name.\n"
                    if (report.incorrect_time):
                        medication_error_reason += "Incorrect Time.\n"
                    if (report.incorrect_drug):
                        medication_error_reason += "Incorrect Drug.\n"
                    if (report.extra_dose_given):
                        medication_error_reason += "Extra Dose Given.\n"
                    if (report.dose_omitted):
                        medication_error_reason += "Dose Omitted.\n"
                    if (report.pharmacy_error):
                        medication_error_reason += "Pharmacy Error.\n"
                    if (report.other_medication_error):
                        medication_error_reason += "Other Medication Error.\n"

                type_of_incident = ""
                if (report.near_miss):
                    type_of_incident += "Near Miss\n"
                if (report.fall):
                    type_of_incident += "Fall\n"
                if (report.medication_error):
                    type_of_incident += "Medication Error\n"
                if (report.treatment_error):
                    type_of_incident += "Treatment Error\n"
                if (report.loss_of_property):
                    type_of_incident += "Loss of Property\n"
                if (report.death):
                    type_of_incident += "Death\n"
                if (report.other_type_of_incident):
                    type_of_incident += "Other Type of Incident\n"
                if (report.staff_injury):
                    type_of_incident += "Staff Injury\n"

                writer.writerow(
                    [report.community, report.residents, report.staff, report.others, report.name_of_writer,
                     report.incident_location, report.date_of_incident, report.fall_risk_assessment,
                     report.employee_wcb_form, report.employer_wcb_form, type_of_incident, medication_error_reason,
                     report.incident_description, report.action_taken, report.condition, report.T, report.P, report.R,
                     report.BP, report.SpO2, report.blood_sugar, report.pupil_size_L,
                     report.pupil_size_R, report.CS, report.family_notified, report.family_name,
                     report.family_notification_date, report.physician_notified, report.physician_name,
                     report.physician_notification_date,
                     report.supervisor_notified, report.supervisor_name, report.supervisor_notification_date,
                     report.action_treatment_prescribed, report.cause_of_incident, report.prevention_of_incident,
                     report.incident_documented_on_chart, report.post_incident_huddle_held,
                     report.post_incident_huddle_charted,
                     report.follow_up_notes, report.physician_comments, report.report_submission_date,
                     report.reporter_account,
                     report.completing_account, report.physician_review_account, report.report_status])

            # for key, value in this_form.cleaned_data.iteritems():
            # writer.writerow([value, 'A', 'B', 'C', '"Testing"', "Here's a quote"])

        return response


def dashboard(request):
    if request.user.is_authenticated:
        reports = Report.objects.all()
        return render(request, "dashboard.html", {"username": request.user.username, "reports": reports})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User Successfully Logged Out')
    else:
        messages.add_message(request, messages.WARNING, 'No User Authenticated')
    return redirect('home')
