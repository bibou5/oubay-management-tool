from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('project-status-data/', views.project_status_data, name='project_status_data'),
]