from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.template import loader


from myapp.forms import EmployeeForm
from myapp.models import Employee
# Create your views here.

#temp=loader.get_template('index.html')
#return HttpResponse(temp.render(data))



def emp(request):
    if request.method == "GET":
        form = EmployeeForm(request.GET)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = EmployeeForm()
        temp=loader.get_template('index.html')
        return HttpResponse(temp.render({'form':form}))


def show(request):
    employees = Employee.objects.all()
    temp=loader.get_template('show.html')
    return HttpResponse(temp.render({'employees':employees}))


def edit(request, id):
    employee = Employee.objects.get(id=id)
    temp=loader.get_template('edit.html')
    return HttpResponse(temp.render({'employee':employee}))


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.GET, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    temp=loader.get_template('edit.html')
    return HttpResponse(temp.render({'employees':id}))

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def __str__(self):
    return self.id






