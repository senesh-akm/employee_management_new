from django.shortcuts import render
from django.db.models import Count
from apps.emp_management.models import Employee
from apps.attendance_leave.models import Leave, Attendance
from apps.payroll_management.models import SalaryProcessing

def dashboard_view(request):
    total_employees = Employee.objects.count()
    total_departments = (
        Employee.objects.values('department')
        .annotate(department_count=Count('id'))
        .distinct()
        .count()
    )
    pending_leave_requests = Leave.objects.filter(approval_status="Pending").count()
    total_payrolls = SalaryProcessing.objects.count()

    employees = Employee.objects.all()
    attendance = [Attendance.objects.filter(employee=emp).count() for emp in employees]
    leaves = [Leave.objects.filter(employee=emp).count() for emp in employees]
    labels = [emp.full_name for emp in employees]

    context = {
        'statistics': {
            'total_employees': total_employees,
            'total_departments': total_departments,
            'pending_leave_requests': pending_leave_requests,
            'total_payrolls': total_payrolls,
        },
        'analytics': {
            'attendance': attendance,
            'leave': leaves,
            'labels': labels,
        },
        'quick_links': [
            {'name': 'Employees', 'url': 'employee_list', 'icon': 'bi-people-fill'},
            {'name': 'Attendance', 'url': 'attendance_list', 'icon': 'bi-calendar'},
            {'name': 'Payroll', 'url': 'payroll_generation_list', 'icon': 'bi-cash'},
            {'name': 'Leaves', 'url': 'leave_list', 'icon': 'bi-journal'},
        ],
    }
    return render(request, "dashboard.html", context)