from django.db import models
import datetime
from django.core.exceptions import ValidationError
import re
# choices
from .choices.country_code_choices import COUNTRY_CODE_CHOICES
# date and utils
from django.utils.text import slugify
from django.db.models import Sum
# stakeholder_list info
from decimal import Decimal, ROUND_HALF_UP
from django.core.validators import MinValueValidator
from datetime import date

# services

from .services.values import ValuesService
import calendar
from multiselectfield import MultiSelectField
from account.models import CustomUser
import uuid


# Create your models here.
class OrganizationalProfile(models.Model):
    organization_choices = [
        ('sole_proprietorship', 'Sole Proprietorship'),
        ('partnership', 'Partnership'), ('corporation', 'Corporation'),
        ('joint_venture', 'Joint Venture'), ('cooperative', 'Cooperative'), ('non_profit', 'Non Profit'),
        ('non_governmental', 'Non Governmental'), ('governmental', 'Governmental'),
        ('other', 'Other')
    ]
    SECTOR_CHOICES = [
        ('education', 'Education'),
        ('healthcare', 'Healthcare & Medical Services'),
        ('information_technology', 'Information Technology & Digital Services'),
        ('finance_banking', 'Finance, Banking & Insurance'),
        ('agriculture', 'Agriculture & Agribusiness'),
        ('manufacturing', 'Manufacturing & Industry'),
        ('energy_utilities', 'Energy & Utilities'),
        ('environment_sustainability', 'Environment & Sustainability'),
        ('transport_logistics', 'Transportation & Logistics'),
        ('tourism_hospitality', 'Tourism, Travel & Hospitality'),
        ('construction_real_estate', 'Construction & Real Estate'),
        ('telecommunications', 'Telecommunications'),
        ('research_development', 'Research & Development'),
        ('public_sector', 'Government & Public Administration'),
        ('creative_media', 'Creative Arts, Media & Entertainment'),
        ('retail_wholesale', 'Retail & Wholesale Trade'),
        ('ecommerce', 'E-commerce & Online Retail'),
        ('professional_services', 'Professional & Business Services'),
        ('hospitality_food', 'Hospitality & Food Services'),
        ('mining_resources', 'Mining, Oil & Natural Resources'),
    ]
    organization_name = models.CharField(max_length=80)
    organization_address = models.CharField(max_length=80)
    employer_tin = models.CharField(max_length=90, verbose_name='Employer TIN')
    organization_type = models.CharField(choices=organization_choices, max_length=70)
    sector_name = models.CharField( max_length=50, choices=SECTOR_CHOICES)
    contact_personnel = models.CharField(max_length=90)


    def __str__(self):
        return str(self.organization_name)

    class Meta:
        verbose_name = "Organizational Profile"
        verbose_name_plural = "               Organizational Profile"
        ordering = ['-id']


def validate_phone_number(value):
    # Regular expression pattern to validate phone number without country code
    pattern = r'^\d{9,10}'
    if not re.match(pattern, value):
        raise ValidationError("Enter a valid phone number (7-12 digits) without country code.")



class OrganizationInvitation(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (CANCELLED, 'Cancelled'),
    ]

    ROLE_CHOICES = [
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ]

    organization_name = models.ForeignKey(
        OrganizationalProfile, on_delete=models.CASCADE, related_name='invitations'
    )
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    invited_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)
    message = models.TextField(blank=True, null=True, help_text="Optional message to the invitee")
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


    def __str__(self):
        return f"{self.email} ({self.status})"


    
class Vision(models.Model):
    organization_name = models.ForeignKey(OrganizationalProfile, on_delete=models.PROTECT)
    vision_statement = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.vision_statement} - {self.organization_name}"

    @property
    def display_vision_statement(self):
        from management_project.services.vision import VisionService
        return VisionService.get_display_statement(self.organization_name.organization_name, self.vision_statement)


class Mission(models.Model):
    organization_name = models.ForeignKey(OrganizationalProfile, on_delete=models.PROTECT)
    mission_statement = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.mission_statement} - {self.organization_name}"

    @property
    def display_mission_statement(self):
        from management_project.services.mission import MissionService
        return MissionService.get_display_statement(self.organization_name.organization_name, self.mission_statement)




class Values(models.Model):
    organization_name = models.ForeignKey(OrganizationalProfile, on_delete=models.PROTECT)

    values = models.CharField(
        max_length=50,
        choices=[(key, label) for group in ValuesService.VALUE_CHOICES for key, label in group[1]],
        unique=True
    )

    def get_category(self):
        for group_name, group_values in ValuesService.VALUE_CHOICES:
            for key, label in group_values:
                if key == self.values:
                    return group_name
        return None

    def __str__(self):
        return self.get_values_display()



class SwotAnalysis(models.Model):
    SWOT_TYPES = [
        ('Strength', 'Strength'),
        ('Weakness', 'Weakness'),
        ('Opportunity', 'Opportunity'),
        ('Threat', 'Threat'),
    ]

    PRIORITY_CHOICES = [
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    ]

    IMPACT_CHOICES = [
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    ]

    LIKELIHOOD_CHOICES = [
        ('Almost Certain', 'Almost Certain'),
        ('Likely', 'Likely'),
        ('Possible', 'Possible'),
        ('Unlikely', 'Unlikely'),
        ('Rare', 'Rare'),
    ]

    organization_name = models.ForeignKey(
        OrganizationalProfile, on_delete=models.PROTECT
    )
    swot_type = models.CharField(max_length=20, choices=SWOT_TYPES)
    swot_pillar = models.CharField(max_length=100)
    swot_factor = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    impact = models.CharField(max_length=20, choices=IMPACT_CHOICES, default="Medium")
    likelihood = models.CharField(max_length=20, choices=LIKELIHOOD_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["swot_type", "priority", "-created_at"]

    def __str__(self):
        return f"{self.swot_type} → {self.swot_pillar} → {self.swot_factor[:50]}"



class StrategyHierarchy(models.Model):
    organization_name = models.ForeignKey(
        OrganizationalProfile, on_delete=models.PROTECT
    )
    strategic_perspective = models.CharField(max_length=100)
    focus_area = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    kpi = models.CharField(max_length=100, verbose_name='Key Performance Indicator')
    formula = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.strategic_perspective} → {self.focus_area} → {self.objective} → {self.kpi}"



class Stakeholder(models.Model):
    # ------------------ Enhanced Choices ------------------
    STAKEHOLDER_TYPE_CHOICES = [
        ('internal', 'Internal'),
        ('external', 'External'),
        ('interface', 'Interface'),
    ]

    STAKEHOLDER_CATEGORY_CHOICES = [
        ('strategic', 'Strategic'),
        ('operational', 'Operational'),
        ('tactical', 'Tactical'),
        ('influencer', 'Influencer'),
        ('beneficiary', 'Beneficiary'),
    ]

    ROLE_CHOICES = [
        # Leadership & Governance
        ('owner', 'Owner'),
        ('board_member', 'Board Member'),
        ('ceo', 'CEO'),
        ('executive', 'Executive'),
        ('director', 'Director'),
        # Management
        ('senior_manager', 'Senior Manager'),
        ('manager', 'Manager'),
        ('team_lead', 'Team Lead'),
        ('supervisor', 'Supervisor'),
        ('department_head', 'Department Head'),
        ('branch_manager', 'Branch Manager'),
        # Operational
        ('employee', 'Employee'),
        ('contractor', 'Contractor'),
        ('intern', 'Intern'),
        ('volunteer', 'Volunteer'),
        # Functional Specialists
        ('finance', 'Finance'),
        ('hr', 'Human Resources'),
        ('it', 'IT Support'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('qa', 'Quality Assurance'),
        ('sales', 'Sales'),
        ('marketing', 'Marketing'),
        ('operations', 'Operations'),
        ('logistics', 'Logistics'),
        ('legal', 'Legal Counsel'),
        ('compliance', 'Compliance Officer'),
        # Project & Product
        ('project_manager', 'Project Manager'),
        ('product_owner', 'Product Owner'),
        ('scrum_master', 'Scrum Master'),
        ('business_analyst', 'Business Analyst'),
        ('trainer', 'Trainer'),
        ('mentor', 'Mentor'),
        # External Stakeholders
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
        ('partner', 'Partner'),
        ('investor', 'Investor'),
        ('funder', 'Funder'),
        ('regulator', 'Regulator'),
        ('government_official', 'Government Official'),
        ('auditor', 'Auditor'),
        ('consultant', 'Consultant'),
        ('advisor', 'Advisor'),
        ('researcher', 'Researcher'),
        ('media', 'Media'),
        ('community', 'Community'),
        # Catch-all
        ('other', 'Other'),
    ]

    LEVEL_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]

    ENGAGEMENT_STRATEGY_CHOICES = [
        ('monitor', 'Monitor'),
        ('inform', 'Inform'),
        ('consult', 'Consult'),
        ('involve', 'Involve'),
        ('collaborate', 'Collaborate'),
        ('empower', 'Empower'),
    ]

    RELATIONSHIP_STATUS_CHOICES = [
        ('new', 'New'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('challenged', 'Challenged'),
        ('terminated', 'Terminated'),
    ]

    # ------------------ Core Information ------------------
    organization_name = models.ForeignKey(
        'OrganizationalProfile',
        on_delete=models.PROTECT,
        related_name='stakeholders'
    )
    # ------------------ Identification ------------------
    stakeholder_code = models.CharField(max_length=50, unique=True, blank=True)
    stakeholder_name = models.CharField(max_length=200, help_text='Stakeholder name or organization')
    stakeholder_type = models.CharField(max_length=20, choices=STAKEHOLDER_TYPE_CHOICES)
    stakeholder_category = models.CharField(max_length=20, choices=STAKEHOLDER_CATEGORY_CHOICES, default='operational')

    role = MultiSelectField(
        choices=ROLE_CHOICES,
        max_length=500,
        default=['employee'],
        help_text="Select one or more roles"
    )
    primary_role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        help_text="Primary role for reporting and analysis"
    )

    # ------------------ Stakeholder Analysis ------------------
    impact_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    interest_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    influence_score = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    risk_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    contribution_score = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    priority = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    satisfaction_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')

    engagement_strategy = MultiSelectField(
        choices=ENGAGEMENT_STRATEGY_CHOICES,
        max_length=200,
        default=['inform'],
        help_text="Select one or more engagement strategies"
    )

    # ------------------ Contact Information ------------------
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    # ------------------ Relationship Management ------------------
    relationship_status = models.CharField(max_length=20, choices=RELATIONSHIP_STATUS_CHOICES, default='new')
    last_engagement_date = models.DateField(blank=True, null=True)
    next_engagement_date = models.DateField(blank=True, null=True)

    aligned_objectives = models.ManyToManyField(
        'StrategyHierarchy', blank=True, related_name='stakeholders'
    )

    engagement_priority_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    is_key_stakeholder = models.BooleanField(default=False)
    requires_attention = models.BooleanField(default=False)

    # ------------------ Timestamps ------------------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    # ------------------ Meta ------------------
    # ------------------ Meta ------------------
    class Meta:
        verbose_name = "Stakeholder"
        verbose_name_plural = "Stakeholders"
        ordering = ["-engagement_priority_score", "stakeholder_name"]
        indexes = [
            models.Index(fields=['stakeholder_type', 'engagement_priority_score']),
            models.Index(fields=['organization_name', 'risk_level']),
            models.Index(fields=['stakeholder_code']),
        ]

    def __str__(self):
        return f"{self.stakeholder_name} ({self.get_primary_role_display()})"

    # ------------------ Save Override ------------------
    def save(self, *args, **kwargs):
        # Auto-generate stakeholder_code
        if not self.stakeholder_code:
            org_prefix = self.organization_name.organization_name[:3].upper()
            base_code = f"STK-{org_prefix}-{self.stakeholder_name[:3].upper()}"
            counter = 1
            code = f"{base_code}-{counter:04d}"
            while Stakeholder.objects.filter(stakeholder_code=code).exists():
                counter += 1
                code = f"{base_code}-{counter:04d}"
            self.stakeholder_code = code

        # Auto-generate slug
        if not self.slug:
            base_slug = slugify(f"{self.stakeholder_name}-{self.stakeholder_code}")
            slug = base_slug
            counter = 1
            while Stakeholder.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # Set primary role
        if not self.primary_role and self.role:
            self.primary_role = self.role[0]

        # Calculate engagement score & flags
        self.calculate_engagement_priority()
        self.is_key_stakeholder = self.engagement_priority_score >= Decimal('7.0')
        self.requires_attention = (
                self.engagement_priority_score >= Decimal('8.0') or
                self.risk_level in ['high', 'very_high'] or
                self.satisfaction_level in ['very_low', 'low']
        )

        super().save(*args, **kwargs)

    # ------------------ Engagement Priority Calculation ------------------
    def calculate_engagement_priority(self):
        """Calculate numerical engagement priority score"""
        score_map = {
            'very_low': 1,
            'low': 2,
            'medium': 3,
            'high': 4,
            'very_high': 5
        }
        weighted_score = (
                score_map.get(self.impact_level, 3) * 0.3 +
                score_map.get(self.influence_score, 3) * 0.25 +
                score_map.get(self.interest_level, 3) * 0.2 +
                score_map.get(self.risk_level, 3) * 0.25
        )
        self.engagement_priority_score = Decimal(round(weighted_score * 2, 1))

    # ------------------ Properties ------------------
    @property
    def engagement_matrix_position(self):
        if self.influence_score in ['high', 'very_high'] and self.interest_level in ['high', 'very_high']:
            return 'manage_closely'
        elif self.influence_score in ['high', 'very_high']:
            return 'keep_satisfied'
        elif self.interest_level in ['high', 'very_high']:
            return 'keep_informed'
        else:
            return 'monitor'

    @property
    def days_since_last_engagement(self):
        if self.last_engagement_date:
            return (date.today() - self.last_engagement_date).days
        return None

    @property
    def is_engagement_overdue(self):
        return self.days_since_last_engagement > 90 if self.days_since_last_engagement else False

    # ------------------ Validation ------------------
    def clean(self):
        import re
        errors = {}
        if self.email and not re.match(r'^[^@]+@[^@]+\.[^@]+$', self.email):
            errors['email'] = 'Enter a valid email address.'
        if self.phone and not re.match(r'^\+?\d{9,15}$', self.phone):
            errors['phone'] = 'Enter a valid phone number.'
        if errors:
            raise ValidationError(errors)



class StrategicCycle(models.Model):
    TIME_HORIZON_CHOICES = [
        ('10 years', '10 years'),
        ('5 years', '5 years'),
        ('3 years', '3 years'),
        ('2 years', '2 years'),
        ('1 year', '1 year'),
        ('6 months', '6 months'),
        ('Quarterly', 'Quarterly'),
        ('Monthly', 'Monthly'),
    ]

    TIME_HORIZON_TYPE_CHOICES = [
        ('Long Term', 'Long Term'),
        ('Medium Term', 'Medium Term'),
        ('Short Term', 'Short Term'),
    ]

    organization_name = models.ForeignKey(
        OrganizationalProfile,
        on_delete=models.PROTECT,
        related_name='strategic_cycles'
    )
    name = models.CharField(max_length=100, help_text='Descriptive name for the strategic cycle')
    time_horizon = models.CharField(max_length=20, choices=TIME_HORIZON_CHOICES)
    time_horizon_type = models.CharField(max_length=20, choices=TIME_HORIZON_TYPE_CHOICES)
    start_date = models.DateField(help_text='Exact start date of the strategic cycle')
    end_date = models.DateField(help_text='Exact end date of the strategic cycle / report date')

    # New fields to store calculated values

    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = "Strategic Cycle"
        verbose_name_plural = "Strategic Cycles"
        ordering = ['start_date', '-id']

    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days

    @property
    def start_month_name(self):
        return calendar.month_name[self.start_date.month]

    @property
    def start_quarter(self):
        return (self.start_date.month - 1) // 3 + 1

    @property
    def start_year(self):
        return self.start_date.year

    def save(self, *args, **kwargs):
        # Auto-generate name based on org + time horizon + dates
        self.name = f"{self.organization_name} - {self.time_horizon} ({self.start_date:%B %Y}–{self.end_date:%B %Y})"

        if not self.slug:
            # Build slug from multiple fields
            base_slug = slugify(
                f"{self.name}-"
                f"{self.time_horizon}-{self.time_horizon_type}-"
                f"{self.start_date}-{self.end_date}"
            )
            slug = base_slug
            counter = 1
            while StrategicCycle.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        start_str = self.start_date.strftime("%Y-%m-%d") if self.start_date else "N/A"
        end_str = self.end_date.strftime("%Y-%m-%d") if self.end_date else "N/A"
        return f"{self.organization_name} - {self.name} ({self.time_horizon_type}, {start_str} → {end_str})"


class StrategicActionPlan(models.Model):
    # stakeholder_list information
    INDICATOR_TYPE_CHOICES = [
        ('Lead', 'Lead'),
        ('Lagg', 'Lagg'),
    ]

    DIRECTION_OF_CHANGE_CHOICES = [
        ('Increasing', 'Increasing'),
        ('Decreasing', 'Decreasing'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    organization_name = models.ForeignKey(
        OrganizationalProfile, on_delete=models.PROTECT
    )
    # Parent references
    strategic_cycle = models.ForeignKey(
        'StrategicCycle',
        on_delete=models.CASCADE,
        related_name='action_plans'
    )
    strategy_hierarchy = models.ForeignKey(
        'StrategyHierarchy',
        on_delete=models.CASCADE,
        related_name='action_plans'
    )
    responsible_bodies = models.ManyToManyField(
        'Stakeholder', blank=True, related_name='action_plans'
    )

    # KPI & Measurement
    indicator_type = models.CharField(max_length=10, choices=INDICATOR_TYPE_CHOICES)
    direction_of_change = models.CharField(max_length=10, choices=DIRECTION_OF_CHANGE_CHOICES)
    baseline = models.DecimalField(max_digits=22, decimal_places=2)
    target = models.DecimalField(max_digits=22, decimal_places=2)
    improvement_needed = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    status = models.CharField( max_length=20, choices=STATUS_CHOICES,
        default='pending', help_text="Current status of the strategic plan"
    )
    weight = models.DecimalField(
        max_digits=5, decimal_places=2,
        default=100,
        help_text="Weight of this Action Plan KPI relative to other KPI per strategic cycle"
    )


    class Meta:
        verbose_name = "Strategic Action Plan"
        verbose_name_plural = "Strategic Action Plans"
        ordering = ['strategic_cycle__start_date', '-id']



    def save(self, *args, **kwargs):

        # Calculate improvement_needed and duration
        if self.baseline is not None and self.target is not None:
            self.improvement_needed = self.target - self.baseline

        super().save(*args, **kwargs)

    def responsible_bodies_display(self):
        return ", ".join([str(s) for s in self.responsible_bodies.all()])

    def get_full_display(self):
        """Full info for tooltip"""
        cycle_name = (
            f"{self.strategic_cycle.name} - {self.strategic_cycle.time_horizon} - "
            f"{self.strategic_cycle.time_horizon_type} - {self.strategic_cycle.start_date} - "
            f"{self.strategic_cycle.end_date}" if self.strategic_cycle else "N/A"
        )
        kpi = self.strategy_hierarchy.kpi if self.strategy_hierarchy else "N/A"
        baseline = self.baseline or 0
        target = self.target or 0
        responsible = self.responsible_bodies_display() or "N/A"

        return f"{cycle_name} | KPI: {kpi} | Baseline: {baseline} | Target: {target} | Responsible: {responsible}"

    def __str__(self):
        """Single-line label for dropdown"""
        if self.strategic_cycle:
            start = self.strategic_cycle.start_date.strftime("%B %d, %Y") if self.strategic_cycle.start_date else "N/A"
            end = self.strategic_cycle.end_date.strftime("%B %d, %Y") if self.strategic_cycle.end_date else "N/A"
            cycle_name = f"{self.strategic_cycle.name} - {self.strategic_cycle.time_horizon} - {self.strategic_cycle.time_horizon_type} - {start} - {end}"
        else:
            cycle_name = "N/A"

        kpi = self.strategy_hierarchy.kpi if self.strategy_hierarchy else "N/A"
        baseline = self.baseline or 0
        target = self.target or 0
        responsible = self.responsible_bodies_display() or "N/A"

        return f"{cycle_name} | KPI: {kpi} | Baseline: {baseline} | Target: {target} | Responsible: {responsible}"


    def dropdown_label_lines(self):
        """Return tuple/list of lines for display in the radio label."""
        if self.strategic_cycle:
            start = self.strategic_cycle.start_date.strftime("%B %d, %Y") if self.strategic_cycle.start_date else "N/A"
            end = self.strategic_cycle.end_date.strftime("%B %d, %Y") if self.strategic_cycle.end_date else "N/A"
            cycle_line = f"{self.strategic_cycle.name} ({start} - {end})"
        else:
            cycle_line = "Cycle: N/A"

        kpi = self.strategy_hierarchy.kpi if self.strategy_hierarchy else "N/A"
        baseline = self.baseline or 0
        target = self.target or 0
        resp = self.responsible_bodies_display() or "N/A"

        return [
            cycle_line,
            f"KPI: {kpi}",
            f"Baseline: {baseline} | Target: {target}",
            f"Responsible: {resp}",
        ]


class InitiativePlanning(models.Model):
    LEVEL_CHOICES = [
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    ]

    organization_name = models.ForeignKey(
        'OrganizationalProfile', on_delete=models.PROTECT
    )
    initiative_focus_area = models.CharField(max_length=100)
    initiative_dimension = models.CharField(max_length=100)
    initiative_name = models.CharField(max_length=100)

    aligned_objectives = models.ManyToManyField(
        'StrategyHierarchy',
        related_name='supporting_initiatives',
        blank=True,
        help_text="Optional: Which strategic objectives does this initiative_planning support?"
    )
    description = models.TextField(max_length=100)

    total_budget_planned = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0)],
        help_text="Planned budget for the project, programme or action",
    )
    total_hr_planned = models.DecimalField(
        "Planned Human Resources (Person-Days)",
        max_digits=8,
        decimal_places=2,
        default=0,
        help_text="Planned effort in person-days for this initiative"
    )

    priority = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Medium')
    impact = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Medium')
    likelihood = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Medium')
    risk_level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Medium')
    baseline_status = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Medium')
    target_status = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='High')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.initiative_focus_area} → {self.initiative_dimension} → {self.initiative_name}"



class InitiativeReport(models.Model):
    LEVEL_CHOICES = [
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    ]

    organization_name = models.ForeignKey(
        'OrganizationalProfile', on_delete=models.PROTECT
    )
    initiative_planning = models.ForeignKey(
        'InitiativePlanning', on_delete=models.CASCADE, related_name='reports'
    )
    report_date = models.DateField(auto_now_add=True)

    total_budget_spent = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Amount spent so far"
    )
    total_actual_hr = models.DecimalField(
        "Actual HR (Person-Days)",
        max_digits=8,
        decimal_places=2,
        default=0,
        help_text="The total human resource effort actually used in person-days for this initiative"
    )

    achieved_status = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Medium')

    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ===== Calculated fields =====
    # ===== Calculated fields =====
    @property
    def planned_budget(self):
        return self.initiative_planning.total_budget_planned or 0

    @property
    def budget_remaining(self):
        return max(self.planned_budget - self.total_budget_spent, 0)

    @property
    def budget_utilization_percent(self):
        return round((self.total_budget_spent / self.planned_budget) * 100, 1) if self.planned_budget else 0

    @property
    def planned_hr(self):
        return self.initiative_planning.total_hr_planned or 0

    @property
    def remaining_hr(self):
        return max(self.planned_hr - self.total_actual_hr, 0)

    @property
    def hr_utilization_percent(self):
        return round((self.total_actual_hr / self.planned_hr) * 100, 1) if self.planned_hr else 0

    @property
    def remaining_days(self):
        end = getattr(self, 'end_date', None) or self.initiative_planning.end_date
        if end:
            return max((end - date.today()).days, 0)
        return None

    @property
    def remaining_months(self):
        start = getattr(self, 'start_date', None) or self.initiative_planning.start_date
        end = getattr(self, 'end_date', None) or self.initiative_planning.end_date
        if start and end:
            return max((end - date.today()).days // 30, 0)
        return None

    @property
    def status_achievement_percent(self):
        """
        Calculates achievement percent based on baseline -> target mapping.
        """
        mapping = {'Very Low': 20, 'Low': 40, 'Medium': 60, 'High': 80, 'Very High': 100}
        baseline = mapping.get(getattr(self.initiative_planning, 'baseline_status', 'Medium'), 0)
        target = mapping.get(getattr(self.initiative_planning, 'target_status', 'High'), 100)
        achieved = mapping.get(self.achieved_status, 0)

        if target <= baseline:
            return 100.0

        percent = ((achieved - baseline) / (target - baseline)) * 100
        return max(0, min(round(percent, 1), 100))

    def __str__(self):
        return f"Report for {self.initiative_planning.initiative_name} on {self.report_date}"




RESOURCE_TYPES = [
    ('Person_hours', 'Person hours'),
    ('Equipment', 'Equipment'),
    ('Material', 'Material'),
    ('hr', 'HR'),
    ('Budget', 'Budget'),
    ('Other', 'Other'),
]

class InitiativeResourceItemPlan(models.Model):
    organization = models.ForeignKey(
        'OrganizationalProfile', on_delete=models.PROTECT
    )
    initiative_name = models.ForeignKey(
        'InitiativePlanning', on_delete=models.CASCADE, related_name='resource_item_plans'
    )
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES, default='Other')
    resource_name = models.CharField(max_length=100)
    resource_required = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resource_name} ({self.resource_type})"



class InitiativeResourceItemReport(models.Model):
    initiative_resource_plan = models.ForeignKey(
        InitiativeResourceItemPlan, on_delete=models.CASCADE, related_name='reports'
    )
    resource_used = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )
    report_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ===== Calculated fields =====
    # ===== Calculated fields =====
    @property
    def planned_amount(self):
        """Planned amount from the linked resource plan."""
        return self.initiative_resource_plan.resource_required or 0

    @property
    def total_used(self):
        """Total used resource for this plan, summing all reports."""
        return self.initiative_resource_plan.reports.aggregate(total=models.Sum('resource_used'))['total'] or 0

    @property
    def remaining(self):
        """Remaining resource for this plan."""
        return max(self.planned_amount - self.total_used, 0)

    @property
    def utilization_percent(self):
        """Percentage of resource used for this plan."""
        if self.planned_amount:
            return round((self.total_used / self.planned_amount) * 100, 1)
        return 0

    def __str__(self):
        return f"Report for {self.resource_plan.resource_name} on {self.report_date}"


# strategic report
class StrategicReport(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    organization_name = models.ForeignKey(OrganizationalProfile, on_delete=models.PROTECT)
    action_plan = models.ForeignKey(
        StrategicActionPlan, on_delete=models.CASCADE, related_name="reports"
    )
    achievement = models.DecimalField(max_digits=22, decimal_places=2, default=0)
    percent_achieved = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    variance = models.DecimalField(max_digits=22, decimal_places=2, default=0)
    weighted_score = models.DecimalField(max_digits=22, decimal_places=2, default=0)
    data_source = models.CharField(max_length=200, blank=True, null=True)
    data_collector = models.CharField(max_length=200, blank=True, null=True)
    progress_summary = models.TextField(blank=True, null=True)
    performance_summary = models.TextField(blank=True, null=True)
    # Optional qualitative fields
    challenges = models.TextField(blank=True, null=True)
    successes = models.TextField(blank=True, null=True)
    lessons_learned = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='pending', help_text="Current status of the strategic plan"
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = "Strategic Report"
        verbose_name_plural = "Strategic Reports"

    def save(self, *args, **kwargs):

        plan = self.action_plan
        # Ensure percent achieved and variance
        baseline = plan.baseline or 0
        target = plan.target or 0
        actual = self.achievement
        self.percent_achieved = ((actual - baseline) / (target - baseline) * 100) if target != baseline else 0
        self.variance = target - actual
        self.weighted_score = actual * (plan.weight / 100)
        self.responsible_body = plan.responsible_bodies_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.action_plan.strategic_cycle.time_horizon} | "
            f"Start: {self.action_plan.strategic_cycle.start_date:%B %d, %Y} | "
            f"End: {self.action_plan.strategic_cycle.end_date:%B %d, %Y}"
        )


class SwotReport(models.Model):
    SWOT_TYPES = [
        ('Strength', 'Strength'),
        ('Weakness', 'Weakness'),
        ('Opportunity', 'Opportunity'),
        ('Threat', 'Threat'),
    ]

    PRIORITY_CHOICES = [
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    ]

    IMPACT_CHOICES = [
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    ]

    LIKELIHOOD_CHOICES = [
        ('Almost Certain', 'Almost Certain'),
        ('Likely', 'Likely'),
        ('Possible', 'Possible'),
        ('Unlikely', 'Unlikely'),
        ('Rare', 'Rare'),
    ]

    organization_name = models.ForeignKey(
        OrganizationalProfile, on_delete=models.PROTECT
    )
    strategic_report_period = models.ForeignKey(
        StrategicReport, on_delete=models.CASCADE
    )
    swot_type = models.CharField(max_length=20, choices=SWOT_TYPES)
    swot_pillar = models.CharField(max_length=100)
    swot_factor = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    impact = models.CharField(max_length=20, choices=IMPACT_CHOICES, default="Medium")
    likelihood = models.CharField(max_length=20, choices=LIKELIHOOD_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["swot_type", "priority", "-created_at"]

    def __str__(self):
        return f"{self.swot_type} → {self.swot_pillar} → {self.swot_factor[:50]}"




class RiskManagement(models.Model):
    """
    Represents a risk item categorized by type,
    with likelihood, impact, severity score, and recommended mitigation actions.
    """

    # --- Choices ---
    LEVEL_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]

    STATUS_CHOICES = [
        ('identified', 'Identified'),
        ('mitigated', 'Mitigated'),
        ('closed', 'Closed'),
    ]

    organization_name = models.ForeignKey(
        OrganizationalProfile, on_delete=models.PROTECT
    )
    strategic_cycle = models.ForeignKey(
        'StrategicCycle',
        on_delete=models.CASCADE,
    )

    # --- Core Fields ---
    risk_category = models.CharField(
        max_length=100,
        help_text="Select or define the risk category."
    )
    risk_name = models.CharField(
        max_length=150,
        unique=True,
        help_text="Enter a descriptive name for the risk."
    )
    mitigation_action = models.CharField(
        max_length=255,
        blank=True,
        help_text="Suggested or automatic mitigation action."
    )

    # --- Assessment Fields ---
    likelihood = models.CharField(
        max_length=15,
        choices=LEVEL_CHOICES,
        default='medium'
    )
    impact = models.CharField(
        max_length=15,
        choices=LEVEL_CHOICES,
        default='medium'
    )
    severity_score = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='identified'
    )

    # --- Timestamps ---
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Risk Management Entry"
        verbose_name_plural = "Risk Management Entries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.risk_category} → {self.risk_name}"

    # --- Logic ---
    def calculate_severity(self):
        """Compute severity score based on 5-level likelihood × impact scale."""
        scale = {
            'very_low': 1,
            'low': 2,
            'medium': 3,
            'high': 4,
            'very_high': 5,
        }
        return scale.get(self.likelihood, 1) * scale.get(self.impact, 1)

    def save(self, *args, **kwargs):
        """Auto-calculate severity score before saving."""
        self.severity_score = self.calculate_severity()
        super().save(*args, **kwargs)

