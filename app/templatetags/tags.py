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
    for x in value:
        if x.incident_location not in temp:
            temp.append(x.incident_location)
            s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" value="' +  x.incident_location + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + x.incident_location + '\n</label>\n</div>\n')

    return mark_safe(s)


@register.filter(name="care_options")
def care_options(value):
    temp = []
    s = ""
    for x in value:
        if x.community not in temp:
            temp.append(x.community)
            s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" value="' + str(x.community) + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + str(x.community) + '\n</label>\n</div>\n')

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
            temp.append('Near Miss')
            break

    for x in value:
        if x.medication_error:
            temp.append('Near Miss')
            break

    for x in value:
        if x.treatment_error:
            temp.append('Near Miss')
            break


    for x in value:
        if x.death:
            temp.append('Near Miss')
            break

    for x in value:
        if x.other_type_of_incident:
            temp.append('Near Miss')
            break

    for x in value:
        if x.staff_injury:
            temp.append('Near Miss')
            break

    for x in temp:
        s = s + ('\n<div class="form-check" style="margin-left: 10px;">\n<input class="form-check-input" type="checkbox" value="' + str(x) + '" id="formCheck-8">\n<label class="form-check-label" for="formCheck-8">\n' + str(x) + '\n</label>\n</div>\n')

    return mark_safe(s)
