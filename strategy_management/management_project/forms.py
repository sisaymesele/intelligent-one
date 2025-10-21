from django import forms
from management_project.models import (
    OrganizationalProfile, OrganizationInvitation, SwotAnalysis, Vision, Mission, Values, StrategyHierarchy,
    Stakeholder, StrategicCycle, StrategicActionPlan, StrategicReport, SwotReport, InitiativePlanning,
    InitiativeReport, InitiativeResourceItemReport, InitiativeResourceItemPlan, InitiativePlanning, RiskManagement
)
from management_project.services.vision import VisionService
from management_project.services.mission import MissionService
from .services.swot import SwotChoicesService
from .services.strategy_hierarchy import StrategyHierarchyChoicesService
from .services.values import ValuesService
from .services.initiative import InitiativePlanningChoicesService
from multiselectfield import MultiSelectFormField
from .services.risk_management import RiskChoicesService



class OrganizationalProfileForm(forms.ModelForm):

    class Meta:

        model = OrganizationalProfile

        fields = [
            'organization_name', 'organization_address', 'employer_tin', 'organization_type',
            'sector_name', 'contact_personnel'
        ]

        widgets = {
            'organization_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Organization Name'
            }),
            'organization_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Organization Address'
            }),
            'employer_tin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employer TIN'
            }),

            'organization_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'sector_name': forms.Select(attrs={
                'class': 'form-control',
            }),
            'contact_personnel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contact Personnel'
            }),
        }

class OrganizationInvitationForm(forms.ModelForm):
    class Meta:
        model = OrganizationInvitation
        fields = [
            'email',
            'role',
            'message',
        ]

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Invitee Email',
            }),
            'role': forms.Select(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional message to the invitee',
                'rows': 3,
            }),
        }
        labels = {
            'email': 'Invitee Email',
            'role': 'Role',
            'message': 'Message',
        }
        help_texts = {
            'role': 'Choose the role for the invitee: Editor (content) or Viewer (read-only).',
            'message': 'Optional message to include with the invitation.',
        }

class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = ['organization_name', 'vision_statement',]
        widgets = {
            'organization_name': forms.HiddenInput(),  # Hide the field
            'vision_statement': forms.Select(attrs={'class': 'form-control'}),
        }

    error_css_class = 'text-danger'
    required_css_class = 'font-weight-bold'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Safe default organization
        default_org = getattr(self.instance, 'organization_name', None) or OrganizationalProfile.objects.first()

        # Override with GET/POST data if available
        org_id = None
        if self.request:
            org_id = self.request.GET.get('organization_id') or self.data.get('organization_name')
        if org_id:
            default_org = OrganizationalProfile.objects.filter(id=org_id).first() or default_org

        self.fields['organization_name'].initial = default_org

        # Use VisionService instance
        self.service = VisionService(default_org)

        # Set vision statement choices
        vision_choices = self.service.get_choices()
        if vision_choices:
            self.fields['vision_statement'].widget.choices = vision_choices
            self.fields['vision_statement'].initial = getattr(self.instance, 'vision_statement', None) or vision_choices[0][0]
        else:
            self.fields['vision_statement'].widget.attrs['disabled'] = True

        # Add error class for invalid fields
        for field_name, field in self.fields.items():
            if field_name in self.errors:
                field.widget.attrs['class'] = f"{field.widget.attrs.get('class', '')} is-invalid"

    def clean(self):
        cleaned_data = super().clean()
        vision_statement = cleaned_data.get('vision_statement')
        if vision_statement:
            try:
                self.service.validate_choice(vision_statement)
            except ValueError as e:
                self.add_error('vision_statement', str(e))
        return cleaned_data


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['organization_name', 'mission_statement']
        widgets = {
            'organization_name': forms.HiddenInput(),  # Hide the field
            'mission_statement': forms.Select(attrs={'class': 'form-control'}),
        }

    error_css_class = 'text-danger'
    required_css_class = 'font-weight-bold'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Safe default organization
        default_org = getattr(self.instance, 'organization_name', None) or OrganizationalProfile.objects.first()

        # Override with GET/POST data if available
        org_id = None
        if self.request:
            org_id = self.request.GET.get('organization_id') or self.data.get('organization_name')
        if org_id:
            default_org = OrganizationalProfile.objects.filter(id=org_id).first() or default_org

        self.fields['organization_name'].initial = default_org

        # Use MissionService instance
        self.service = MissionService(default_org)

        # Set mission statement choices
        mission_choices = self.service.get_choices()
        if mission_choices:
            self.fields['mission_statement'].widget.choices = mission_choices
            self.fields['mission_statement'].initial = getattr(self.instance, 'mission_statement', None) or mission_choices[0][0]
        else:
            self.fields['mission_statement'].widget.attrs['disabled'] = True

        # Add error class for invalid fields
        for field_name, field in self.fields.items():
            if field_name in self.errors:
                field.widget.attrs['class'] = f"{field.widget.attrs.get('class', '')} is-invalid"

    def clean(self):
        cleaned_data = super().clean()
        mission_statement = cleaned_data.get('mission_statement')
        if mission_statement:
            try:
                self.service.validate_choice(mission_statement)
            except ValueError as e:
                self.add_error('mission_statement', str(e))
        return cleaned_data



class ValuesForm(forms.ModelForm):
    class Meta:
        model = Values
        fields = ['values']
        widgets = {
            'values': forms.Select(
                attrs={'class': 'form-control'},
                choices=ValuesService.VALUE_CHOICES
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure choices always follow grouped <optgroup> style
        self.fields['values'].choices = ValuesService.VALUE_CHOICES




class SwotAnalysisForm(forms.ModelForm):
    class Meta:
        model = SwotAnalysis
        fields = [
            'swot_type', 'swot_pillar', 'swot_factor',
            'priority', 'impact', 'likelihood', 'description'
        ]
        widgets = {
            'swot_type': forms.Select(attrs={'class': 'form-control'}),
            'swot_pillar': forms.Select(attrs={'class': 'form-control'}),
            'swot_factor': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'impact': forms.Select(attrs={'class': 'form-control'}),
            'likelihood': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        swot_type = self.data.get('swot_type') or getattr(self.instance, 'swot_type', None)
        pillar = self.data.get('swot_pillar') or getattr(self.instance, 'swot_pillar', None)

        # Level 1: SWOT Type
        self.fields['swot_type'].choices = [('', '--- Select SWOT Type ---')] + SwotChoicesService.get_swot_type_choices()

        # Level 2: Pillar
        if swot_type:
            self.fields['swot_pillar'].choices = [('', '--- Select Pillar ---')] + SwotChoicesService.get_pillar_choices(swot_type)
            self.fields['swot_pillar'].widget.attrs.pop('disabled', None)
        else:
            self.fields['swot_pillar'].choices = [('', '--- Select Type First ---')]
            self.fields['swot_pillar'].widget.attrs['disabled'] = True

        # Level 3: Factor
        if swot_type and pillar:
            self.fields['swot_factor'].choices = [('', '--- Select Factor ---')] + SwotChoicesService.get_factor_choices(swot_type, pillar)
            self.fields['swot_factor'].widget.attrs.pop('disabled', None)
        else:
            self.fields['swot_factor'].choices = [('', '--- Select Pillar First ---')]
            self.fields['swot_factor'].widget.attrs['disabled'] = True



class StrategyHierarchyForm(forms.ModelForm):
    # Include formula in the form explicitly
    formula = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'readonly': 'readonly',
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Select KPI to see formula'
        }),
        label="KPI Formula"
    )

    class Meta:
        model = StrategyHierarchy
        fields = ['strategic_perspective', 'focus_area', 'objective', 'kpi', 'formula']
        widgets = {
            'strategic_perspective': forms.Select(attrs={'class': 'form-control'}),
            'focus_area': forms.Select(attrs={'class': 'form-control'}),
            'objective': forms.Select(attrs={'class': 'form-control'}),
            'kpi': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # instantiate the service once
        service = StrategyHierarchyChoicesService()

        # Load current selections
        perspective = self.data.get('strategic_perspective') or getattr(self.instance, 'strategic_perspective', None)
        pillar = self.data.get('focus_area') or getattr(self.instance, 'focus_area', None)
        objective = self.data.get('objective') or getattr(self.instance, 'objective', None)
        kpi = self.data.get('kpi') or getattr(self.instance, 'kpi', None)

        # Populate dropdowns dynamically
        self.fields['strategic_perspective'].choices = [('', '--- Select Perspective ---')] + service.get_perspective_choices()

        if perspective:
            self.fields['focus_area'].choices = [('', '--- Select Pillar ---')] + service.get_pillar_choices(perspective)
        else:
            self.fields['focus_area'].choices = [('', '--- Select Perspective First ---')]
            self.fields['focus_area'].widget.attrs['disabled'] = True

        if perspective and pillar:
            self.fields['objective'].choices = [('', '--- Select Objective ---')] + service.get_objective_choices(perspective, pillar)
        else:
            self.fields['objective'].choices = [('', '--- Select Pillar First ---')]
            self.fields['objective'].widget.attrs['disabled'] = True

        if perspective and pillar and objective:
            self.fields['kpi'].choices = [('', '--- Select KPI ---')] + service.get_kpi_choices(perspective, pillar, objective)
        else:
            self.fields['kpi'].choices = [('', '--- Select Objective First ---')]
            self.fields['kpi'].widget.attrs['disabled'] = True

        # Auto-fill formula
        if perspective and pillar and objective and kpi:
            self.fields['formula'].initial = service.get_formula(perspective, pillar, objective, kpi)
        else:
            self.fields['formula'].initial = "Select a KPI to see the formula"
#
#
# class StakeholderForm(forms.ModelForm):
#     class Meta:
#         model = Stakeholder
#         exclude = ['organization_name']  # Exclude the organization field
#         widgets = {
#             'stakeholder_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stakeholder Name'}),
#             'stakeholder_type': forms.Select(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description'}),
#             'impact_level': forms.Select(attrs={'class': 'form-control'}),
#             'interest_level': forms.Select(attrs={'class': 'form-control'}),
#             'influence_score': forms.Select(attrs={'class': 'form-control'}),
#             'priority': forms.Select(attrs={'class': 'form-select', 'id': 'priority'}),
#             'satisfaction_level': forms.Select(attrs={'class': 'form-control'}),
#             'risk_level': forms.Select(attrs={'class': 'form-control'}),
#             'contribution_score': forms.Select(attrs={'class': 'form-select', 'id': 'contribution_score'}),
#             'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email, Phone, or Contact'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         # Add 'is-invalid' class to fields with errors
#         for field_name, field in self.fields.items():
#             css_classes = field.widget.attrs.get('class', 'form-control')
#             if field_name in self.errors:
#                 css_classes += ' is-invalid'
#             field.widget.attrs['class'] = css_classes

class StakeholderForm(forms.ModelForm):
    role = MultiSelectFormField(
        choices=Stakeholder.ROLE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True,
    )
    engagement_strategy = MultiSelectFormField(
        choices=Stakeholder.ENGAGEMENT_STRATEGY_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True,
    )

    class Meta:
        model = Stakeholder
        exclude = ['organization_name', 'stakeholder_code', 'slug', 'engagement_priority_score',
                   'is_key_stakeholder', 'requires_attention', 'created_at', 'updated_at']
        widgets = {
            'stakeholder_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stakeholder Name'}),
            'stakeholder_type': forms.Select(attrs={'class': 'form-select'}),
            'stakeholder_category': forms.Select(attrs={'class': 'form-select'}),
            'primary_role': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Internal notes'}),
            'impact_level': forms.Select(attrs={'class': 'form-select'}),
            'interest_level': forms.Select(attrs={'class': 'form-select'}),
            'influence_score': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'satisfaction_level': forms.Select(attrs={'class': 'form-select'}),
            'risk_level': forms.Select(attrs={'class': 'form-select'}),
            'contribution_score': forms.Select(attrs={'class': 'form-select'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email, Phone, or Contact'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'relationship_status': forms.Select(attrs={'class': 'form-select'}),
            'last_engagement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_engagement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Organization-specific filtering
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['aligned_objectives'].queryset = StrategyHierarchy.objects.filter(organization_name=org)
        else:
            self.fields['aligned_objectives'].queryset = StrategyHierarchy.objects.none()

        # Add Bootstrap validation classes
        for field_name, field in self.fields.items():
            css_classes = field.widget.attrs.get('class', 'form-control')
            if field_name in self.errors:
                css_classes += ' is-invalid'
            field.widget.attrs['class'] = css_classes


class StrategicCycleForm(forms.ModelForm):
    class Meta:
        model = StrategicCycle
        fields = [
            'time_horizon',
            'time_horizon_type',
            'start_date',
            'end_date',
        ]
        widgets = {
            'time_horizon': forms.Select(attrs={'class': 'form-select'}),
            'time_horizon_type': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Optional: style help text
        for field_name, field in self.fields.items():
            if field.help_text:
                field.help_text = f'<span style="color: blue; font-style: italic;">{field.help_text}</span>'


class StrategicActionPlanForm(forms.ModelForm):
    class Meta:
        model = StrategicActionPlan
        exclude = ['organization_name', 'strategic_cycle', 'improvement_needed']
        widgets = {
            'strategy_hierarchy': forms.Select(attrs={'class': 'form-control'}),
            # 'responsible_bodies': forms.CheckboxSelectMultiple(),
            'indicator_type': forms.Select(attrs={'class': 'form-control'}),
            'direction_of_change': forms.Select(attrs={'class': 'form-control'}),
            'baseline': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter baseline value'}),
            'target': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter target value'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Weight'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.cycle = kwargs.pop('cycle', None)  # cycle passed from view
        super().__init__(*args, **kwargs)

        # Filter by organization
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['strategy_hierarchy'].queryset = StrategyHierarchy.objects.filter(organization_name=org)
            self.fields['responsible_bodies'].queryset = Stakeholder.objects.filter(organization_name=org)
        else:
            self.fields['strategy_hierarchy'].queryset = StrategyHierarchy.objects.none()
            self.fields['responsible_bodies'].queryset = Stakeholder.objects.none()

        # Add bootstrap error styling
        for field_name, field in self.fields.items():
            css_classes = field.widget.attrs.get('class', 'form-control')
            if field_name in self.errors:
                css_classes += ' is-invalid'
            field.widget.attrs['class'] = css_classes

        # If cycle is passed, store it in a hidden field
        if self.cycle:
            self.fields['strategic_cycle'] = forms.ModelChoiceField(
                queryset=StrategicCycle.objects.filter(pk=self.cycle.pk),
                initial=self.cycle.pk,
                widget=forms.HiddenInput()
            )
        # If editing an existing plan, keep its cycle
        elif self.instance.pk and self.instance.strategic_cycle:
            self.fields['strategic_cycle'] = forms.ModelChoiceField(
                queryset=StrategicCycle.objects.filter(pk=self.instance.strategic_cycle.pk),
                initial=self.instance.strategic_cycle.pk,
                widget=forms.HiddenInput()
            )



class InitiativePlanningForm(forms.ModelForm):
    class Meta:
        model = InitiativePlanning
        exclude = ['organization_name',]
        widgets = {
            'initiative_focus_area': forms.Select(attrs={'class': 'form-select'}),
            'initiative_dimension': forms.Select(attrs={'class': 'form-select'}),
            'initiative_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'total_budget_planned': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter target value'}),
            'total_hr_planned': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter target value'}),

            'priority': forms.Select(attrs={'class': 'form-select'}),
            'impact': forms.Select(attrs={'class': 'form-select'}),
            'likelihood': forms.Select(attrs={'class': 'form-select'}),
            'risk_level': forms.Select(attrs={'class': 'form-select'}),
            'baseline_status': forms.Select(attrs={'class': 'form-select'}),
            'target_status': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'aligned_objectives': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Organization-specific filtering
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['aligned_objectives'].queryset = StrategyHierarchy.objects.filter(organization_name=org)
        else:
            self.fields['aligned_objectives'].queryset = StrategyHierarchy.objects.none()

        # --- Cascading dropdown logic ---
        # Current selections
        initiative_focus_area = self.data.get('initiative_focus_area') or getattr(self.instance, 'initiative_focus_area', None)

        # --- Pillar dropdown ---
        self.fields['initiative_focus_area'].choices = [('', '--- Select Pillar ---')] + \
            InitiativePlanningChoicesService.get_initiative_focus_area_choices()

        # --- Area dropdown ---
        if initiative_focus_area:
            self.fields['initiative_dimension'].choices = [('', '--- Select Area ---')] + \
                InitiativePlanningChoicesService.get_area_choices(initiative_focus_area)
            self.fields['initiative_dimension'].widget.attrs.pop('disabled', None)
        else:
            self.fields['initiative_dimension'].choices = [('', '--- Select Pillar First ---')]
            self.fields['initiative_dimension'].widget.attrs['disabled'] = True




class InitiativeReportForm(forms.ModelForm):
    class Meta:
        model = InitiativeReport
        exclude = ['organization_name']  # Will be set in view
        widgets = {
            'initiative_planning': forms.Select(attrs={'class': 'form-control'}),
            'report_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'achieved_status': forms.Select(attrs={'class': 'form-control'}),
            'total_budget_spent': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Enter amount spent'
            }),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes'}),
        }

    error_css_class = 'text-danger'
    required_css_class = 'font-weight-bold'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Filter initiatives by the user's organization
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['initiative_planning'].queryset = InitiativePlanning.objects.filter(organization_name=org)
        else:
            self.fields['initiative_planning'].queryset = InitiativePlanning.objects.none()

        # Add Bootstrap 'is-invalid' class dynamically for fields with errors
        for field_name, field in self.fields.items():
            css_classes = field.widget.attrs.get('class', 'form-control')
            if self.errors.get(field_name):
                css_classes += ' is-invalid'
            field.widget.attrs['class'] = css_classes




class InitiativeResourceItemPlanForm(forms.ModelForm):
    class Meta:
        model = InitiativeResourceItemPlan
        fields = ['initiative_name', 'resource_type', 'resource_name', 'resource_required']
        widgets = {
            'initiative_name': forms.Select(attrs={'class': 'form-control'}),
            'resource_type': forms.Select(attrs={'class': 'form-control'}),
            'resource_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter resource name (e.g. HR, Equipment)'
            }),
            'resource_required': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Enter planned amount'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Filter initiative choices by organization
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['initiative_name'].queryset = InitiativePlanning.objects.filter(organization_name=org)
        else:
            self.fields['initiative_name'].queryset = InitiativePlanning.objects.none()

        # Add invalid class for errors
        for field_name, field in self.fields.items():
            if field_name in self.errors:
                field.widget.attrs['class'] += ' is-invalid'

    error_css_class = 'text-danger'
    required_css_class = 'font-weight-bold'



class InitiativeResourceItemReportForm(forms.ModelForm):
    class Meta:
        model = InitiativeResourceItemReport
        fields = ['initiative_resource_plan', 'resource_used', 'notes']
        widgets = {
            'initiative_resource_plan': forms.Select(attrs={'class': 'form-control'}),
            'resource_used': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Enter actual used amount'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional notes or remarks...'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Filter resource plans by organization
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['initiative_resource_plan'].queryset = InitiativeResourceItemPlan.objects.filter(organization=org)
        else:
            self.fields['initiative_resource_plan'].queryset = InitiativeResourceItemPlan.objects.none()

        # Bootstrap invalid styling
        for field_name, field in self.fields.items():
            if field_name in self.errors:
                field.widget.attrs['class'] += ' is-invalid'

    error_css_class = 'text-danger'
    required_css_class = 'font-weight-bold'



#strategy report

class StrategicReportForm(forms.ModelForm):
    action_plan = forms.ModelChoiceField(
        queryset=StrategicActionPlan.objects.none(),  # initially empty
        label="Action Plan",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'title': '',  # optional, will set via __init__
        }),
        empty_label="Select Action Plan"
    )

    class Meta:
        model = StrategicReport
        fields = [
            'action_plan', 'achievement', 'data_source',
            'data_collector', 'progress_summary', 'performance_summary',
            'challenges', 'successes', 'lessons_learned', 'status',
        ]
        widgets = {
            'achievement': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data_source': forms.TextInput(attrs={'class': 'form-control'}),
            'data_collector': forms.TextInput(attrs={'class': 'form-control'}),
            'progress_summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'performance_summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'challenges': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'successes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'lessons_learned': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.cycle = kwargs.pop('cycle', None)
        super().__init__(*args, **kwargs)

        # Filter by user organization
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            qs = StrategicActionPlan.objects.filter(organization_name=org)
        else:
            qs = StrategicActionPlan.objects.none()

        # Optionally filter further by cycle if you need it
        if self.cycle:
            qs = qs.filter(strategic_cycle=self.cycle)


        # If we're editing and the instance has an action_plan, ensure it's included
        instance_plan = getattr(self.instance, 'action_plan', None)
        if instance_plan:
            qs = (qs | StrategicActionPlan.objects.filter(pk=instance_plan.pk)).distinct()

        self.fields['action_plan'].queryset = qs




class SwotReportForm(forms.ModelForm):
    strategic_report_period = forms.ModelChoiceField(
        queryset=StrategicReport.objects.none(),
        label="Strategic Report Period",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Strategic Report"
    )

    class Meta:
        model = SwotReport
        fields = [
            'strategic_report_period', 'swot_type', 'swot_pillar', 'swot_factor',
            'priority', 'impact', 'likelihood', 'description'
        ]
        widgets = {
            'swot_type': forms.Select(attrs={'class': 'form-control'}),
            'swot_pillar': forms.Select(attrs={'class': 'form-control'}),
            'swot_factor': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'impact': forms.Select(attrs={'class': 'form-control'}),
            'likelihood': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # ---------------- Filter unique by action_plan ----------------
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            reports = StrategicReport.objects.filter(organization_name=org).order_by('action_plan', '-id')

            unique_ids = []
            seen = set()
            for report in reports:
                if report.action_plan_id not in seen:
                    seen.add(report.action_plan_id)
                    unique_ids.append(report.id)

            self.fields['strategic_report_period'].queryset = StrategicReport.objects.filter(id__in=unique_ids)
        else:
            self.fields['strategic_report_period'].queryset = StrategicReport.objects.none()

        # ---------------- Cascade dropdown logic ----------------
        swot_type = self.data.get('swot_type') or getattr(self.instance, 'swot_type', None)
        pillar = self.data.get('swot_pillar') or getattr(self.instance, 'swot_pillar', None)

        # Level 1: SWOT Type
        self.fields['swot_type'].choices = [('', '--- Select SWOT Type ---')] + SwotChoicesService.get_swot_type_choices()

        # Level 2: Pillar
        if swot_type:
            self.fields['swot_pillar'].choices = [('', '--- Select Pillar ---')] + SwotChoicesService.get_pillar_choices(swot_type)
            self.fields['swot_pillar'].widget.attrs.pop('disabled', None)
        else:
            self.fields['swot_pillar'].choices = [('', '--- Select Type First ---')]
            self.fields['swot_pillar'].widget.attrs['disabled'] = True

        # Level 3: Factor
        if swot_type and pillar:
            self.fields['swot_factor'].choices = [('', '--- Select Factor ---')] + SwotChoicesService.get_factor_choices(swot_type, pillar)
            self.fields['swot_factor'].widget.attrs.pop('disabled', None)
        else:
            self.fields['swot_factor'].choices = [('', '--- Select Pillar First ---')]
            self.fields['swot_factor'].widget.attrs['disabled'] = True



#
# class RiskManagementForm(forms.ModelForm):
#     class Meta:
#         model = RiskManagement
#         exclude = ['mitigation_action', 'severity_score', 'organization_name', 'created_at', 'updated_at']
#         widgets = {
#             'risk_category': forms.Select(attrs={'class': 'form-select'}),
#             'risk_name': forms.Select(attrs={'class': 'form-select'}),
#             'likelihood': forms.Select(attrs={'class': 'form-select'}),
#             'impact': forms.Select(attrs={'class': 'form-select'}),
#             'status': forms.Select(attrs={'class': 'form-select'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super().__init__(*args, **kwargs)
#
#         risk_category = self.data.get('risk_category') or getattr(self.instance, 'risk_category', None)
#         self.fields['risk_category'].choices = [('', '--- Select Risk Category ---')] + RiskChoicesService.get_risk_category_choices()
#         self.fields['risk_name'].choices = [('', '--- Select Risk Name ---')] + (RiskChoicesService.get_risk_name_choices(risk_category) if risk_category else [])
#
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if self.request and hasattr(self.request.user, 'organization_name'):
#             instance.organization_name = self.request.user.organization_name  # Must be instance of OrganizationalProfile
#         # Auto-fill mitigation
#         risk_category = self.cleaned_data.get('risk_category')
#         risk_name = self.cleaned_data.get('risk_name')
#         if risk_category and risk_name:
#             instance.mitigation_action = RiskChoicesService.get_mitigation_action(risk_category, risk_name)
#         if commit:
#             instance.save()
#         return instance


#
# class RiskManagementForm(forms.ModelForm):
#     class Meta:
#         model = RiskManagement
#         exclude = ['mitigation_action', 'severity_score', 'organization_name', 'created_at', 'updated_at']
#         widgets = {
#             'risk_category': forms.Select(attrs={'class': 'form-select'}),
#             'risk_name': forms.Select(attrs={'class': 'form-select'}),
#             'likelihood': forms.Select(attrs={'class': 'form-select'}),
#             'impact': forms.Select(attrs={'class': 'form-select'}),
#             'status': forms.Select(attrs={'class': 'form-select'}),
#             'strategic_cycle': forms.Select(attrs={'class': 'form-select'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super().__init__(*args, **kwargs)
#
#         # --- Filter Strategic Cycle based on organization ---
#         if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
#             org = self.request.user.organization_name
#             self.fields['strategic_cycle'].queryset = StrategicCycle.objects.filter(organization_name=org)
#         else:
#             self.fields['strategic_cycle'].queryset = StrategicCycle.objects.none()
#
#         # --- Risk Category and Risk Name cascading ---
#         risk_category = self.data.get('risk_category') or getattr(self.instance, 'risk_category', None)
#         self.fields['risk_category'].choices = [('', '--- Select Risk Category ---')] + RiskChoicesService.get_risk_category_choices()
#         self.fields['risk_name'].choices = [('', '--- Select Risk Name ---')] + (
#             RiskChoicesService.get_risk_name_choices(risk_category) if risk_category else []
#         )
#
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#
#         # Assign organization automatically
#         if self.request and hasattr(self.request.user, 'organization_name'):
#             instance.organization_name = self.request.user.organization_name  # Must be OrganizationalProfile instance
#
#         # Auto-fill mitigation action
#         risk_category = self.cleaned_data.get('risk_category')
#         risk_name = self.cleaned_data.get('risk_name')
#         if risk_category and risk_name:
#             instance.mitigation_action = RiskChoicesService.get_mitigation_action(risk_category, risk_name)
#
#         if commit:
#             instance.save()
#
#         return instance


class RiskManagementForm(forms.ModelForm):
    class Meta:
        model = RiskManagement
        exclude = ['mitigation_action', 'severity_score', 'organization_name', 'created_at', 'updated_at']
        widgets = {
            'risk_category': forms.Select(attrs={'class': 'form-select'}),
            'risk_name': forms.Select(attrs={'class': 'form-select'}),
            'likelihood': forms.Select(attrs={'class': 'form-select'}),
            'impact': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'strategic_cycle': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Filter strategic_cycle based on user's organization
        if self.request and self.request.user.is_authenticated and hasattr(self.request.user, 'organization_name'):
            org = self.request.user.organization_name
            self.fields['strategic_cycle'].queryset = StrategicCycle.objects.filter(organization_name=org)
        else:
            self.fields['strategic_cycle'].queryset = StrategicCycle.objects.none()

        # Risk category & name logic
        risk_category = self.data.get('risk_category') or getattr(self.instance, 'risk_category', None)
        self.fields['risk_category'].choices = [('', '--- Select Risk Category ---')] + RiskChoicesService.get_risk_category_choices()
        self.fields['risk_name'].choices = [('', '--- Select Risk Name ---')] + (RiskChoicesService.get_risk_name_choices(risk_category) if risk_category else [])

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Assign organization
        if self.request and hasattr(self.request.user, 'organization_name'):
            instance.organization_name = self.request.user.organization_name
        # Auto-fill mitigation action
        risk_category = self.cleaned_data.get('risk_category')
        risk_name = self.cleaned_data.get('risk_name')
        if risk_category and risk_name:
            instance.mitigation_action = RiskChoicesService.get_mitigation_action(risk_category, risk_name)
        if commit:
            instance.save()
        return instance
