from django.urls import path

from student.models import Student
from .import views
from student.views import RegisterList, StudentRegister,StudentDelete,  StudentList, StudentUpdate , DeleteView

app_name = 'student'

urlpatterns = [

    path('', StudentList.as_view(), name='list'),
    path('register/', RegisterList.as_view(), name='register'),
    path('studentregister/', StudentRegister.as_view(), name='registers'),
    path('studentdelete/<int:pk>/', StudentDelete.as_view(), name = 'delete'),
    path('studentupdate/<int:pk>/', StudentUpdate.as_view(), name = 'update' ),
    
]