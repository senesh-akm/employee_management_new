from django.contrib import admin
from .models import PerformanceReview, GoalSetting, FeedbackMechanism

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "review_text", 
        "appraisal_text", 
    )
    search_fields = ("employee__full_name", "review_text")
    list_filter = ("employee",)
    ordering = ("-employee",)
    fieldsets = (
        ("Employee Information", {"fields": ["employee"]}),
        ("Review Details", {"fields": ["review_text", "appraisal_text"]}),
    )

@admin.register(GoalSetting)
class GoalSettingAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "goals", 
    )
    search_fields = ("employee__full_name", "goals")
    list_filter = ("employee",)
    ordering = ("-employee",)
    fieldsets = (
        ("Employee Information", {"fields": ["employee"]}),
        ("Goals", {"fields": ["goals"]}),
    )

@admin.register(FeedbackMechanism)
class FeedbackMechanismAdmin(admin.ModelAdmin):
    list_display = (
        "employee", 
        "feedback", 
    )
    search_fields = ("employee__full_name", "feedback")
    list_filter = ("employee",)
    ordering = ("-employee",)
    fieldsets = (
        ("Employee Information", {"fields": ["employee"]}),
        ("Feedback Details", {"fields": ["feedback"]}),
    )