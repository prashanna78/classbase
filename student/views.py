
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


from django.db.models import Q
import student
from .models import Student
from .forms import RegisterUser, StudentForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class RegisterList(SuccessMessageMixin, CreateView):
    template_name ='school/StudentRegistration.html'
    form_class = RegisterUser
    success_url ='/'
    success_message = 'Your Accounts has been created'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class StudentRegister(SuccessMessageMixin,CreateView):
    template_name = 'school/student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student:registers')
    success_message = 'student info has been created'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class StudentList(ListView):
    template_name = 'school/student_list.html'
    model = Student
    context_object_name = 'student_list'

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.GET.get('d')
        
        if query:
            student_list= self.model.objects.filter(

                Q(name__icontains = query)|
                Q(address__icontains = query)
            )
            
        else:
            student_list = queryset

        return student_list
   
  


class StudentDelete(DeleteView):
    template_name = 'school/student_delete.html'
    success_url = reverse_lazy('student:list')
    sucess_message = ("student info is deleted")
    model = Student

    
   
class StudentUpdate(SuccessMessageMixin,UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "school/update.html"
    success_url = reverse_lazy('student:list')
    success_message = ("student info is updated")
   

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form) 



