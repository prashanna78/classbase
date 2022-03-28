from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


from django.db.models import Q
from .models import Student , School
from .forms import RegisterUser, StudentForm, SchoolForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class RegisterList(SuccessMessageMixin, CreateView):
    template_name ='student/StudentRegistration.html'
    form_class = RegisterUser
    success_url ='/'
    success_message = 'Your Accounts has been created'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class StudentRegister(SuccessMessageMixin,CreateView):
    template_name = 'student/student.html'
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
    template_name = 'student/student_list.html'
    model = Student
    context_object_name = 'student_list'
    paginate_by = 2

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.GET.get('search_query')
        
        if query:
            student_list= self.model.objects.filter(

                Q(name__icontains = query)|
                Q(address__icontains = query)
            ) 
            
        else:
            student_list = queryset

        return student_list


class StudentDelete(DeleteView):
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('student:list')
    sucess_message = ("student info is deleted")
    model = Student

class StudentUpdate(SuccessMessageMixin,UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student/update.html"
    success_url = reverse_lazy('student:list')
    success_message = ("student info is updated")
   
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form) 



class SchoolCreate(SuccessMessageMixin, CreateView):
    template_name = 'school/school_regestration.html'
    model = School
    form_class = SchoolForm
    success_url = reverse_lazy('student:school-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)

    #     if form.is_valid():
    #         form.save()
    #         return self.form_valid()
    #     else:
    #         return self.form_invalid()


    def get_success_message(self, cleaned_data):
        return self.get_success_message % cleaned_data

class SchoolList(ListView):
    template_name = 'school/school_list.html'
    model = School
    success_url = 'student:school-list' 

class SchoolDelete(DeleteView):
    template_name = 'school/school_delete.html'
    success_url = reverse_lazy('student:school-list')
    success_message = ("school info is deleted")
    model = School


class SchoolUpdate(UpdateView):
    model = School
    form_class = StudentForm
    template_name = 'school/school_update.htmnl'
    success_url = reverse_lazy('student:school-list')
    success_message = ("school info is updated")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self, **kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id = id)
