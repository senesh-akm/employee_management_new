from django.contrib import admin
from .models import JobPosting, CandidateScreening, OnboardingProcess


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title", "work_type", "employee_type", "description_preview")
    search_fields = ("title", "description", "requirements", "responsibilities")
    list_filter = ("work_type", "employee_type")
    ordering = ("title",)

    def description_preview(self, obj):
        """Returns a short preview of the description."""
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    description_preview.short_description = "Description Preview"


@admin.register(CandidateScreening)
class CandidateScreeningAdmin(admin.ModelAdmin):
    list_display = ("candidate", "job_position", "members_preview", "conduct_interviews")
    search_fields = ("candidate", "job_position__title", "members")
    list_filter = ("job_position",)
    ordering = ("candidate",)

    def members_preview(self, obj):
        """Returns a short preview of members."""
        return obj.members[:50] + "..." if len(obj.members) > 50 else obj.members

    members_preview.short_description = "Members Preview"


@admin.register(OnboardingProcess)
class OnboardingProcessAdmin(admin.ModelAdmin):
    list_display = ("candidate_name", "designation", "joining_date", "offer_letter_preview")
    search_fields = ("candidate__candidate", "designation")
    list_filter = ("joining_date",)
    ordering = ("joining_date",)

    def candidate_name(self, obj):
        """Returns the name of the candidate from the CandidateScreening model."""
        return obj.candidate.candidate

    def offer_letter_preview(self, obj):
        """Returns a short preview of the offer letter."""
        return obj.offer_letter[:50] + "..." if len(obj.offer_letter) > 50 else obj.offer_letter

    candidate_name.short_description = "Candidate Name"
    offer_letter_preview.short_description = "Offer Letter Preview"