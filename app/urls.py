from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_export/', views.dashboard_export, name='dashboard_export'),
    path('csv_export/', views.csv_export, name='csv_export'),
    path('logout/', views.logout_view, name='logout'),
    path('read_report/<int:report_id>', views.read_report, name="read_report")

]
