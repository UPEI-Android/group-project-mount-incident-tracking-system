from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_export/', views.dashboard_export, name='dashboard_export'),
    path('dashboard_export_func/', views.dashboard_export_func, name='dashboard_export_func'),
    path('dashboard_functionality/', views.dashboard_functionality, name='dashboard_functionality'),
    path('logout/', views.logout_view, name='logout'),
    path('read_report/<int:report_id>', views.read_report, name="read_report"),
    path('edit_report/<int:report_id>', views.edit_report, name="edit_report"),
    path('mark_complete/<int:report_id>', views.mark_report_complete, name="mark_complete"),
    path('sign_off/<int:report_id>', views.sign_off_report, name="sign_off"),
    path('delete_report/<int:report_id>', views.delete_report, name="delete_report")

]
