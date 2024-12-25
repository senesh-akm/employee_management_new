from django.contrib import admin
from .models import TrainingNeedsAssessment, TrainingPlan, TrainingRecord


@admin.register(TrainingNeedsAssessment)
class TrainingNeedsAssessmentAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "designation", "duration")
    search_fields = ("employee__full_name", "designation", "duration")
    list_filter = ("duration",)
    ordering = ("employee__full_name",)

    def employee_name(self, obj):
        """Returns the employee's full name."""
        return obj.employee.full_name

    employee_name.short_description = "Employee Name"


@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "plan_preview")
    search_fields = ("employee__full_name", "plan")
    ordering = ("employee__full_name",)

    def employee_name(self, obj):
        """Returns the employee's full name."""
        return obj.employee.full_name

    def plan_preview(self, obj):
        """Returns a short preview of the training plan."""
        return obj.plan[:50] + "..." if len(obj.plan) > 50 else obj.plan

    employee_name.short_description = "Employee Name"
    plan_preview.short_description = "Plan Preview"


@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "month", "training_record", "certificate_status", "description_preview")
    search_fields = ("employee__full_name", "description")
    list_filter = ("month", "training_record", "certificate")
    ordering = ("employee__full_name", "month")

    def employee_name(self, obj):
        """Returns the employee's full name."""
        return obj.employee.full_name

    def certificate_status(self, obj):
        """Displays a yes/no for the certificate."""
        return "Yes" if obj.certificate else "No"

    def description_preview(self, obj):
        """Returns a short preview of the description."""
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    employee_name.short_description = "Employee Name"
    certificate_status.short_description = "Certificate"
    description_preview.short_description = "Description Preview"