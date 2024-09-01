from django.shortcuts import render

from .models import Department


def department_tree(request):
    departments = Department.objects.filter(parent__isnull=True)
    return render(request, "departments/tree.html", {"departments": departments})
