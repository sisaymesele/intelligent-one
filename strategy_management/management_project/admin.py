from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from management_project.models import (
    OrganizationalProfile, SwotAnalysis, Vision, Mission, Values, StrategyHierarchy,
    Stakeholder, StrategicCycle, StrategicActionPlan, StrategicReport, SwotReport, InitiativePlanning,
    InitiativeReport, InitiativeResourceItemReport, InitiativeResourceItemPlan
)
from management_project.forms import (
    OrganizationalProfileForm, SwotAnalysisForm, VisionForm, MissionForm, ValuesForm,
    StrategyHierarchyForm, StakeholderForm, StrategicCycleForm, StrategicActionPlanForm,
    StrategicReportForm, SwotReportForm, InitiativePlanningForm, InitiativeReportForm,
    InitiativeResourceItemReportForm, InitiativeResourceItemPlanForm
)

# Register your models here.
@admin.register(OrganizationalProfile)
class OrganizationalProfileAdmin(admin.ModelAdmin):
    form = OrganizationalProfileForm
    list_display = (
        'organization_name', 'organization_type', 'organization_address', 'employer_tin',
        'sector_name', 'contact_personnel', 'owner'
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(
                organization_name=request.user.organization_name
            )
        return qs.none()

@admin.register(SwotAnalysis)
class SwotAnalysisAdmin(admin.ModelAdmin):
    form = SwotAnalysisForm
    list_display = (
        'organization_name', 'swot_type', 'swot_pillar', 'swot_factor', 'priority',
        'impact', 'likelihood', 'created_at',
    )
    list_filter = ('swot_type', 'priority', 'impact', 'likelihood', 'organization_name')
    search_fields = ('swot_pillar', 'swot_factor', 'description')

    # Restrict foreign key choices based on logged-in user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                kwargs['queryset'] = OrganizationalProfile.objects.filter(
                    pk=request.user.organization_name.pk
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict queryset so non-superusers only see their org's data
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    form = VisionForm

    # Display these fields in the list view
    list_display = ('organization_name', 'vision_statement')

    # Filter foreign key based on user (non-superuser sees only their organization)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                kwargs["queryset"] = OrganizationalProfile.objects.filter(
                    pk=request.user.organization_name.pk
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Filter the queryset in the admin list view
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    form = MissionForm

    # Display these fields in the list view
    list_display = ('organization_name', 'mission_statement')

    # Filter foreign key based on user (non-superuser sees only their organization)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                kwargs["queryset"] = OrganizationalProfile.objects.filter(
                    pk=request.user.organization_name.pk
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Filter the queryset in the admin list view
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


@admin.register(Values)
class ValuesAdmin(admin.ModelAdmin):
    form = ValuesForm

    # Display these fields in the list view
    list_display = ('organization_name', 'values', 'get_category')

    # Filter foreign key based on user (non-superuser sees only their organization)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                kwargs["queryset"] = OrganizationalProfile.objects.filter(
                    pk=request.user.organization_name.pk
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Filter the queryset in the admin list view
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()




@admin.register(StrategyHierarchy)
class StrategyHierarchyAdmin(admin.ModelAdmin):
    form = StrategyHierarchyForm

    list_display = (
        'organization_name', 'strategic_perspective', 'focus_area', 'objective', 'kpi', 'formula',
    )
    list_filter = ('strategic_perspective', 'focus_area', 'organization_name')
    search_fields = ('objective', 'kpi', 'formula')

    # Restrict foreign key choices based on logged-in user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                kwargs['queryset'] = OrganizationalProfile.objects.filter(
                    pk=request.user.organization_name.pk
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict queryset so non-superusers only see their org's data
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()



@admin.register(Stakeholder)
class StakeholderAdmin(admin.ModelAdmin):
    form = StakeholderForm

    # Fields to display in the list view
    list_display = (
        'organization_name', 'stakeholder_name', 'role', 'stakeholder_type',
        'impact_level', 'interest_level', 'engagement_strategy',
        'priority', 'satisfaction_level', 'risk_level', 'influence_score'
    )

    # Fields to exclude from the admin form
    exclude = ('priority', 'contribution_score', 'depends_on')

    # Fields that can be searched
    search_fields = ('stakeholder_name', 'organization_name__organization_name', 'department')

    # Filtering options in admin sidebar
    list_filter = ('stakeholder_type', 'role', 'impact_level', 'interest_level', 'satisfaction_level', 'risk_level')

    # Auto-filter based on user's organization (if not superuser)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                org = request.user.organization_name
                kwargs["queryset"] = OrganizationalProfile.objects.filter(pk=org.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Limit queryset for non-superusers to their organization
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


@admin.register(StrategicCycle)
class StrategicCycleAdmin(admin.ModelAdmin):
    form = StrategicCycleForm

    # Display model fields
    list_display = [
        'organization_name', 'time_horizon', 'time_horizon_type',
        'start_date', 'end_date', 'duration_days', 'slug'
    ]

    # Filters
    list_filter = ['organization_name', 'time_horizon_type', 'time_horizon']
    search_fields = ['time_horizon', 'slug']
    ordering = ['-start_date']

    readonly_fields = ['slug']

    # Restrict foreign keys based on user's organization
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                org = request.user.organization_name
                kwargs['queryset'] = OrganizationalProfile.objects.filter(pk=org.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict queryset to user's organization
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()

# #
@admin.register(StrategicActionPlan)
class StrategicActionPlanAdmin(admin.ModelAdmin):
    form = StrategicActionPlanForm
    list_display = ['organization_name', 'get_perspective', 'get_pillar', 'get_objective', 'get_kpi', 'get_formula',
                    'indicator_type', 'direction_of_change', 'baseline', 'target', 'improvement_needed', 'get_time_horizon',
                    'get_time_horizon_type', 'get_start_date', 'get_end_date', 'get_duration_days',
                    'get_responsible_bodies', 'status', 'weight',]

    # Custom display methods
    def get_perspective(self, obj):
        return obj.strategy_hierarchy.strategic_perspective

    get_perspective.short_description = "Perspective"

    def get_pillar(self, obj):
        return obj.strategy_hierarchy.focus_area

    get_pillar.short_description = "Pillar"

    def get_objective(self, obj):
        return obj.strategy_hierarchy.objective

    get_objective.short_description = "Objective"

    def get_kpi(self, obj):
        return obj.strategy_hierarchy.kpi

    get_kpi.short_description = "KPI"

    def get_formula(self, obj):
        return obj.strategy_hierarchy.formula

    get_formula.short_description = "Formula"

    def get_time_horizon(self, obj):
        return obj.strategic_cycle.time_horizon

    get_time_horizon.short_description = "Time Horizon"

    def get_time_horizon_type(self, obj):
        return obj.strategic_cycle.time_horizon_type

    get_time_horizon_type.short_description = "Horizon Type"

    def get_start_date(self, obj):
        return obj.strategic_cycle.start_date

    get_start_date.short_description = "Start Date"

    def get_end_date(self, obj):
        return obj.strategic_cycle.end_date

    get_end_date.short_description = "End Date"

    def get_duration_days(self, obj):
        return obj.strategic_cycle.duration_days

    get_duration_days.short_description = "Duration (Days)"

    def get_responsible_bodies(self, obj):
        return ", ".join([body.stakeholder_name for body in obj.responsible_bodies.all()])

    get_responsible_bodies.short_description = "Responsible Bodies"

    list_filter = ['organization_name', 'strategic_cycle', 'strategy_hierarchy', 'indicator_type', 'direction_of_change']

    search_fields = [
        'key_performance_indicator',
        'strategy_hierarchy__objective',
        'strategy_hierarchy__kpi'
    ]

    filter_horizontal = ('responsible_bodies',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and hasattr(request.user, 'organization_name'):
            org = request.user.organization_name
            if db_field.name == 'organization_name':
                kwargs["queryset"] = OrganizationalProfile.objects.filter(organization_name=org)
            if db_field.name == 'strategic_cycle':
                kwargs["queryset"] = StrategicCycle.objects.filter(organization_name=org)
            if db_field.name == 'strategy_hierarchy':
                kwargs["queryset"] = StrategyHierarchy.objects.filter(organization_name=org)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form_kwargs(self, request, obj=None, **kwargs):
        form_kwargs = super().get_form_kwargs(request, obj, **kwargs)
        form_kwargs["request"] = request
        return form_kwargs

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


@admin.register(StrategicReport)
class StrategicReportAdmin(admin.ModelAdmin):
    form = StrategicReportForm
    list_display = (
        'organization_name', 'action_plan', 'achievement', 'percent_achieved', 'variance', 'weighted_score',
        'data_source', 'data_collector', 'progress_summary', 'performance_summary',
        'challenges', 'successes', 'lessons_learned', 'status', 'created_at', 'updated_at',
    )

    list_filter = ('action_plan', 'organization_name',)
    search_fields = ('action_plan__strategy_hierarchy__key_performance_indicator', 'responsible_body', 'organization_name__organization_name')
    ordering = ('-created_at',)

    readonly_fields = ( 'percent_achieved', 'variance', 'weighted_score', 'created_at', 'updated_at',)

    # Filter foreign keys based on user organization
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and hasattr(request.user, 'organization_name'):
            org = request.user.organization_name
            if db_field.name == 'organization_name':
                kwargs["queryset"] = OrganizationalProfile.objects.filter(id=org.id)
            if db_field.name == 'action_plan':
                kwargs["queryset"] = StrategicActionPlan.objects.filter(organization_name=org)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form_kwargs(self, request, obj=None, **kwargs):
        form_kwargs = super().get_form_kwargs(request, obj, **kwargs)
        form_kwargs["request"] = request
        return form_kwargs

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


# -------------------------------
# SwotReport Admin
# -------------------------------
@admin.register(SwotReport)
class SwotReportAdmin(admin.ModelAdmin):
    form = SwotReportForm

    list_display = (
        'organization_name', 'strategic_report_period', 'swot_type', 'swot_pillar', 'swot_factor',
        'priority', 'impact', 'likelihood', 'description', 'created_at', 'updated_at'
    )

    list_filter = ('swot_type', 'swot_pillar', 'priority', 'impact')
    search_fields = (
        'strategic_report_period__action_plan__strategy_hierarchy__key_performance_indicator',
        'swot_factor', 'description'
    )
    ordering = ('-strategic_report_period__created_at',)
    readonly_fields = ('created_at', 'updated_at')

    # Pass request to the form
    def get_form_kwargs(self, request, obj=None, **kwargs):
        form_kwargs = super().get_form_kwargs(request, obj, **kwargs)
        form_kwargs['request'] = request  # Pass request to the form for filtering
        return form_kwargs

    # Filter foreign key dropdowns by user's organization
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and hasattr(request.user, 'organization_name'):
            org = request.user.organization_name

            if db_field.name == 'strategic_report_period':
                kwargs['queryset'] = StrategicReport.objects.filter(organization_name=org)

            elif db_field.name == 'organization_name':
                kwargs['queryset'] = OrganizationalProfile.objects.filter(pk=org.pk)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Filter admin list view by user's organization
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()


@admin.register(InitiativePlanning)
class InitiativePlanningAdmin(admin.ModelAdmin):
    form = InitiativePlanningForm

    # Fields to display in the list view
    list_display = [
        'initiative_focus_area', 'initiative_dimension', 'initiative_name',
        'description', 'total_budget_planned', 'total_hr_planned', 'priority', 'impact',
        'likelihood', 'risk_level', 'baseline_status', 'target_status',
        'start_date', 'end_date',
    ]

    list_filter = [
        'organization_name', 'initiative_focus_area', 'initiative_dimension',
        'priority', 'impact', 'likelihood', 'risk_level',
    ]
    search_fields = ['initiative_name', 'description']
    ordering = ['-created_at']

    # Filter foreign keys based on logged-in user's organization
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and hasattr(request.user, 'organization_name'):
            org = request.user.organization_name
            if db_field.name == 'organization_name':
                kwargs['queryset'] = OrganizationalProfile.objects.filter(pk=org.pk)
            elif db_field.name == 'aligned_objectives':
                kwargs['queryset'] = StrategyHierarchy.objects.filter(organization_name=org)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict queryset to user's organization
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()

    # Pass request to the form
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request
        return form

    # Auto-assign organization on save
    def save_model(self, request, obj, form, change):
        if not change and hasattr(request.user, 'organization_name'):
            obj.organization_name = request.user.organization_name
        super().save_model(request, obj, form, change)

#
@admin.register(InitiativeReport)
class InitiativeReportAdmin(admin.ModelAdmin):
    form = InitiativeReportForm

    # Display all relevant fields including calculated ones
    list_display = [
        'initiative_planning', 'report_date', 'achieved_status', 'total_budget_spent_display',
        'budget_remaining_display', 'budget_utilization_percent_display', 'total_actual_hr_display',
        'remaining_hr_display', 'remaining_days', 'remaining_months', 'status_achievement_percent_display',
        'created_at', 'updated_at',
    ]

    list_filter = [
        'initiative_planning',
        'achieved_status',
        'report_date',
    ]
    search_fields = [
        'initiative_planning__initiative_name',
        'notes',
    ]
    ordering = ['-report_date']

    readonly_fields = [
        'budget_remaining_display', 'budget_utilization_percent_display', 'remaining_hr_display',
        'total_actual_hr_display', 'remaining_days', 'remaining_months', 'status_achievement_percent_display',
        'created_at', 'updated_at',
    ]

    # ===== Display methods =====
    def total_budget_spent_display(self, obj):
        return f"${obj.total_budget_spent:,.2f}"
    total_budget_spent_display.short_description = "Total Spent"

    def budget_remaining_display(self, obj):
        return f"${obj.budget_remaining:,.2f}"
    budget_remaining_display.short_description = "Budget Remaining"

    def budget_utilization_percent_display(self, obj):
        return f"{obj.budget_utilization_percent:.1f}%"
    budget_utilization_percent_display.short_description = "Budget Utilization"

    def total_actual_hr_display(self, obj):
        return f"{obj.total_actual_hr:,.2f}"
    total_actual_hr_display.short_description = "Actual HR"

    def remaining_hr_display(self, obj):
        return f"{obj.remaining_hr:,.2f}"
    remaining_hr_display.short_description = "Remaining HR"

    def status_achievement_percent_display(self, obj):
        return f"{obj.status_achievement_percent:.1f}%"
    status_achievement_percent_display.short_description = "Achievement %"

    def achieved_status_display(self, obj):
        return obj.achieved_status
    achieved_status_display.short_description = "Achievement Level"

    # ===== Filter foreign keys by logged-in user's organization =====
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'initiative_planning' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                org = request.user.organization_name
                kwargs['queryset'] = InitiativePlanning.objects.filter(organization_name=org)
        if db_field.name == 'organization_name' and not request.user.is_superuser:
            if hasattr(request.user, 'organization_name'):
                org = request.user.organization_name
                kwargs['queryset'] = OrganizationalProfile.objects.filter(pk=org.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict queryset to user's organization
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(organization_name=request.user.organization_name)
        return qs.none()

    # Pass request to form for filtering initiatives
    def get_form_kwargs(self, request, obj=None, **kwargs):
        form_kwargs = super().get_form_kwargs(request, obj, **kwargs)
        form_kwargs['request'] = request
        return form_kwargs

    # Automatically set organization_name on save
    def save_model(self, request, obj, form, change):
        if not obj.organization_name and hasattr(request.user, 'organization_name'):
            obj.organization_name = request.user.organization_name
        super().save_model(request, obj, form, change)


# ============================
@admin.register(InitiativeResourceItemPlan)
class InitiativeResourceItemPlanAdmin(admin.ModelAdmin):
    form = InitiativeResourceItemPlanForm

    list_display = [
        'organization', 'initiative_name', 'resource_type',
        'resource_name', 'resource_required', 'created_at', 'updated_at'
    ]
    list_filter = ['organization', 'initiative_name', 'resource_type']
    search_fields = ['resource_name', 'resource_type', 'initiative_name__initiative_name']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

    # Filter foreign keys by logged-in user organization
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and hasattr(request.user, 'organization'):
            org = request.user.organization
            if db_field.name == 'initiative_name':
                kwargs['queryset'] = InitiativePlanning.objects.filter(organization=org)
            if db_field.name == 'organization':
                kwargs['queryset'] = OrganizationalProfile.objects.filter(pk=org.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict displayed queryset
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization') and request.user.organization:
            return qs.filter(organization=request.user.organization)
        return qs.none()

    # Pass request to form for custom filtering
    def get_form_kwargs(self, request, obj=None, **kwargs):
        form_kwargs = super().get_form_kwargs(request, obj, **kwargs)
        form_kwargs['request'] = request
        return form_kwargs


@admin.register(InitiativeResourceItemReport)
class InitiativeResourceItemReportAdmin(admin.ModelAdmin):
    form = InitiativeResourceItemReportForm

    # List display including calculated fields
    list_display = [
        'get_plan', 'get_initiative', 'get_organization', 'resource_used',
        'planned_amount_display', 'total_used_display', 'remaining_display', 'utilization_percent_display',
        'report_date', 'created_at', 'updated_at'
    ]

    list_filter = [
        'initiative_resource_plan__organization',
        'initiative_resource_plan__initiative_name',
        'initiative_resource_plan__resource_type',
        'report_date'
    ]

    search_fields = [
        'initiative_resource_plan__resource_name',
        'initiative_resource_plan__initiative_name__initiative_name'
    ]

    ordering = ['-created_at']

    readonly_fields = [
        'planned_amount_display', 'total_used_display', 'remaining_display', 'utilization_percent_display',
        'created_at', 'updated_at'
    ]

    # ===== Filter foreign keys by logged-in user's organization =====
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and hasattr(request.user, 'organization_name'):
            org = request.user.organization_name
            if db_field.name == 'initiative_resource_plan':
                kwargs['queryset'] = InitiativeResourceItemPlan.objects.filter(organization=org)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Restrict queryset to user's organization
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'organization_name') and request.user.organization_name:
            return qs.filter(initiative_resource_plan__organization=request.user.organization_name)
        return qs.none()

    # Pass request to form for filtering plan dropdown
    def get_form_kwargs(self, request, obj=None, **kwargs):
        form_kwargs = super().get_form_kwargs(request, obj, **kwargs)
        form_kwargs['request'] = request
        return form_kwargs

    # ===== Helper fields for list display =====
    def get_plan(self, obj):
        return obj.initiative_resource_plan.resource_name
    get_plan.short_description = 'Resource Plan'

    def get_initiative(self, obj):
        return obj.initiative_resource_plan.initiative_name
    get_initiative.short_description = 'Initiative'

    def get_organization(self, obj):
        return obj.initiative_resource_plan.organization
    get_organization.short_description = 'Organization'

    # Calculated fields for display
    def planned_amount_display(self, obj):
        return obj.planned_amount
    planned_amount_display.short_description = 'Planned Amount'

    def total_used_display(self, obj):
        return obj.total_used
    total_used_display.short_description = 'Total Used'

    def remaining_display(self, obj):
        return obj.remaining
    remaining_display.short_description = 'Remaining'

    def utilization_percent_display(self, obj):
        return obj.utilization_percent
    utilization_percent_display.short_description = 'Utilization %'
