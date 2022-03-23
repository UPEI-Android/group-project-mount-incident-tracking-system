from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submit_report, name='submit'),
    path('read_report/<int:report_id>', views.read_report, name="read_report")

]
