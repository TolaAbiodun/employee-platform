from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from employee import views
  
urlpatterns = [
    path('employees/', views.employees_list, name='employees'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

]
  
urlpatterns = format_suffix_patterns(urlpatterns)
