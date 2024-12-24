from django.contrib import admin
from .models import Employee, Education, WorkHistory

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    can_delete = True

class WorkHistoryInline(admin.TabularInline):
    model = WorkHistory
    extra = 1
    can_delete = True

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "department", "job_title", "contact_number", "email")
    search_fields = ("full_name", "department", "job_title")
    list_filter = ("department", "job_title")

    inlines = [EducationInline, WorkHistoryInline]

    fieldsets = (
        ("Personal Information", {
            "fields": ["title", "full_name", "dob", "nic", "address", "contact_number", "email", "emergency_person", "emergency_contact"]
        }),
        ("Professional Information", {
            "fields": ["job_number", "job_title", "department", "designation", "date_of_joining", "salary", "skills", "immediate_supervisor"]
        }),
        ("Login Information", {
            "fields": ["username", "password"]
        }),
        ("Financial Information", {
            "fields": ["bank", "account_number", "account_holder", "bank_code", "branch_code", "swift_code"]
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "institute", "employee")
    search_fields = ("title", "institute", "employee__full_name")
    list_filter = ("institute",)

@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "employee")
    search_fields = ("position", "company", "employee__full_name")
    list_filter = ("company",)