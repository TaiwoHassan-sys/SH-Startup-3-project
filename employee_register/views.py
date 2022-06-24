from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee, Vacation
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer,EmployeeSerializer,VacationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

# Create your views here.
# Employee Viewset
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # AllowAny means any users can access the data
    # IsAuthenticatedOrReadOnly means only authenticated users can access the data


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]



class VacationModelViewSet(ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
    permission_classes = [AllowAny]


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id):
    if request.method == "GET":
        if id == None:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')



def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
