from django.db import models
from apps.emp_management.models import Employee

class SalaryProcessing(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="salary_processings")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deduction = models.TextField()
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)  # Paid (True) or Not Paid (False)
    no_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Salary Processing - {self.employee.full_name}"
    

class PayrollGeneration(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="payrolls")
    salary_processing = models.ForeignKey(SalaryProcessing, on_delete=models.CASCADE, related_name="payrolls")
    issued = models.BooleanField(default=False)  # Issued (True) or Not Issued (False)

    def __str__(self):
        return f"Payroll for {self.employee.full_name} - {'Issued' if self.issued else 'Not Issued'}"
    

class TaxManagement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="taxes")
    income_tax = models.DecimalField(max_digits=3, decimal_places=2)
    social_security = models.TextField()
    other_taxes = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"Tax Management - {self.employee.full_name}"