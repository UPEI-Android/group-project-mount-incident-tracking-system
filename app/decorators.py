from django.http import HttpResponse
from app.models import Report
from app.forms import ReportForm
from django.contrib.auth.models import User

from django.http import HttpResponse


def allowed_users(allowed_roles={""}):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            count = 0

            name = request.user.username
            all_users = User.objects.all()

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            print(group)

            for report in Report.objects.all():

                while count < 3:

                    print('hello')

                count = count + 1

            # print(allowed_roles)
            # print(count)

            # if (str(all_users[count]) == report.reporter_account) and ((all_users[count]).groups.all()[0].name == group):

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse('You are not authorised')

        return wrapper_func

    return decorator
