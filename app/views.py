from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.forms import ReportForm


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
                #Save Model without checking for empty fields
                print("save")

        return render(request, 'input_form.html', {"username": request.user.username})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
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
