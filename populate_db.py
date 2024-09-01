import os
import random
import sys
from datetime import timedelta

import django
from django.utils import timezone
from faker import Faker

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from departments.models import Department, Employee

fake = Faker()


def create_departments():
    departments = []
    department_names = {
        1: ["Главный офис", "Региональный офис"],
        2: ["Отдел продаж", "Отдел маркетинга", "Отдел разработки"],
        3: ["Сектор B2B", "Сектор B2C", "Сектор рекламы", "Поддержка"],
        4: ["Группа аналитиков", "Группа разработчиков", "Группа тестирования"],
        5: ["Команда проекта A", "Команда проекта B", "Команда проекта C"],
    }

    for level in range(1, 6):
        for name in department_names[level]:
            parent = random.choice(departments) if level > 1 else None
            dept = Department.objects.create(name=name, parent=parent)
            departments.append(dept)

    return departments


def get_department_level(department):
    level = 1
    while department.parent:
        level += 1
        department = department.parent
    return level


def get_position_and_salary(department_level):
    if department_level == 1:
        return "Директор", round(random.uniform(100000, 150000), 2)
    elif department_level == 2:
        return "Руководитель отдела", round(random.uniform(80000, 120000), 2)
    elif department_level == 3:
        return "Менеджер", round(random.uniform(60000, 90000), 2)
    elif department_level == 4:
        return "Старший специалист", round(random.uniform(40000, 60000), 2)
    else:
        return "Младший специалист", round(random.uniform(30000, 50000), 2)


def create_employees(departments):
    for i in range(50000):
        dept = random.choice(departments)
        department_level = get_department_level(dept)
        position, salary = get_position_and_salary(department_level)
        hire_date = timezone.now() - timedelta(days=random.randint(30, 3650))

        Employee.objects.create(
            full_name=fake.name(),
            position=position,
            hire_date=hire_date,
            salary=salary,
            department=dept,
        )


if __name__ == "__main__":
    print("Deleting old data...")
    Department.objects.all().delete()
    Employee.objects.all().delete()

    print("Creating departments...")
    departments = create_departments()

    print("Creating employees...")
    create_employees(departments)

    print("Data population complete.")
