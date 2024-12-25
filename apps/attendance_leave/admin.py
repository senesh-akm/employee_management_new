from django.contrib import admin
from .models import Leave, Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "date", 
        "check_in", 
        "check_out", 
        "work_hours", 
        "overtime", 
        "status"
    )
    search_fields = ("employee__full_name", "date", "status")
    list_filter = ("status", "date")
    date_hierarchy = "date"
    ordering = ("-date",)

    fieldsets = (
        ("Employee Information", {
            "fields": ["employee"]
        }),
        ("Attendance Details", {
            "fields": ["date", "check_in", "check_out", "work_hours", "overtime", "status"]
        }),
    )


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "leave_type", 
        "from_date", 
        "to_date", 
        "leave_balance", 
        "approval_status",
    )
    search_fields = ("employee__full_name", "leave_type", "approval_status")
    list_filter = ("leave_type", "approval_status", "from_date")
    date_hierarchy = "from_date"
    ordering = ("-from_date",)

    fieldsets = (
        ("Employee Information", {
            "fields": ["employee"]
        }),
        ("Leave Details", {
            "fields": ["leave_type", "leave_count", "used_leave", "leave_balance", "from_date", "to_date"]
        }),
        ("Approval and Reason", {
            "fields": ["approval_status", "reason"]
        }),
    )