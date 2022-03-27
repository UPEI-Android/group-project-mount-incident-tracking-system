from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import Report
from app.forms import ReportForm
from django import forms
import csv


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
                    for error in report.errors:
                        print(error)
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
                    for error in report.errors:
                        print(error)
                    messages.add_message(request, messages.WARNING, 'Error in Form')
                    return render(request, 'input_form.html', {"username": request.user.username})

        return render(request, 'input_form.html', {"username": request.user.username})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def read_report(request, report_id):
    if request.user.is_authenticated:
        report = Report.objects.filter(id=report_id)[0]
        return render(request, "read_only_report.html", {"report_id": report_id, "report": report})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def edit_report(request, report_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            # TODO: Add functionality to save submitted and unfinished reports
            report = Report.objects.filter(id=report_id)[0]
            return render(request, "edit_report.html", {"report": report})
        else:
            report = Report.objects.filter(id=report_id)[0]
            return render(request, "edit_report.html", {"username": request.user.username, "report": report})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def dashboard_export(request):
    if request.user.is_authenticated:
        reports = Report.objects.all()
        return render(request, "dashboard-export.html", {"username": request.user.username, "reports": reports})
      
      
def mark_report_complete(request, report_id):
    if request.user.is_authenticated:
        report = Report.objects.filter(id=report_id)[0]
        if report.report_status == "SU":
            report.report_status = "CO"
            report.save()
        else:
            messages.error(request, f'Report cannot be marked as complete')
            return redirect('read_report', report_id=report_id)
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def sign_off_report(request, report_id):
      if request.user.is_authenticated:
        report = Report.objects.filter(id=report_id)[0]
        if report.report_status == "PP":
            report.report_status = "SU"
            report.save()
        else:
            messages.error(request, f'Cannot sign off on report')
            return redirect('read_report', report_id=report_id)
      else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')
      
      
def csv_export(request):
    if request.POST:
        #this_form = request.POST.form
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="Reports.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        #for key, value in this_form.cleaned_data.iteritems():
            #writer.writerow([value, 'A', 'B', 'C', '"Testing"', "Here's a quote"])
        #if this_form.is_valid():

        return response
    return redirect('form')



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
