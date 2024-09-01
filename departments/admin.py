from django.contrib import admin

from .models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "hire_date", "salary", "department")
    list_filter = ("department",)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
