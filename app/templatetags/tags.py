from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="index_finder")
def index_finder(reports, report):
    temp = 0
    print("Report ID: " + str(report.id))
    for x in reports:
        print("Report List IDs: " + str(x.id))
        if(report.id == x.id):
            print("Found, Temp: " + str(temp))
            return temp
        temp += 1
    return 0


@register.filter(name="location_options")
def location_options(value):
    temp = []
    s = ""
    options = ""
    for x in value:
        if x.incident_location not in temp:
            temp.append(x.incident_location)
            options = options + x.incident_location + "?" #'?' is being used as a delimiter that I know won't be picked up by the HTML
            s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" name="' + x.incident_location + '" value="' +  x.incident_location + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + x.incident_location + '\n</label>\n</div>\n')
    s = s + '<input type="hidden" name="location_options_list" value="' + options[:-1] + '"></input>\n'   #drops the extra delimiter from the end of the string

    return mark_safe(s)


@register.filter(name="care_options")
def care_options(value):
    temp = []
    s = ""
    options = ""
    for x in value:
        if x.community not in temp:
            temp.append(x.community)
            s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" name="' + x.community + '" value="' + str(x.community) + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + str(x.community) + '\n</label>\n</div>\n')
            options = options + x.community + "?"
    s = s + '<input type="hidden" name="care_options_list" value="' + options[:-1] + '"></input>\n'
    return mark_safe(s)


@register.filter(name="report_status")
def report_status(value):
    temp = []
    s = ""
    options = ""
    for x in value:
        if x.report_status not in temp:
            temp.append(x.report_status)
            s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" name="' + x.report_status + '" value="' + str(x.report_status) + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + str(x.report_status) + '\n</label>\n</div>\n')
            options = options + x.report_status + "?"
    s = s + '<input type="hidden" name="status_options_list" value="' + options[:-1] + '"></input>\n'
    return mark_safe(s)


@register.filter(name="incident_options")
def incident_options(value):
    temp = []
    s = ""
    for x in value:
        if x.near_miss:
            temp.append('Near Miss')
            break
    for x in value:
        if x.fall:
            temp.append('Fall')
            break

    for x in value:
        if x.medication_error:
            temp.append('Medication Error')
            break

    for x in value:
        if x.treatment_error:
            temp.append('Treatment Error')
            break


    for x in value:
        if x.death:
            temp.append('Death')
            break

    for x in value:
        if x.other_type_of_incident:
            temp.append('Other')
            break

    for x in value:
        if x.staff_injury:
            temp.append('Staff Injury')
            break
    options = ""
    for x in temp:
        s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" value="' + str(x) + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + str(x) + '\n</label>\n</div>\n')
        options = options + str(x) + "?"
    s = s + '<input type="hidden" name="incident_options_list" value="' + options[:-1] + '"></input>\n'
    return mark_safe(s)
