class ValuesService:
    CATEGORY_CHOICES = [
        'People & Culture',
        'Customer & Market',
        'Sustainability & Ethics',
        'Governance & Strategy',
        'Technology & Digital',
        'Finance & Risk',
        'Innovation & Growth',
        'Operations & Quality',
        'Brand & Reputation',
        'Community & Social Responsibility',
    ]

    VALUE_CHOICES = [
        # People & Culture
        ('People & Culture', [
            ('integrity', 'Integrity'),
            ('respect', 'Respect'),
            ('empathy', 'Empathy'),
            ('collaboration', 'Collaboration'),
            ('excellence', 'Excellence'),
            ('adaptability', 'Adaptability'),
            ('diversity_inclusion', 'Diversity & Inclusion'),
            ('courage', 'Courage'),
            ('humility', 'Humility'),
            ('resilience', 'Resilience'),
            ('accountability', 'Accountability'),
            ('learning_mindset', 'Continuous Learning'),
        ]),
        # Customer & Market
        ('Customer & Market', [
            ('customer_focus', 'Customer Focus'),
            ('trustworthiness', 'Trustworthiness'),
            ('quality', 'Quality'),
            ('responsiveness', 'Responsiveness'),
            ('fairness', 'Fairness'),
            ('loyalty', 'Loyalty'),
            ('service_orientation', 'Service Orientation'),
            ('customer_innovation', 'Customer-Centric Innovation'),
        ]),
        # Sustainability & Ethics
        ('Sustainability & Ethics', [
            ('sustainability', 'Sustainability'),
            ('responsibility', 'Responsibility'),
            ('ethics', 'Ethics'),
            ('transparency', 'Transparency'),
            ('equity', 'Equity'),
            ('community_focus', 'Community Focus'),
            ('environmental_stewardship', 'Environmental Stewardship'),
            ('social_responsibility', 'Social Responsibility'),
        ]),
        # Governance & Strategy
        ('Governance & Strategy', [
            ('strategic_thinking', 'Strategic Thinking'),
            ('vision', 'Vision'),
            ('integrity_leadership', 'Integrity in Leadership'),
            ('collaboration_governance', 'Collaboration'),
            ('risk_management', 'Risk Management'),
            ('accountability_governance', 'Accountability'),
            ('long_term_orientation', 'Long-Term Orientation'),
        ]),
        # Technology & Digital
        ('Technology & Digital', [
            ('innovation', 'Innovation'),
            ('responsible_tech_use', 'Responsible Use of Technology'),
            ('digital_adaptability', 'Digital Adaptability'),
            ('data_driven', 'Data-Driven Decision Making'),
            ('tech_learning', 'Continuous Tech Learning'),
            ('automation_ethics', 'Ethical Automation'),
        ]),
        # Finance & Risk
        ('Finance & Risk', [
            ('prudence', 'Prudence'),
            ('financial_responsibility', 'Financial Responsibility'),
            ('integrity_finance', 'Integrity'),
            ('risk_awareness', 'Risk Awareness'),
            ('transparency_finance', 'Transparency'),
            ('compliance', 'Regulatory Compliance'),
            ('budget_discipline', 'Budget Discipline'),
            ('cost_efficiency', 'Cost Efficiency'),
        ]),
        # Innovation & Growth
        ('Innovation & Growth', [
            ('creativity', 'Creativity'),
            ('entrepreneurial_mindset', 'Entrepreneurial Mindset'),
            ('agility', 'Agility'),
            ('continuous_improvement', 'Continuous Improvement'),
            ('visionary', 'Visionary Thinking'),
            ('opportunity_seeking', 'Opportunity Seeking'),
            ('collaboration_innovation', 'Collaborative Innovation'),
        ]),
        # Operations & Quality
        ('Operations & Quality', [
            ('efficiency', 'Efficiency'),
            ('quality_focus', 'Quality Focus'),
            ('process_excellence', 'Process Excellence'),
            ('customer_satisfaction', 'Customer Satisfaction'),
            ('safety', 'Safety'),
            ('reliability', 'Reliability'),
            ('lean_practices', 'Lean Practices'),
        ]),
        # Brand & Reputation
        ('Brand & Reputation', [
            ('brand_integrity', 'Brand Integrity'),
            ('reliability_reputation', 'Reliability'),
            ('trust', 'Trust'),
            ('social_image', 'Social Image'),
            ('authenticity', 'Authenticity'),
            ('emotional_connection', 'Emotional Connection'),
        ]),
        # Community & Social Responsibility
        ('Community & Social Responsibility', [
            ('community_engagement', 'Community Engagement'),
            ('volunteering', 'Volunteering'),
            ('philanthropy', 'Philanthropy'),
            ('diversity_advocacy', 'Diversity Advocacy'),
            ('social_impact', 'Social Impact'),
            ('education_support', 'Education Support'),
        ]),
    ]