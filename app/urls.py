from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_export/', views.dashboard_export, name='dashboard_export'),
    path('export/', views.export, name='export'),
    path('logout/', views.logout_view, name='logout'),
    path('read_report/<int:report_id>', views.read_report, name="read_report"),
    path('edit_report/<int:report_id>', views.edit_report, name="edit_report"),
    path('mark_complete/<int:report_id>', views.mark_report_complete, name="mark_complete"),
    path('sign_off/<int:report_id>', views.sign_off_report, name="sign_off")

]
