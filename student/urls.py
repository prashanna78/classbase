from django.urls import path

from student.models import Student
from .import views
from student.views import (RegisterList, StudentRegister,StudentDelete,  StudentList, StudentUpdate , DeleteView, SchoolCreate,SchoolDelete, SchoolList, SchoolUpdate)

app_name = 'student'

urlpatterns = [

    path('', StudentList.as_view(), name='list'),
    path('register/', RegisterList.as_view(), name='register'),
    path('studentregister/', StudentRegister.as_view(), name='student-registers'),
    path('student/delete/<int:pk>/', StudentDelete.as_view(), name = 'student-delete'),
    path('student/update/<int:pk>/', StudentUpdate.as_view(), name = 'student-update' ),
    

    path('school/create', SchoolCreate.as_view(), name = 'school-create'),
    path('school/list', SchoolList.as_view(), name = 'school-list'  ),
    path('school/delete/<int:pk>/', SchoolDelete.as_view, name = 'school-delete'),
    path('school/update/<int:pk>/', SchoolUpdate.as_view, name = 'school-update')
     
]