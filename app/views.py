import pytz
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from app.models import Report
from app.forms import ReportForm
from django import forms
import csv
from datetime import datetime
from app.decorators import allowed_users


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if "previous_page" in request.session:
                url = request.session['previous_page']
                del request.session['previous_page']
                return redirect(url)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'Invalid Credentials')
            return render(request, 'index.html')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'index.html')


@allowed_users(allowed_roles=["super_admins", "admins", "supervisors", "general_staff"])
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
                    # Check if the resident is in a Nursing Care community to indicate that a Physician must review
                    # the report
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
                    messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Saved')
                    return render(request, 'input_form.html', {"username": request.user.username})
                else:
                    messages.add_message(request, messages.WARNING, 'Error in Form')
                    return render(request, 'input_form.html', {"username": request.user.username})

        if 'report_data' in request.session:
            report = ReportForm(request.session['report_data'])
            report.full_clean()
            print(request.session['report_data']['staff'])
            del request.session['report_data']
            return render(request, 'input_form.html', {"username": request.user.username, "report": report})
        return render(request, 'input_form.html', {"username": request.user.username})
    else:
        request.session['previous_page'] = reverse("form")
        if request.method == 'POST':
            request.session['report_data'] = request.POST
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def read_report(request, report_id):
    if request.user.is_authenticated:
        if request.user.groups.exists():

            report_instance = Report.objects.get(id=report_id)
            report = ReportForm(request.POST, instance=report_instance)
            general_staff = 'general_staff'
            userr = User.objects.get(username=report_instance.reporter_account)

            if (userr.groups.all()[0].name == general_staff and request.user.groups.all()[
                0].name == general_staff and report_instance.report_status == 'PC') or \
                    (report_instance.report_status != 'CO' and request.user.groups.all()[0].name != general_staff and
                     request.user.groups.all()[0].name != 'physicians') or \
                    (request.user.groups.all()[0].name == 'physicians' and report_instance.report_status == "PP"):

                report = Report.objects.filter(id=report_id)[0]
                return render(request, "read_only_report.html",
                              {"username": request.user.username, "report_id": report_id, "report": report})
            else:
                return HttpResponse('You are not authorised')
        else:
            messages.add_message(request, messages.WARNING, 'No group assigned to user')
            return render(request, 'index.html')
    else:
        request.session['previous_page'] = reverse("read_report", kwargs={'report_id': report_id})
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def edit_report(request, report_id):
    if request.user.is_authenticated:
        report_instance = Report.objects.get(id=report_id)
        report = ReportForm(request.POST, instance=report_instance)
        general_staff = 'general_staff'
        userr = User.objects.get(username=report_instance.reporter_account)

        if request.user.groups.exists():
            if (userr.groups.all()[0].name == general_staff and request.user.groups.all()[
                0].name == general_staff and report_instance.report_status == 'PC') or \
                    (report_instance.report_status != 'CO' and request.user.groups.all()[0].name != general_staff and
                     request.user.groups.all()[0].name != 'physicians') or \
                    (request.user.groups.all()[0].name == 'physicians' and report_instance.report_status == "PP"):

                if request.method == "POST":
                    if request.POST['submit'] == 'submit':
                        report.full_clean()
                        report.validate()
                        if report.is_valid():
                            # Create an instance of the database object to add the report status to

                            report_data = report.save(commit=False)
                            # Check if the resident is in a Nursing Care community to indicate that a Physician must
                            # review the report
                            if 'NC' in report_data.community:
                                report_data.report_status = 'PP'
                            else:
                                report_data.report_status = 'SU'
                            # Adds the reporting accounts username to the data and saves the data to the database
                            report_data.save()
                            messages.add_message(request, messages.SUCCESS,
                                                 'Incident Report Form Successfully Submitted')
                            return redirect('dashboard')
                        else:
                            messages.add_message(request, messages.WARNING, 'Error in Form')
                            if request.user.groups.filter(name='physicians').exists():
                                return render(request, "physician_edit_report.html",
                                              {"username": request.user.username, "report": report})
                            return render(request, 'edit_report.html',
                                          {"username": request.user.username, "report": report})
                    elif request.POST['submit'] == "save":
                        if report.is_valid():
                            report_data = report.save(commit=False)
                            report_data.report_status = 'PC'
                            report_data.save()
                            messages.add_message(request, messages.SUCCESS, 'Incident Report Form Successfully Saved')
                            return redirect('read_report', report_id=report_id)
                        else:
                            messages.add_message(request, messages.WARNING, 'Error in Form')
                            if request.user.groups.filter(name='physicians').exists():
                                return render(request, "physician_edit_report.html",
                                              {"username": request.user.username, "report": report})
                            return render(request, 'edit_report.html',
                                          {"username": request.user.username, "report": report})

                else:
                    report = Report.objects.get(id=report_id)
                    if request.user.groups.filter(name='physicians').exists():
                        return render(request, "physician_edit_report.html",
                                      {"username": request.user.username, "report": report})
                    return render(request, "edit_report.html", {"username": request.user.username, "report": report})

            else:
                return HttpResponse('You are not authorised')
        else:
            messages.add_message(request, messages.WARNING, 'No group assigned to user')
            return render(request, 'index.html')
    else:
        if request.method == 'POST':
            request.session['report_data'] = request.POST
        request.session['previous_page'] = reverse("edit_report", kwargs={'report_id': report_id})
        messages.error(request, f'User is not authenticated')
        return redirect('home')


@allowed_users(allowed_roles=["super_admins", "admins"])
def dashboard_export(request):
    if request.user.is_authenticated:
        reports = Report.objects.all()
        displayReports = reports.reverse()[:50]
        return render(request, "dashboard-export.html",
                      {"username": request.user.username, "reports": displayReports, "count": displayReports.count()})
    else:
        request.session['previous_page'] = reverse("form")
        messages.error(request, f'User is not authenticated')
        return redirect('home')


@allowed_users(allowed_roles=["super_admins", "admins"])
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
        request.session['previous_page'] = reverse("read_report", kwargs={'report_id': report_id})
        messages.error(request, f'User is not authenticated')
        return redirect('home')


@allowed_users(allowed_roles=["physicians"])
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
        request.session['previous_page'] = reverse("read_report", kwargs={'report_id': report_id})
        messages.error(request, f'User is not authenticated')
        return redirect('home')


@allowed_users(allowed_roles=["super_admins", "admins"])
def export(request):
    if request.method == "GET" & request.user.is_authenticated:
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
            report_id = request.GET.get("reportID" + str(i))
            # report_id = int(report_id)
            if report_id != None:
                report = Report.objects.filter(id=report_id)[0]
                medication_error_reason = ""
                if report.medication_error:
                    if report.incorrect_resident:
                        medication_error_reason += "Incorrect Resident.\n"
                    if report.incorrect_route:
                        medication_error_reason += "Incorrect Route.\n"
                    if report.incorrect_dose:
                        medication_error_reason += "Incorrect Dose.\n"
                    if report.incorrect_label:
                        medication_error_reason += "Incorrect Label.\n"
                    if report.incorrect_name:
                        medication_error_reason += "Incorrect Name.\n"
                    if report.incorrect_time:
                        medication_error_reason += "Incorrect Time.\n"
                    if report.incorrect_drug:
                        medication_error_reason += "Incorrect Drug.\n"
                    if report.extra_dose_given:
                        medication_error_reason += "Extra Dose Given.\n"
                    if report.dose_omitted:
                        medication_error_reason += "Dose Omitted.\n"
                    if report.pharmacy_error:
                        medication_error_reason += "Pharmacy Error.\n"
                    if report.other_medication_error:
                        medication_error_reason += "Other Medication Error.\n"

                type_of_incident = ""
                if report.near_miss:
                    type_of_incident += "Near Miss\n"
                if report.fall:
                    type_of_incident += "Fall\n"
                if report.medication_error:
                    type_of_incident += "Medication Error\n"
                if report.treatment_error:
                    type_of_incident += "Treatment Error\n"
                if report.loss_of_property:
                    type_of_incident += "Loss of Property\n"
                if report.death:
                    type_of_incident += "Death\n"
                if report.other_type_of_incident:
                    type_of_incident += "Other Type of Incident\n"
                if report.staff_injury:
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

        return response
    else:
        request.session['previous_page'] = reverse("dashboard")
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.groups.exists():
            if request.user.groups.all()[0].name == 'general_staff':
                report = Report.objects.filter(report_status='PC', reporter_account=request.user.username)
                filter_selection = [[], [], [], [], [], [], [], []]
                return render(request, "dashboard.html", {"username": request.user.username, "reports": reports, "filter_selection": filter_selection})
            elif request.user.groups.all()[0].name == 'physicians':
                report = Report.objects.filter(report_status='PP')
                filter_selection = [[], [], [], [], [], [], [], []]
                return render(request, "dashboard.html", {"username": request.user.username, "reports": reports, "filter_selection": filter_selection})
            else:
                reports = Report.objects.all()filter_selection = [[], [], [], [], [], [], [], []]
                 return render(request, "dashboard.html", {"username": request.user.username, "reports": reports, "filter_selection": filter_selection})
        else:
            messages.add_message(request, messages.WARNING, 'No group assigned to user')
            return render(request, 'index.html')
    else:
        request.session['previous_page'] = reverse("dashboard")
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User Successfully Logged Out')
    else:
        messages.add_message(request, messages.WARNING, 'No User Authenticated')
    return redirect('home')


def dashboard_functionality(request):
    if request.method == "GET":
        if request.GET.get('submit') == "apply_filters":
            return dashboard_filtering(request)
    reports = Report.objects.all()
    filter_selection = [[], [], [], [], [], [], [], []]
    return render(request, "dashboard.html", {"username": request.user.username, "reports": reports[:50], "filter_selection": filter_selection})


def dashboard_filtering(request):
    # Get dropdown options
    location_options = request.GET.get('location_options_list').split('?')
    care_options = request.GET.get('care_options_list').split('?')
    status_options = request.GET.get('status_options_list').split('?')
    incident_options = request.GET.get('incident_options_list').split('?')
    # Get selected options
    location_selection = get_filter_selection(request, location_options)
    care_selection = get_filter_selection(request, care_options)
    status_selection = get_filter_selection(request, status_options)
    incident_selection = get_filter_selection(request, incident_options)
    reports_to_display = apply_filters(request, location_selection, care_selection, status_selection, incident_selection)
    print(str(len(status_selection)))
    filter_selection = [request.GET.get('residents_name'), [request.GET.get('date_from'), request.GET.get('date_to')], request.GET.get('reporter_name'), location_selection, care_selection, incident_selection, status_selection, request.GET.get('display_all_toggle')]
    print("filter_selection: " + str(len(filter_selection)))
    if request.GET.get('display_all_toggle') is not None:
        return render(request, "dashboard.html",
                      {"username": request.user.username, "reports": reports_to_display, "filter_selection": filter_selection})
    return render(request, "dashboard.html", {"username": request.user.username, "reports": reports_to_display[:50], "filter_selection": filter_selection})


def get_filter_selection(request, options):
    temp = []
    print(options[0])
    for x in options:
        print(request.GET.get(x))
        if request.GET.get(x) is not None:
            temp.append(x)
    #if len(temp) == 0:
    #    return options
    return temp


def apply_filters(request, location_selection, care_selection, status_selection, incident_selection):
    reports = Report.objects.all()
    results = []

    for x in reports:
        if resident_filter(x, request.GET.get('residents_name')) and reporter_filter(x, request.GET.get(
                'reporter_name')) and location_filter(x, location_selection) and care_filter(x, care_selection) and status_filter(x, status_selection) and incident_filter(x, incident_selection) and date_filter(x, request):
            results.append(x)
    return results


def location_filter(report, location_list):
    if len(location_list) == 0:
        return True
    for x in location_list:
        if x == report.incident_location:
            return True
    return False


def care_filter(report, care_list):
    if len(care_list) == 0:
        return True
    for x in care_list:
        if x == report.community:
            return True
    return False


def incident_filter(report, incident_list):
    if len(incident_list) == 0:
        print("empty incident list")
        return True
    if report.near_miss:
        for x in incident_list:
            if x == "Near Miss":
                return True
    if report.fall:
        for x in incident_list:
            if x == "Fall":
                return True
    if report.medication_error:
        for x in incident_list:
            if x == "Medication Error":
                return True
    if report.treatment_error:
        for x in incident_list:
            if x == "Treatment Error":
                return True
    if report.death:
        for x in incident_list:
            if x == "Death":
                return True
    if report.other_type_of_incident:
        for x in incident_list:
            if x == "Other":
                return True
    if report.staff_injury:
        for x in incident_list:
            if x == "Staff Injury":
                return True

    return False


def status_filter(report, status_list):
    if len(status_list) == 0:
        return True
    for x in status_list:
        if x == report.report_status:
            return True
    return False


def reporter_filter(report, query):
    if query == "":  # if this field hasn't been used just ignore it
        return True
    if report.name_of_writer.lower() == query.lower():
        return True
    if query.lower() in report.name_of_writer.lower():
        return True
    return False


def resident_filter(report, query):
    if query == "":  # if this field hasn't been used just ignore it
        return True
    if report.residents.lower() == query.lower():
        return True
    if query.lower() in report.residents.lower():
        return True
    return False


def date_filter(report, request):
    from_bool = False
    to_bool = False

    if request.GET.get('date_from') != "" and report.date_of_incident is not None:
        date_from = datetime.strptime(request.GET.get('date_from'), '%Y-%m-%d').replace(tzinfo=pytz.timezone('America/Halifax'))

        if report.date_of_incident > date_from:
            from_bool = True    #if date is after "from" date
    else:
        from_bool = True    #if no "from" date is selected then all are true

    if request.GET.get('date_to') != "":
        if report.date_of_incident is not None:
            date_to = datetime.strptime(request.GET.get('date_to'), '%Y-%m-%d').replace(tzinfo=pytz.timezone('America/Halifax'))
            if report.date_of_incident < date_to:
                to_bool = True  # if date is after "from" date
    else:
        to_bool = True  # if no "from" date is selected then all are true

    return from_bool and to_bool


@allowed_users(allowed_roles=["super_admins", "admins"])
def delete_report(request, report_id):
    if request.user.is_authenticated:
        report = Report.objects.get(id=report_id)
        report.delete()
        messages.success(request, "Report Deleted successfully!")
        return redirect('dashboard')
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')

