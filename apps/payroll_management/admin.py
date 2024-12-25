from django.contrib import admin
from .models import SalaryProcessing, PayrollGeneration, TaxManagement


@admin.register(SalaryProcessing)
class SalaryProcessingAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "salary", 
        "deduction", 
        "taxes", 
        "no_pay", 
        "days", 
        "payment", 
        "status"
    )
    search_fields = ("employee__full_name", "status")
    list_filter = ("status",)
    ordering = ("-id",)
    fieldsets = (
        ("Employee Information", {"fields": ["employee"]}),
        ("Salary Details", {
            "fields": [
                "salary", 
                "deduction", 
                "taxes", 
                "no_pay", 
                "days", 
                "payment", 
                "status"
            ]
        }),
    )

@admin.register(PayrollGeneration)
class PayrollGenerationAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "salary_processing", 
        "issued"
    )
    search_fields = ("employee__full_name", "salary_processing__id")
    list_filter = ("issued",)
    ordering = ("-id",)
    fieldsets = (
        ("Payroll Information", {"fields": ["employee", "salary_processing"]}),
        ("Status", {"fields": ["issued"]}),
    )

@admin.register(TaxManagement)
class TaxManagementAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "income_tax", 
        "social_security", 
        "other_taxes"
    )
    search_fields = ("employee__full_name",)
    ordering = ("-id",)
    fieldsets = (
        ("Employee Information", {"fields": ["employee"]}),
        ("Tax Details", {
            "fields": [
                "income_tax", 
                "social_security", 
                "other_taxes"
            ]
        }),
    )