class StrategyHierarchyChoicesService:
    # Define the complete hierarchy in a single structure
    STRATEGY_MAP_HIERARCHY = {
        "Financial Perspective": {

            # ---------------- 1. REVENUE GROWTH & DIVERSIFICATION ----------------
            "Revenue Growth & Diversification": {
                "Enhance Total Revenue Performance": {
                    "Total revenue growth (%)": "(Current revenue - Previous revenue) / Previous revenue * 100",
                    "Quarterly revenue growth rate (%)": "Quarter-over-quarter revenue increase percentage",
                    "Annual revenue growth acceleration": "Year-over-year growth rate improvement",
                    "Revenue per customer growth ($)": "(Current revenue/customer - Previous) / Previous * 100"
                },
                "Strengthen Market Share & Positioning": {
                    "Market share growth (%)": "(Current market share - Previous market share) / Previous * 100",
                    "Revenue in target segments growth (%)": "Growth in priority customer segments",
                    "Geographic expansion revenue ($)": "Revenue from new geographic markets",
                    "Competitive win rate (%)": "(Contracts won / Total bids) * 100"
                },
                "Accelerate New Product/Service Revenue": {
                    "Revenue from innovations (%)": "(Revenue from new products / Total revenue) * 100",
                    "Time-to-revenue for new offerings (months)": "Speed from launch to revenue generation",
                    "R&D ROI from new products (%)": "(Revenue from new products / R&D investment) * 100",
                    "Product adoption rate acceleration": "Faster customer adoption of new offerings"
                },
                "Diversify Revenue Streams": {
                    "Recurring revenue ratio (%)": "(Subscription revenue / Total revenue) * 100",
                    "Number of revenue streams (#)": "Count of distinct revenue sources",
                    "Revenue concentration risk index": "1 - (Revenue from top 3 products / Total revenue)",
                    "Passive income growth (%)": "Growth in non-operational revenue streams"
                }
            },

            # ---------------- 2. COST MANAGEMENT & EFFICIENCY ----------------
            "Cost Management & Efficiency": {
                "Enhance Operational Efficiency": {
                    "Cost per unit reduction (%)": "(Current cost/unit - Previous) / Previous * 100",
                    "Labor productivity growth (%)": "(Current output/employee - Previous) / Previous * 100",
                    "Process efficiency improvement (%)": "Reduction in process cycle time",
                    "Energy efficiency ratio": "Output per unit of energy consumed"
                },
                "Implement Strategic Cost Reduction": {
                    "Operating expense ratio (%)": "(Operating expenses / Revenue) * 100",
                    "Cost savings achievement rate (%)": "(Actual savings / Target savings) * 100",
                    "Overhead cost optimization (%)": "Reduction in administrative costs",
                    "Zero-based budgeting effectiveness": "Cost justification and optimization"
                },
                "Optimize Procurement & Supply Chain": {
                    "Procurement cost reduction (%)": "Savings from strategic sourcing",
                    "Supplier performance index": "Weighted score of supplier metrics",
                    "Supply chain cost as % of revenue": "(Total supply chain cost / Revenue) * 100",
                    "Inventory carrying cost reduction (%)": "Reduction in holding costs"
                },
                "Enhance Resource Utilization": {
                    "Asset utilization rate (%)": "(Productive time / Total available time) * 100",
                    "Capacity utilization improvement (%)": "Increase in production capacity usage",
                    "Technology ROI (%)": "(Benefits from technology / Technology cost) * 100",
                    "Space utilization efficiency": "Revenue generated per square foot"
                }
            },

            # ---------------- 3. PROFITABILITY OPTIMIZATION ----------------
            "Profitability Optimization": {
                "Maximize Net Profit Performance": {
                    "Net profit margin (%)": "(Net income / Revenue) * 100",
                    "Net profit growth rate (%)": "(Current net profit - Previous) / Previous * 100",
                    "Earnings quality score": "Sustainability and predictability of earnings",
                    "Return on revenue (%)": "Net income / Revenue * 100"
                },
                "Enhance Gross Margin Performance": {
                    "Gross margin (%)": "(Revenue - COGS) / Revenue * 100",
                    "Product margin optimization": "Improvement in lowest-margin products",
                    "Direct cost efficiency (%)": "Reduction in direct production costs",
                    "Pricing strategy effectiveness": "Margin improvement from pricing changes"
                },
                "Improve Operating Profitability": {
                    "EBITDA margin (%)": "(EBITDA / Revenue) * 100",
                    "Operating leverage effect": "Revenue growth vs. operating cost growth",
                    "Departmental profitability": "Profit contribution by business unit",
                    "Break-even point reduction": "Lower revenue required for profitability"
                },
                "Optimize Contribution Margins": {
                    "Average contribution margin (%)": "(Revenue - Variable costs) / Revenue * 100",
                    "Customer profitability segmentation": "Profitability by customer tier",
                    "Product portfolio margin mix": "Weighted average margin across products",
                    "Variable cost control effectiveness": "Reduction in direct variable costs"
                }
            },

            # ---------------- 4. LIQUIDITY & CASH FLOW MANAGEMENT ----------------
            "Liquidity & Cash Flow Management": {
                "Enhance Operating Cash Flow": {
                    "Operating cash flow growth (%)": "(Current OCF - Previous OCF) / Previous * 100",
                    "Cash flow margin (%)": "(Operating cash flow / Revenue) * 100",
                    "Free cash flow generation ($)": "Operating cash flow - Capital expenditures",
                    "Cash flow predictability index": "Variance in monthly cash flows"
                },
                "Optimize Working Capital Efficiency": {
                    "Working capital ratio improvement": "Current assets / Current liabilities",
                    "Cash conversion cycle reduction (days)": "DSO + Inventory days - DPO",
                    "Working capital turnover ratio": "Revenue / Average working capital",
                    "Excess working capital reduction ($)": "Optimization of current assets"
                },
                "Maintain Strong Liquidity Position": {
                    "Current ratio stability": "Current assets / Current liabilities",
                    "Quick ratio improvement": "(Current assets - Inventory) / Current liabilities",
                    "Liquidity buffer adequacy (days)": "Cash available for daily operations",
                    "Short-term financial flexibility": "Access to emergency funding"
                },
                "Improve Cash Flow Forecasting": {
                    "Cash forecast accuracy (%)": "(1 - |Forecast - Actual| / Actual) * 100",
                    "Cash flow timing optimization": "Alignment of inflows and outflows",
                    "Working capital predictability": "Accuracy of working capital projections",
                    "Scenario planning effectiveness": "Preparedness for cash flow variations"
                }
            },

            # ---------------- 5. FINANCIAL STABILITY & RISK MANAGEMENT ----------------
            "Financial Stability & Risk Management": {
                "Strengthen Balance Sheet Structure": {
                    "Debt-to-equity ratio optimization": "Total liabilities / Shareholders' equity",
                    "Asset quality improvement": "Percentage of performing assets",
                    "Capital structure efficiency": "Optimal mix of debt and equity",
                    "Tangible net worth growth ($)": "Increase in real asset value"
                },
                "Enhance Solvency & Creditworthiness": {
                    "Interest coverage ratio": "EBIT / Interest expense",
                    "Debt service coverage ratio": "Operating income / Total debt service",
                    "Credit rating improvement": "Upgrade in credit agency ratings",
                    "Borrowing cost reduction (%)": "Decrease in interest expenses"
                },
                "Implement Robust Risk Management": {
                    "Financial risk exposure reduction": "Decrease in volatility-sensitive positions",
                    "Hedging effectiveness (%)": "Risk reduction from hedging strategies",
                    "Compliance adherence rate (%)": "(Compliant processes / Total processes) * 100",
                    "Risk-adjusted return improvement": "Return per unit of risk taken"
                },
                "Strengthen Business Continuity Planning": {
                    "Contingency fund adequacy (%)": "(Contingency funds / Risk exposure) * 100",
                    "Disaster recovery readiness": "Time to restore critical operations",
                    "Insurance coverage optimization": "Adequacy of risk transfer mechanisms",
                    "Stress testing frequency (#)": "Number of risk scenario analyses"
                }
            },

            # ---------------- 6. ECONOMIC DEVELOPMENT & IMPACT ----------------
            "Economic Development & Impact": {
                "Drive Regional Economic Growth": {
                    "GDP contribution growth (%)": "(Sector contribution / Total GDP) * 100",
                    "Regional economic multiplier effect": "Total economic impact / Direct investment",
                    "Local supplier development (#)": "Number of local businesses supported",
                    "Infrastructure development impact": "Economic benefits from infrastructure projects"
                },
                "Promote Trade & Commerce": {
                    "Export growth rate (%)": "(Current exports - Previous exports) / Previous * 100",
                    "Import substitution value ($)": "Value of locally produced substitutes",
                    "Trade balance improvement ($)": "Exports - Imports",
                    "Market access expansion (#)": "New markets entered for local products"
                },
                "Foster Innovation Ecosystem": {
                    "R&D investment growth (%)": "Increase in research and development spending",
                    "Technology transfer value ($)": "Commercial value of research成果",
                    "Startup ecosystem support (#)": "Number of new businesses incubated",
                    "Innovation cluster development": "Growth of innovation-focused zones"
                },
                "Enhance Economic Resilience": {
                    "Economic diversification index": "Number of viable economic sectors",
                    "Shock absorption capacity": "Ability to withstand economic disruptions",
                    "Regional economic stability": "Reduction in economic volatility",
                    "Long-term economic sustainability": "Sustainable growth indicators"
                }
            },

            # ---------------- 7. INFRASTRUCTURE DEVELOPMENT & MANAGEMENT ----------------
            "Infrastructure Development & Management": {
                "Enhance Physical Infrastructure": {
                    "Infrastructure quality index": "Condition and capacity of physical assets",
                    "Maintenance efficiency ratio": "(Planned maintenance / Total maintenance) * 100",
                    "Infrastructure utilization rate (%)": "(Actual usage / Design capacity) * 100",
                    "Asset lifecycle cost reduction (%)": "Reduction in total ownership costs"
                },
                "Optimize Digital Infrastructure": {
                    "Digital connectivity coverage (%)": "(Population with access / Total population) * 100",
                    "Network reliability index": "Uptime and performance metrics",
                    "Data infrastructure capacity (TB)": "Storage and processing capabilities",
                    "Cybersecurity infrastructure strength": "Protection level of digital assets"
                },
                "Improve Transportation & Logistics": {
                    "Transport efficiency index": "Cost and time efficiency of logistics",
                    "Logistics cost reduction (%)": "Decrease in supply chain transportation costs",
                    "Accessibility improvement (%)": "(Population with transport access / Total) * 100",
                    "Supply chain resilience": "Ability to maintain operations during disruptions"
                },
                "Enhance Public Infrastructure": {
                    "Public facility utilization (%)": "(Users served / Design capacity) * 100",
                    "Infrastructure investment ROI": "Economic return on public infrastructure",
                    "Community infrastructure access": "Percentage with access to basic services",
                    "Sustainable infrastructure ratio": "(Green infrastructure / Total infrastructure) * 100"
                }
            },

            # ---------------- 8. FUND & GRANT MANAGEMENT ----------------
            "Fund & Grant Management": {
                "Optimize Funding Acquisition": {
                    "Grant success rate (%)": "(Grants awarded / Grants applied) * 100",
                    "Funding diversification index": "Number of distinct funding sources",
                    "Average grant size growth ($)": "Increase in funding per successful application",
                    "Donor retention rate (%)": "(Retained donors / Total donors) * 100"
                },
                "Enhance Fund Utilization Efficiency": {
                    "Fund utilization rate (%)": "(Funds used effectively / Total funds) * 100",
                    "Program cost efficiency": "Outcomes achieved per spent",
                    "Administrative cost ratio (%)": "(Admin costs / Total expenses) * 100",
                    "Grant compliance rate (%)": "(Compliant expenditures / Total expenditures) * 100"
                },
                "Strengthen Donor Relations": {
                    "Donor satisfaction index": "Feedback from funding partners",
                    "Reporting timeliness (%)": "(Reports submitted on time / Total reports) * 100",
                    "Donor engagement level": "Depth of relationship with funders",
                    "Funding predictability index": "Stability of future funding streams"
                },
                "Improve Impact Measurement & Reporting": {
                    "Outcome achievement rate (%)": "(Target outcomes achieved / Total targets) * 100",
                    "Impact reporting quality": "Completeness and accuracy of impact reports",
                    "Cost per outcome ($)": "Total cost / Number of outcomes achieved",
                    "Stakeholder feedback integration": "Use of feedback in program improvement"
                }
            },

            # ---------------- 9. INVESTMENT MANAGEMENT & GROWTH ----------------
            "Investment Management & Growth": {
                "Enhance Investment Performance": {
                    "Portfolio ROI (%)": "(Total return / Total investment) * 100",
                    "Risk-adjusted returns": "Return per unit of risk",
                    "Investment diversification score": "Spread across asset classes and sectors",
                    "Alpha generation (%)": "Excess return over benchmark"
                },
                "Optimize Capital Allocation": {
                    "Return on invested capital (%)": "(NOPAT / Invested capital) * 100",
                    "Capital allocation efficiency": "Alignment with strategic priorities",
                    "Hurdle rate achievement (%)": "(Projects meeting targets / Total projects) * 100",
                    "Investment timing effectiveness": "Market entry and exit timing"
                },
                "Strengthen Strategic Investments": {
                    "Strategic alignment score": "Investment alignment with organizational goals",
                    "Long-term value creation": "Net present value of future benefits",
                    "Innovation investment ratio (%)": "(Innovation spending / Total investment) * 100",
                    "ESG investment performance": "Returns from sustainable investments"
                },
                "Improve Investment Decision Making": {
                    "Due diligence effectiveness": "Quality of investment analysis",
                    "Investment committee efficiency": "Speed and quality of decisions",
                    "Post-investment monitoring": "Ongoing performance tracking",
                    "Exit strategy success rate (%)": "(Successful exits / Total exits) * 100"
                }
            },

            # ---------------- 10. POVERTY REDUCTION & SOCIAL EQUITY ----------------
            "Poverty Reduction & Social Equity": {
                "Reduce Income Poverty": {
                    "Households above poverty line (#)": "Number lifted out of poverty",
                    "Income inequality reduction (Gini)": "Improvement in income distribution",
                    "Living wage achievement rate (%)": "(Employees earning living wage / Total) * 100",
                    "Economic mobility index": "Ability to move between income levels"
                },
                "Enhance Access to Basic Services": {
                    "Basic service coverage (%)": "(Population with access / Total population) * 100",
                    "Affordability index": "Cost of basic services relative to income",
                    "Service quality improvement": "Quality metrics for essential services",
                    "Digital inclusion rate (%)": "(Population with digital access / Total) * 100"
                },
                "Promote Social Protection": {
                    "Social safety net coverage (%)": "(Protected population / Vulnerable population) * 100",
                    "Disaster resilience index": "Community ability to withstand shocks",
                    "Vulnerability reduction rate": "Decrease in at-risk populations",
                    "Social cohesion indicators": "Community trust and cooperation levels"
                },
                "Strengthen Gender & Social Inclusion": {
                    "Gender parity index": "Equality across gender indicators",
                    "Minority inclusion rate (%)": "(Representation in opportunities / Population share) * 100",
                    "Disability access improvement": "Accessibility for people with disabilities",
                    "Social equity achievement": "Reduction in discrimination and barriers"
                }
            },

            # ---------------- 11. EMPLOYMENT GENERATION & WORKFORCE DEVELOPMENT ----------------
            "Employment Generation & Workforce Development": {
                "Create Quality Employment Opportunities": {
                    "Net jobs created (#)": "New employment opportunities generated",
                    "Employment growth rate (%)": "(Current employment - Previous) / Previous * 100",
                    "Job quality index": "Wages, benefits, and working conditions",
                    "Youth employment rate (%)": "(Employed youth / Total youth) * 100"
                },
                "Enhance Workforce Skills & Capabilities": {
                    "Skills development completion rate (%)": "(Trained individuals / Enrolled) * 100",
                    "Workforce productivity growth (%)": "Output per worker improvement",
                    "Technical certification rate (%)": "(Certified workers / Total workers) * 100",
                    "Digital literacy improvement": "Increase in technology skills"
                },
                "Promote Labor Market Inclusion": {
                    "Female employment rate (%)": "(Employed women / Working-age women) * 100",
                    "Disadvantaged group employment (#)": "Jobs for marginalized populations",
                    "Wage gap reduction (%)": "Closing of pay disparities",
                    "Workplace diversity index": "Representation across demographic groups"
                },
                "Strengthen Labor Market Efficiency": {
                    "Job matching efficiency": "Speed and quality of employment matches",
                    "Labor market information system": "Quality of employment data",
                    "Vocational training relevance": "Alignment with market needs",
                    "Employment retention rate (%)": "(Retained employees / Total employees) * 100"
                }
            },

            # ---------------- 12. FINANCIAL EFFICIENCY & PRODUCTIVITY ----------------
            "Financial Efficiency & Productivity": {
                "Optimize Financial Operations": {
                    "Financial process automation rate (%)": "(Automated processes / Total processes) * 100",
                    "Transaction processing cost ($)": "Cost per financial transaction",
                    "Financial close cycle time (days)": "Time for period-end closing",
                    "Error reduction in financial operations (%)": "Decrease in processing errors"
                },
                "Enhance Financial Technology Utilization": {
                    "FinTech adoption rate (%)": "(Digital finance users / Total users) * 100",
                    "Data analytics ROI in finance": "Value from financial data analysis",
                    "AI implementation in finance (%)": "(AI-driven processes / Total processes) * 100",
                    "Blockchain application value": "Benefits from distributed ledger technology"
                },
                "Improve Financial Decision Support": {
                    "Financial modeling accuracy (%)": "(Model accuracy / Total predictions) * 100",
                    "Decision support system utilization": "Usage of financial analysis tools",
                    "Scenario analysis effectiveness": "Quality of financial projections",
                    "Strategic planning integration": "Finance input in strategic decisions"
                },
                "Strengthen Financial Governance": {
                    "Internal control effectiveness": "Strength of financial controls",
                    "Audit finding resolution rate (%)": "(Resolved findings / Total findings) * 100",
                    "Policy compliance rate (%)": "(Compliant operations / Total operations) * 100",
                    "Financial transparency index": "Openness in financial reporting"
                }
            },

            # ---------------- 13. SUSTAINABLE FINANCE & ESG INTEGRATION ----------------
            "Sustainable Finance & ESG Integration": {
                "Enhance Environmental Financial Performance": {
                    "Green investment portfolio (%)": "(Sustainable investments / Total portfolio) * 100",
                    "Carbon cost reduction ($)": "Savings from emissions reduction",
                    "Circular economy revenue ($)": "Income from waste-to-value initiatives",
                    "Climate resilience investment ROI": "Return on climate adaptation spending"
                },
                "Strengthen Social Impact Finance": {
                    "Social impact bond performance": "Achievement of social outcome targets",
                    "Community investment returns": "Financial and social returns",
                    "Financial inclusion rate (%)": "(Population with financial access / Total) * 100",
                    "Affordable financing availability": "Access to credit for underserved groups"
                },
                "Optimize Governance-Linked Finance": {
                    "ESG compliance cost reduction": "Savings from proactive compliance",
                    "Stakeholder engagement value": "Financial benefits from engagement",
                    "Ethical investment growth (%)": "Increase in responsible investing",
                    "Transparency premium": "Value from open financial practices"
                },
                "Implement Sustainable Banking Practices": {
                    "Green loan portfolio growth (%)": "Increase in environmentally friendly lending",
                    "Social responsibility banking": "Community-focused financial services",
                    "Sustainable risk management": "Integration of ESG in risk assessment",
                    "Impact measurement sophistication": "Quality of sustainability reporting"
                },
            },
        },

        "Customer Perspective": {
            "Customer Acquisition & Market Reach": {
                "Increase qualified lead generation": {
                    "Number of qualified leads per month": "Count of leads meeting qualification criteria per month",
                    "Lead generation cost per channel": "Total marketing spend per channel / Number of leads generated per channel",
                    "Lead-to-opportunity conversion rate": "(Leads converted to opportunities / Total leads) * 100",
                    "Marketing qualified lead volume growth": "((Current MQL volume - Previous MQL volume) / Previous MQL volume) * 100"
                },
                "Improve conversion rates across channels": {
                    "Conversion rate by channel": "(Leads converted / Total leads per channel) * 100",
                    "Sales funnel efficiency": "(Opportunities closed / Total leads) * 100",
                    "Cost per acquisition reduction": "((Previous acquisition cost - Current acquisition cost) / Previous acquisition cost) * 100",
                    "Revenue per channel growth": "((Current revenue per channel - Previous revenue per channel) / Previous revenue per channel) * 100"
                },
                "Enhance digital marketing effectiveness": {
                    "Digital marketing ROI": "((Revenue from digital campaigns - Campaign cost) / Campaign cost) * 100",
                    "Click-through rate improvement": "((Current CTR - Previous CTR) / Previous CTR) * 100",
                    "Cost per click reduction": "((Previous CPC - Current CPC) / Previous CPC) * 100",
                    "Digital campaign conversion rate": "(Conversions / Total clicks) * 100"
                },
                "Build strong brand awareness": {
                    "Brand awareness survey": "(Surveyed awareness level / Total surveyed) * 100",
                    "Unaided brand recall": "(Respondents recalling brand without prompts / Total respondents) * 100",
                    "Social media reach and engagement": "(Total interactions on social media / Total followers) * 100",
                    "Share of voice in market": "(Brand mentions / Total market mentions) * 100"
                },
                "Target new customer segments": {
                    "Revenue from new segments": "Revenue generated from newly targeted segments",
                    "Customer acquisition rate for new segments": "(New customers acquired / Total potential customers in segment) * 100",
                    "Market penetration rate for new segments": "(Customers acquired / Total potential customers in segment) * 100",
                    "Segment growth percentage": "((Current segment revenue - Previous segment revenue) / Previous segment revenue) * 100"
                },
                "Expand into underserved markets": {
                    "Revenue from underserved markets": "Total revenue generated in underserved areas",
                    "Customer acquisition cost in new markets": "Marketing & sales spend in new markets / New customers acquired",
                    "Market share in new areas": "(Sales in new area / Total market size) * 100",
                    "Customer satisfaction in new markets": "(Sum of satisfaction ratings from new market customers / Number of respondents) * 100"
                },
                "Optimize customer onboarding": {
                    "Onboarding completion rate": "(Customers completing onboarding / Total new customers) * 100",
                    "Time to first value reduction": "Previous time to first value - Current time to first value",
                    "New customer satisfaction score": "(Sum of satisfaction ratings from new customers / Number of respondents) * 100",
                    "Onboarding cost per customer": "Total onboarding cost / Number of onboarded customers"
                },
                "Leverage customer referral programs": {
                    "Referral rate": "(Referrals / Total customers) * 100",
                    "Cost per acquired referral": "Total referral program cost / Referrals acquired",
                    "Referral program ROI": "((Revenue from referrals - Program cost) / Program cost) * 100",
                    "Customer lifetime value from referrals": "Average CLV of customers acquired via referrals"
                },
                "Improve website conversion funnels": {
                    "Website conversion rate": "(Conversions / Total website visitors) * 100",
                    "Cart abandonment rate reduction": "((Previous abandonment rate - Current abandonment rate) / Previous abandonment rate) * 100",
                    "Bounce rate improvement": "((Previous bounce rate - Current bounce rate) / Previous bounce rate) * 100",
                    "Page views per session increase": "Current average page views per session - Previous average page views per session"
                },
                "Execute targeted acquisition campaigns": {
                    "Campaign ROI": "((Revenue from campaign - Campaign cost) / Campaign cost) * 100",
                    "Customer acquisition cost per campaign": "Total campaign cost / Customers acquired from campaign",
                    "Conversion rate per campaign": "(Conversions / Total leads generated from campaign) * 100",
                    "Revenue generated from campaigns": "Total revenue attributable to specific campaigns"
                }
            },
            "Customer Satisfaction & Experience": {
                "Improve service quality standards": {
                    "Customer satisfaction score (CSAT)": "(Sum of satisfaction ratings / Number of survey respondents) * 100",
                    "Service quality index score": "((Sum of service metrics scores) / Maximum possible score) * 100",
                    "First-contact resolution rate": "(Issues resolved at first contact / Total issues) * 100",
                    "Service level agreement compliance": "(SLAs met / Total SLAs) * 100"
                },
                "Enhance customer support responsiveness": {
                    "Average response time reduction": "Previous average response time - Current average response time",
                    "Support ticket backlog reduction": "Previous backlog - Current backlog",
                    "Customer satisfaction post-support": "(Sum of satisfaction ratings post-support / Number of respondents) * 100",
                    "Resolution time improvement": "Previous average resolution time - Current average resolution time"
                },
                "Personalize customer interactions": {
                    "Personalization effectiveness score": "((Number of personalized interactions leading to desired outcome) / Total personalized interactions) * 100",
                    "Customer engagement rate improvement": "((Current engagement rate - Previous engagement rate) / Previous engagement rate) * 100",
                    "Repeat purchase rate increase": "((Current repeat purchases - Previous repeat purchases) / Previous repeat purchases) * 100",
                    "Upsell conversion rate improvement": "((Current upsell conversions - Previous upsell conversions) / Previous upsell conversions) * 100"
                },
                "Streamline customer journey mapping": {
                    "Customer effort score reduction": "((Previous effort score - Current effort score) / Previous effort score) * 100",
                    "Journey completion rate improvement": "((Current journey completions - Previous journey completions) / Previous journey completions) * 100",
                    "Touchpoint satisfaction scores": "(Sum of touchpoint satisfaction ratings / Number of touchpoints) * 100",
                    "Process step reduction in journey": "Previous number of steps - Current number of steps"
                },
                "Improve complaint resolution processes": {
                    "Complaint resolution time reduction": "((Previous resolution time - Current resolution time) / Previous resolution time) * 100",
                    "First-contact resolution rate": "(Issues resolved at first contact / Total issues) * 100",
                    "Customer satisfaction post-complaint": "(Sum of satisfaction ratings post-complaint / Number of respondents) * 100",
                    "Complaint escalation rate reduction": "((Previous escalations - Current escalations) / Previous escalations) * 100"
                },
                "Enhance after-sales service": {
                    "After-sales satisfaction score": "(Sum of satisfaction ratings after service / Number of respondents) * 100",
                    "Service follow-up completion rate": "(Follow-ups completed / Total required follow-ups) * 100",
                    "Repeat purchase rate improvement": "((Current repeat purchases - Previous repeat purchases) / Previous repeat purchases) * 100",
                    "Warranty claim resolution time": "Average time to resolve warranty claims"
                },
                "Strengthen customer communication": {
                    "Communication open rate": "(Emails opened / Total emails sent) * 100",
                    "Click-through rate improvement": "((Current CTR - Previous CTR) / Previous CTR) * 100",
                    "Customer engagement score": "((Sum of interactions per customer) / Total customers) * 100",
                    "Response rate to outreach": "(Responses received / Total outreach attempts) * 100"
                },
                "Implement customer feedback systems": {
                    "Feedback collection rate": "(Feedback collected / Total customers solicited) * 100",
                    "Actionable insights implemented": "(Implemented insights / Total insights collected) * 100",
                    "Feedback response time reduction": "((Previous response time - Current response time) / Previous response time) * 100",
                    "Customer perception of being heard": "(Sum of survey scores on being heard / Number of respondents) * 100"
                },
                "Improve product usability": {
                    "Product usability score": "(Sum of usability ratings / Number of respondents) * 100",
                    "Customer training time reduction": "((Previous training hours - Current training hours) / Previous training hours) * 100",
                    "Support calls related to usability": "(Number of calls about usability / Total support calls) * 100",
                    "Feature adoption rate improvement": "((Current adoption rate - Previous adoption rate) / Previous adoption rate) * 100"
                },
                "Enhance digital experience": {
                    "Digital experience score": "(Sum of digital experience ratings / Number of respondents) * 100",
                    "Mobile app rating improvement": "((Current rating - Previous rating) / Previous rating) * 100",
                    "Website satisfaction score": "(Sum of website satisfaction ratings / Number of respondents) * 100",
                    "Digital channel engagement rate": "(Interactions via digital channels / Total users) * 100"
                }
            },
            "Customer Loyalty & Retention": {
                "Reduce customer churn rate": {
                    "Churn rate reduction": "((Previous churn rate - Current churn rate) / Previous churn rate) * 100",
                    "Customer lifetime value improvement": "((Current CLV - Previous CLV) / Previous CLV) * 100",
                    "Revenue retention percentage": "(Revenue retained from existing customers / Total revenue) * 100",
                    "Lost customer recovery rate": "(Recovered customers / Total lost customers) * 100"
                },
                "Increase customer retention percentage": {
                    "Customer retention rate by segment": "(Retained customers / Total customers in segment) * 100",
                    "Repeat purchase rate improvement": "((Current repeat purchase rate - Previous repeat purchase rate) / Previous repeat purchase rate) * 100",
                    "Loyalty program participation rate": "(Participants / Eligible customers) * 100",
                    "Customer tenure increase": "Average tenure current period - Previous period"
                },
                "Enhance loyalty program effectiveness": {
                    "Loyalty program enrollment rate": "(Enrolled customers / Total target customers) * 100",
                    "Points redemption rate": "(Redeemed points / Total points issued) * 100",
                    "Program engagement score": "(Sum of engagement actions in program / Total participants) * 100",
                    "Retention uplift from loyalty program": "((Retention of participants - Retention of non-participants) / Retention of non-participants) * 100"
                },
                "Improve net promoter score": {
                    "NPS score improvement": "Current NPS - Previous NPS",
                    "Promoter percentage increase": "((Current promoters / Total respondents) * 100) - Previous percentage",
                    "Detractor percentage reduction": "((Previous detractors - Current detractors) / Previous detractors) * 100",
                    "NPS trend over time": "Graphical trend analysis of NPS across periods"
                },
                "Strengthen customer engagement": {
                    "Active user percentage": "(Active users / Total users) * 100",
                    "Engagement score improvement": "((Current engagement actions per user - Previous) / Previous) * 100",
                    "Interaction frequency increase": "((Current interactions - Previous interactions) / Previous interactions) * 100",
                    "Product usage depth improvement": "((Current depth metrics - Previous depth metrics) / Previous depth metrics) * 100"
                },
                "Increase renewal rates": {
                    "Contract renewal rate": "(Contracts renewed / Contracts due for renewal) * 100",
                    "Renewal revenue retention": "(Revenue from renewed contracts / Revenue from contracts due) * 100",
                    "Auto-renewal rate improvement": "((Current auto-renewals - Previous auto-renewals) / Previous auto-renewals) * 100",
                    "Renewal process satisfaction": "(Sum of satisfaction ratings with renewal process / Number of respondents) * 100"
                },
                "Improve product stickiness": {
                    "Daily active users percentage": "(DAU / Total users) * 100",
                    "Feature usage frequency": "Average usage per feature / Total users",
                    "Product dependency index": "(Sum of reliance scores per feature / Number of features) * 100",
                    "Switching cost perception": "(Sum of survey scores on perceived switching cost / Number of respondents) * 100"
                },
                "Build customer communities": {
                    "Community participation rate": "(Active community members / Total members) * 100",
                    "User-generated content volume": "Total content contributions from users",
                    "Peer-to-peer support percentage": "(Resolved support issues by peers / Total support issues) * 100",
                    "Community satisfaction score": "(Sum of community satisfaction ratings / Number of respondents) * 100"
                },
                "Enhance proactive support": {
                    "Proactive issue resolution rate": "(Proactively resolved issues / Total issues) * 100",
                    "Preventative support incidents": "Number of incidents prevented via proactive actions",
                    "Customer satisfaction proactive support": "(Sum of satisfaction ratings for proactive support / Number of respondents) * 100",
                    "Reactive ticket reduction percentage": "((Previous reactive tickets - Current reactive tickets) / Previous reactive tickets) * 100"
                },
                "Personalize retention strategies": {
                    "Personalized offer acceptance rate": "(Accepted personalized offers / Total offers) * 100",
                    "Retention campaign effectiveness": "(Retention achieved via campaign / Total targeted) * 100",
                    "Customer segment retention rates": "(Retained customers per segment / Total segment customers) * 100",
                    "Lifetime value preservation rate": "(CLV preserved via retention actions / Total CLV) * 100"
                }
            },
            "Customer Value & Relationship Management": {
                "Increase customer lifetime value": {
                    "CLV amount improvement": "Current CLV - Previous CLV",
                    "Customer profitability score increase": "Current profitability score - Previous profitability score",
                    "Value per customer growth": "((Current value per customer - Previous value per customer) / Previous value per customer) * 100",
                    "Return on customer investment": "(Profit from customer / Cost to acquire & serve customer) * 100"
                },
                "Improve relationship management": {
                    "Account health score improvement": "Current health score - Previous health score",
                    "Relationship depth score": "(Sum of meaningful interactions per account / Total interactions) * 100",
                    "Strategic account retention rate": "(Strategic accounts retained / Total strategic accounts) * 100",
                    "Executive engagement frequency": "Average number of executive interactions per account"
                },
                "Enhance customer segmentation": {
                    "Segmentation accuracy percentage": "(Correctly segmented customers / Total customers) * 100",
                    "Targeting effectiveness score": "(Revenue or conversions from targeted segments / Total targeted segments) * 100",
                    "Segment-specific growth rates": "((Current segment revenue - Previous segment revenue) / Previous segment revenue) * 100",
                    "Personalization relevance score": "(Interactions meeting personalized needs / Total personalized interactions) * 100"
                },
                "Strengthen account management": {
                    "Account growth rate": "((Current account revenue - Previous account revenue) / Previous account revenue) * 100",
                    "Account penetration depth": "(Products/services used per account / Total offerings) * 100",
                    "Account manager effectiveness score": "(Sum of KPIs achieved by account manager / Total KPIs assigned) * 100",
                    "Strategic account satisfaction": "(Sum of satisfaction ratings from strategic accounts / Number of respondents) * 100"
                },
                "Develop customer success programs": {
                    "Customer success score improvement": "Current success score - Previous success score",
                    "Product adoption rate increase": "((Current adoption rate - Previous adoption rate) / Previous adoption rate) * 100",
                    "Success plan completion rate": "(Completed success plans / Total success plans) * 100",
                    "Business outcomes achieved": "(Number of outcomes achieved / Total improvement_needed outcomes) * 100"
                },
                "Improve upsell and cross-sell rates": {
                    "Upsell conversion rate": "(Upsell transactions / Eligible customers) * 100",
                    "Cross-sell revenue growth": "((Current cross-sell revenue - Previous cross-sell revenue) / Previous cross-sell revenue) * 100",
                    "Average revenue per account": "Total revenue / Total accounts",
                    "Solution adoption breadth": "(Number of solutions adopted per customer / Total solutions offered) * 100"
                },
                "Enhance customer education": {
                    "Training completion rate": "(Completed trainings / Total assigned trainings) * 100",
                    "Customer proficiency score": "(Sum of proficiency scores / Number of assessed customers) * 100",
                    "Self-service usage increase": "((Current usage - Previous usage) / Previous usage) * 100",
                    "Support ticket reduction percentage": "((Previous tickets - Current tickets) / Previous tickets) * 100"
                },
                "Build strategic customer partnerships": {
                    "Strategic partnership count": "Number of active strategic partnerships",
                    "Joint business value created": "Revenue or profit generated through partnerships",
                    "Partnership satisfaction score": "(Sum of satisfaction ratings from partners / Number of respondents) * 100",
                    "Co-innovation projects completed": "(Completed joint innovation projects / Total improvement_needed projects) * 100"
                },
                "Improve customer health scoring": {
                    "Health score accuracy percentage": "(Accurate health predictions / Total customers assessed) * 100",
                    "At-risk customer identification rate": "(Correctly identified at-risk customers / Total at-risk customers) * 100",
                    "Intervention effectiveness score": "(Revenue or retention preserved through interventions / Total interventions) * 100",
                    "Health score trend improvement": "Improvement of average health score over time"
                },
                "Develop customer advocacy programs": {
                    "Advocate identification rate": "(Identified advocates / Total customers) * 100",
                    "Referenceable customer percentage": "(Referenceable customers / Total customers) * 100",
                    "Case study completion rate": "(Completed case studies / Improvement Needed case studies) * 100",
                    "Advocate engagement score": "(Sum of engagement actions by advocates / Total advocates) * 100"
                }
            },
            "Customer Insights & Analytics": {
                "Enhance customer data collection": {
                    "Data completeness score": "(Complete customer profiles / Total customers) * 100",
                    "Data accuracy rate": "(Accurate data points / Total data points) * 100",
                    "Real-time data availability": "(Real-time data sources / Total data sources) * 100",
                    "Customer profile enrichment rate": "(Enriched profiles / Total profiles) * 100"
                },
                "Improve customer analytics capabilities": {
                    "Predictive model accuracy": "(Correct predictions / Total predictions) * 100",
                    "Customer segmentation effectiveness": "(Revenue from targeted segments / Total revenue) * 100",
                    "Behavioral pattern identification rate": "(Identified patterns / Total potential patterns) * 100",
                    "Analytics adoption by business units": "(Business units using analytics / Total units) * 100"
                },
                "Leverage customer feedback for improvement": {
                    "Feedback implementation rate": "(Implemented feedback items / Total feedback) * 100",
                    "Customer-suggested improvements implemented": "(Implemented customer suggestions / Total suggestions) * 100",
                    "Feedback response time": "Average time to respond to customer feedback",
                    "Customer perception of feedback utilization": "Survey score on how well feedback is used"
                },
                "Enhance customer journey analytics": {
                    "Journey mapping completeness": "(Mapped journey stages / Total stages) * 100",
                    "Drop-off point identification": "(Identified drop-off points / Total potential points) * 100",
                    "Journey optimization impact": "((Improved conversion rate - Baseline rate) / Baseline rate) * 100",
                    "Cross-channel journey visibility": "(Visible cross-channel interactions / Total interactions) * 100"
                },
                "Develop customer intelligence systems": {
                    "Customer intelligence platform adoption": "(Users adopting platform / Total potential users) * 100",
                    "Single customer view completeness": "(Complete customer views / Total customers) * 100",
                    "Real-time customer insights availability": "(Available real-time insights / Total improvement_needed insights) * 100",
                    "Customer intelligence ROI": "((Benefits from intelligence - System cost) / System cost) * 100"
                },
            },
            #health
            "Health / Health Outcomes & Impact": {
                "Reduce disease prevalence": {
                    "Incidence rate of target diseases": "(New cases / Population at risk) * 1000",
                    "Mortality rate reduction": "((Previous mortality rate - Current mortality rate) / Previous rate) * 100",
                    "DALYs reduction": "((Previous DALYs - Current DALYs) / Previous DALYs) * 100",
                    "Patient recovery rate": "(Recovered patients / Total patients) * 100"
                },
                "Improve chronic disease management": {
                    "Patients under disease control": "(Patients with controlled condition / Total chronic patients) * 100",
                    "Hospital readmission rate reduction": "((Previous readmissions - Current readmissions) / Previous readmissions) * 100",
                    "Medication adherence rate": "(Patients adhering to prescribed treatment / Total patients) * 100",
                    "Complication incidence reduction": "((Previous complication rate - Current rate) / Previous rate) * 100"
                },
                "Enhance mental health outcomes": {
                    "Population with improved mental well-being": "(Individuals reporting improvement / Total served) * 100",
                    "Reduction in depression prevalence": "((Previous depression cases - Current cases) / Previous cases) * 100",
                    "Suicide rate reduction": "((Previous rate - Current rate) / Previous rate) * 100",
                    "Access to counseling services": "(Individuals receiving counseling / Total target population) * 100"
                },
                "Increase life expectancy & quality of life": {
                    "Life expectancy at birth": "Average years",
                    "Healthy life expectancy": "Average years free of major illness",
                    "Quality-adjusted life years (QALY)": "Sum of QALYs gained",
                    "Productivity improvement due to health": "(Workdays gained / Total potential workdays) * 100"
                },
            },
            "Health / Preventive & Public Health": {
                "Increase immunization coverage": {
                    "Vaccination coverage %": "(Vaccinated population / Total eligible population) * 100",
                    "Reduction in preventable disease prevalence": "((Previous prevalence - Current prevalence) / Previous prevalence) * 100",
                    "Maternal and child health service utilization": "(Women/children served / Target population) * 100",
                    "Public health campaign reach": "(Population reached / Total target population) * 100"
                },
                "Promote health education & awareness": {
                    "Health literacy index": "Survey score on population knowledge of health practices",
                    "Community health workshops conducted": "Number of workshops / period",
                    "Campaign engagement rate": "(Population actively engaged / Total target population) * 100",
                    "Behavioral change adoption rate": "(Population adopting healthy behaviors / Total targeted) * 100"
                },
                "Expand preventive screening programs": {
                    "Screening coverage %": "(Population screened / Total target population) * 100",
                    "Early detection rate": "(Cases detected early / Total cases) * 100",
                    "Follow-up adherence rate": "(Patients completing follow-up / Total patients requiring follow-up) * 100",
                    "Screening campaign reach": "(Population reached / Total target population) * 100"
                },
                "Improve maternal & child health": {
                    "Antenatal care coverage": "(Women receiving ANC / Total pregnant women) * 100",
                    "Safe delivery rate": "(Institutional deliveries / Total expected deliveries) * 100",
                    "Postnatal care coverage": "(Women receiving PNC / Total mothers) * 100",
                    "Child growth monitoring coverage": "(Children monitored / Total children under 5) * 100"
                },
            },
            "Health / Health Service Accessibility & Coverage": {
                "Expand access to primary healthcare": {
                    "Population with access to primary healthcare": "(Number of people with access / Total population) * 100",
                    "Geographic coverage of facilities": "(Number of regions covered / Total regions) * 100",
                    "Equity in access for marginalized groups": "(Number of marginalized served / Total marginalized population) * 100",
                    "Telemedicine adoption rate": "(Telemedicine users / Eligible population) * 100"
                },
                "Improve patient service availability": {
                    "Average appointment availability": "Average time to get appointment",
                    "24/7 emergency service coverage": "(Facilities offering 24/7 emergency / Total facilities) * 100",
                    "Average response time for emergencies": "Average minutes to respond",
                    "Availability of essential medications": "(Available essential meds / Total essential meds) * 100"
                },
                "Enhance specialty services access": {
                    "Population served by specialists": "(Patients receiving specialist care / Total needing care) * 100",
                    "Wait time for specialty appointments": "Average days from referral to appointment",
                    "Referral completion rate": "(Completed referrals / Total referrals) * 100",
                    "Patient satisfaction with specialty care": "(Sum of satisfaction ratings / Number of respondents) * 100"
                },
                "Increase telehealth utilization": {
                    "Telemedicine visit rate": "(Telemedicine visits / Total visits) * 100",
                    "Patient adoption rate": "(Patients using telehealth / Total eligible patients) * 100",
                    "Telemedicine satisfaction score": "(Sum of satisfaction ratings / Number of respondents) * 100",
                    "Reduction in in-person visit load": "((Previous in-person visits - Current in-person visits) / Previous visits) * 100"
                },
            },
            "Health / Health Equity & Gender": {
                "Promote gender-sensitive healthcare": {
                    "Female access to maternal care": "(Women served / Target women population) * 100",
                    "Reduction in gender disparities in health": "Index comparing male/female outcomes",
                    "Women-focused health programs coverage": "(Programs delivered / Planned programs) * 100",
                    "Gender-specific morbidity reduction": "((Previous female/male morbidity rate - Current rate) / Previous rate) * 100"
                },
                "Ensure inclusion of vulnerable populations": {
                    "Access for disabled individuals": "(Disabled individuals served / Total disabled population) * 100",
                    "Health services for elderly population": "(Elderly served / Target elderly population) * 100",
                    "Rural population health service coverage": "(Rural residents served / Total rural population) * 100",
                    "Monitoring health disparities index": "Index tracking service disparities among groups"
                },
                "Improve indigenous & minority health outcomes": {
                    "Population coverage for indigenous groups": "(Indigenous population served / Total indigenous population) * 100",
                    "Reduction in morbidity disparities": "Index comparing minority vs majority morbidity rates",
                    "Access to culturally sensitive care": "(Patients receiving culturally sensitive care / Total target population) * 100",
                    "Community satisfaction among minority groups": "(Sum of satisfaction ratings / Number of respondents) * 100"
                },
                "Address refugee & migrant health": {
                    "Refugee/migrant population served": "(Individuals served / Total refugee/migrant population) * 100",
                    "Immunization coverage in migrant groups": "(Vaccinated migrants / Total eligible migrants) * 100",
                    "Access to primary healthcare": "(Migrants accessing services / Total target population) * 100",
                    "Follow-up and continuity of care": "(Completed follow-ups / Total required follow-ups) * 100"
                },
            },
            "Health / Community & Stakeholder Engagement": {
                "Engage citizens and communities in health initiatives": {
                    "Community participation rate": "(Participants in programs / Total targeted population) * 100",
                    "Feedback incorporation rate": "(Community suggestions implemented / Total suggestions) * 100",
                    "Local health committee involvement": "(Active committees / Total planned committees) * 100",
                    "Public awareness improvement": "(Surveyed population aware / Total population) * 100"
                },
                "Collaborate with NGOs and social organizations": {
                    "Joint health initiatives launched": "Number of projects implemented jointly",
                    "Beneficiaries reached through partnerships": "Number of people served",
                    "Social program effectiveness score": "Evaluation score from program assessment",
                    "Community satisfaction with partnerships": "(Sum of satisfaction ratings / Number of respondents) * 100"
                },
                "Strengthen community-led health programs": {
                    "Number of community health projects": "Count of active community projects",
                    "Population reached by community programs": "(Population served / Total target population) * 100",
                    "Community participation in planning": "(Individuals involved in planning / Total invited) * 100",
                    "Impact of community interventions": "(Measured health improvement / Target improvement) * 100"
                },
                "Enhance cross-sector stakeholder engagement": {
                    "Number of multi-stakeholder meetings": "Count per period",
                    "Joint initiatives executed": "(Completed joint initiatives / Planned initiatives) * 100",
                    "Stakeholder satisfaction score": "(Sum of satisfaction ratings / Number of respondents) * 100",
                    "Policy adoption influenced by stakeholders": "(Policies adopted / Total proposed) * 100"
                },
            },
        },

        "Internal Process Perspective": {
            "Operational Excellence & Quality": {
                "Reduce process cycle times": {
                    "Cycle time reduction percentage": "((Previous cycle time - Current cycle time) / Previous cycle time) * 100",
                    "Process throughput improvement": "((Current throughput - Previous throughput) / Previous throughput) * 100",
                    "On-time completion rate": "(Processes completed on time / Total processes) * 100",
                    "Process efficiency score improvement": "Current process efficiency score - Previous score"
                },
                "Improve process standardization": {
                    "SOP adoption rate": "(Processes following SOP / Total processes) * 100",
                    "Process consistency score": "((Number of consistent process executions / Total executions) * 100)",
                    "Training compliance rate": "(Employees trained / Total required employees) * 100",
                    "Quality audit score improvement": "Current audit score - Previous audit score"
                },
                "Enhance quality control systems": {
                    "Quality inspection pass rate": "(Passed inspections / Total inspections) * 100",
                    "Defect detection rate improvement": "((Current detection rate - Previous) / Previous) * 100",
                    "Quality cost reduction percentage": "((Previous quality cost - Current) / Previous quality cost) * 100",
                    "Customer quality perception score": "Average rating from customer quality surveys"
                },
                "Reduce error and defect rates": {
                    "Error rate reduction percentage": "((Previous error rate - Current error rate) / Previous error rate) * 100",
                    "Defects per million reduction": "Previous defects per million - Current defects per million",
                    "Rework percentage decrease": "((Previous rework % - Current rework %) / Previous rework %) * 100",
                    "First-pass yield improvement": "Current first-pass yield - Previous first-pass yield"
                },
                "Improve supply chain efficiency": {
                    "Supply chain cycle time reduction": "((Previous cycle time - Current) / Previous cycle time) * 100",
                    "On-time delivery rate improvement": "((Current on-time deliveries - Previous) / Previous) * 100",
                    "Inventory accuracy percentage": "(Accurate inventory counts / Total inventory) * 100",
                    "Order fulfillment rate improvement": "((Current fulfilled orders - Previous) / Previous) * 100"
                },
                "Enhance inventory management": {
                    "Inventory turnover ratio improvement": "((Current turnover ratio - Previous) / Previous) * 100",
                    "Stock-out frequency reduction": "((Previous stock-outs - Current) / Previous) * 100",
                    "Inventory carrying cost reduction": "((Previous cost - Current cost) / Previous cost) * 100",
                    "Obsolete inventory percentage decrease": "((Previous obsolete % - Current) / Previous) * 100"
                },
                "Strengthen vendor performance": {
                    "Vendor performance score improvement": "Current vendor score - Previous score",
                    "Supplier on-time delivery rate": "(On-time deliveries / Total deliveries) * 100",
                    "Quality compliance rate improvement": "((Current compliance % - Previous) / Previous) * 100",
                    "Cost savings from vendor optimization": "Previous spend - Optimized spend"
                },
                "Improve asset utilization": {
                    "Asset utilization rate": "(Actual productive time / Available time) * 100",
                    "Equipment efficiency improvement": "((Current OEE - Previous OEE) / Previous OEE) * 100",
                    "Maintenance cost reduction": "((Previous maintenance cost - Current) / Previous) * 100",
                    "Uptime percentage improvement": "((Current uptime - Previous) / Previous) * 100"
                },
                "Reduce operational downtime": {
                    "Downtime hours reduction": "Previous downtime hours - Current downtime hours",
                    "Mean time between failures improvement": "Current MTBF - Previous MTBF",
                    "Mean time to repair reduction": "Previous MTTR - Current MTTR",
                    "System availability percentage": "(Uptime / Total time) * 100"
                },
                "Enhance service delivery consistency": {
                    "Service quality variance reduction": "Previous variance - Current variance",
                    "Customer experience consistency score": "((Number of consistent experiences / Total experiences) * 100)",
                    "Process standard deviation reduction": "Previous process deviation - Current deviation",
                    "Service level agreement compliance rate": "(SLAs met / Total SLAs) * 100"
                },
            },
            "Innovation & New Product Development": {
                "Accelerate time-to-market for new products": {
                    "Development cycle time reduction": "((Previous cycle time - Current) / Previous) * 100",
                    "Time from idea to launch reduction": "Previous time - Current time",
                    "Market readiness score improvement": "Current readiness score - Previous score",
                    "Project timeline adherence percentage": "(On-time milestones / Total milestones) * 100"
                },
                "Enhance R&D capabilities": {
                    "R&D investment ROI percentage": "((Revenue from R&D - R&D spend) / R&D spend) * 100",
                    "Number of patents filed": "Count of patents filed in period",
                    "Innovation pipeline strength score": "((Number of viable ideas / Total submitted ideas) * 100)",
                    "Research effectiveness index": "(Output of research / Input resources) * 100"
                },
                "Improve product design quality": {
                    "Design satisfaction score improvement": "Current satisfaction - Previous satisfaction",
                    "Number of design improvements implemented": "Count of improvements applied",
                    "Customer adoption rate": "(Adopted features / Total features) * 100",
                    "Time spent in redesign reduction": "((Previous redesign time - Current) / Previous) * 100"
                },
                "Strengthen innovation pipeline": {
                    "Pipeline conversion rate": "(Ideas converted to launch / Total ideas) * 100",
                    "Number of viable innovations": "Count of innovations passing feasibility assessment",
                    "Time through pipeline reduction": "((Previous pipeline duration - Current) / Previous) * 100",
                    "Innovation success rate": "(Successful innovations / Total launched) * 100"
                },
                "Leverage customer insights for innovation": {
                    "Customer insight utilization rate": "(Insights applied / Total collected insights) * 100",
                    "Number of insights applied to innovation": "Count of actionable insights implemented",
                    "Customer co-creation participation": "(Participants in co-creation / Total customers) * 100",
                    "Innovation relevance score improvement": "Current relevance score - Previous"
                },
                "Adopt emerging technologies": {
                    "Technology adoption rate": "(Implemented technologies / Identified emerging technologies) * 100",
                    "Number of emerging tech implementations": "Count of new tech deployed",
                    "Impact on operational efficiency": "Efficiency gain from technology adoption",
                    "Return on technology investment": "((Benefit - Cost) / Cost) * 100"
                },
                "Enhance prototyping processes": {
                    "Prototype iteration speed improvement": "((Previous iteration time - Current) / Previous) * 100",
                    "Prototype cost reduction percentage": "((Previous cost - Current) / Previous) * 100",
                    "Prototype fidelity improvement": "Current fidelity score - Previous score",
                    "Stakeholder feedback incorporation rate": "(Implemented feedback / Total feedback received) * 100"
                },
                "Improve product testing effectiveness": {
                    "Test coverage percentage improvement": "((Current coverage - Previous) / Previous) * 100",
                    "Defects caught in testing percentage": "(Defects found in test / Total defects) * 100",
                    "Testing cycle time reduction": "((Previous test duration - Current) / Previous) * 100",
                    "Customer acceptance rate improvement": "((Current acceptance rate - Previous) / Previous) * 100"
                },
                "Develop intellectual property portfolio": {
                    "Number of patents granted": "Count of patents approved",
                    "IP revenue percentage": "(Revenue from IP / Total revenue) * 100",
                    "IP portfolio value growth": "((Current value - Previous value) / Previous) * 100",
                    "Licensing deals completed": "Number of licensing agreements executed"
                },
                "Foster culture of innovation": {
                    "Employee innovation participation rate": "(Employees contributing ideas / Total employees) * 100",
                    "Number of ideas submitted": "Count of ideas submitted in period",
                    "Innovation culture survey score": "Average survey score on innovation culture",
                    "Implemented ideas percentage": "(Implemented ideas / Total submitted ideas) * 100"
                }
            },
            "Supply Chain & Logistics Management": {
                "Optimize end-to-end supply chain": {
                    "End-to-end supply chain visibility": "(Visible supply chain segments / Total segments) * 100",
                    "Supply chain cost reduction": "((Previous total cost - Current cost) / Previous cost) * 100",
                    "Perfect order fulfillment rate": "(Perfect orders / Total orders) * 100",
                    "Supply chain risk mitigation score": "Weighted score of risk reduction measures"
                },
                "Improve logistics and distribution": {
                    "On-time delivery performance": "(On-time deliveries / Total deliveries) * 100",
                    "Transportation cost optimization": "((Previous transport cost - Current) / Previous) * 100",
                    "Delivery accuracy rate": "(Accurate deliveries / Total deliveries) * 100",
                    "Last-mile delivery efficiency": "(Successful last-mile deliveries / Total) * 100"
                },
                "Enhance supplier relationship management": {
                    "Supplier performance score": "Weighted average of supplier KPIs",
                    "Supplier innovation contribution": "(Supplier-driven innovations / Total innovations) * 100",
                    "Supplier risk assessment coverage": "(Assessed suppliers / Total suppliers) * 100",
                    "Strategic supplier partnership depth": "Score based on partnership maturity"
                },
                "Optimize warehouse operations": {
                    "Warehouse capacity utilization": "(Used capacity / Total capacity) * 100",
                    "Order picking accuracy rate": "(Accurate picks / Total picks) * 100",
                    "Warehouse throughput improvement": "((Current throughput - Previous) / Previous) * 100",
                    "Storage cost per unit reduction": "((Previous cost - Current) / Previous) * 100"
                },
                "Improve demand forecasting accuracy": {
                    "Forecast accuracy percentage": "(1 - (Absolute forecast error / Actual demand)) * 100",
                    "Inventory turnover improvement": "((Current turnover - Previous) / Previous) * 100",
                    "Stock-out rate reduction": "((Previous stock-outs - Current) / Previous) * 100",
                    "Excess inventory percentage decrease": "((Previous excess - Current) / Previous) * 100"
                }
            },
            "Technology & Digital Operations": {
                "Enhance IT infrastructure reliability": {
                    "System uptime percentage": "(Uptime / Total operational time) * 100",
                    "Mean time between failures improvement": "Current MTBF - Previous MTBF",
                    "Infrastructure scalability score": "Weighted score of scalability metrics",
                    "Disaster recovery readiness": "(Recovery objectives met / Total objectives) * 100"
                },
                "Improve software development lifecycle": {
                    "Development velocity improvement": "((Current velocity - Previous) / Previous) * 100",
                    "Code quality score improvement": "Current quality score - Previous score",
                    "Deployment frequency increase": "((Current deployments - Previous) / Previous) * 100",
                    "Bug resolution time reduction": "((Previous resolution time - Current) / Previous) * 100"
                },
                "Optimize cloud operations": {
                    "Cloud cost optimization percentage": "((Previous cloud spend - Current) / Previous) * 100",
                    "Cloud performance reliability": "(Actual performance / Expected performance) * 100",
                    "Cloud security compliance score": "Weighted security compliance metrics",
                    "Multi-cloud management efficiency": "(Managed cloud resources / Total resources) * 100"
                },
                "Enhance data management capabilities": {
                    "Data quality score improvement": "Current data quality - Previous quality",
                    "Data processing efficiency": "(Processed data volume / Processing time)",
                    "Data governance compliance rate": "(Compliant data processes / Total processes) * 100",
                    "Master data management maturity": "Weighted maturity score"
                },
                "Improve cybersecurity posture": {
                    "Security incident reduction percentage": "((Previous incidents - Current) / Previous) * 100",
                    "Vulnerability remediation time reduction": "((Previous remediation time - Current) / Previous) * 100",
                    "Security training completion rate": "(Trained employees / Total employees) * 100",
                    "Compliance audit pass rate": "(Passed audits / Total audits) * 100"
                },
            },
            "Risk Management & Compliance": {
                "Strengthen enterprise risk management": {
                    "Risk identification coverage": "(Identified risks / Total potential risks) * 100",
                    "Risk mitigation effectiveness": "(Mitigated risks / Total risks) * 100",
                    "Risk assessment completion rate": "(Completed assessments / Total improvement_needed) * 100",
                    "Business continuity readiness": "(Ready processes / Total critical processes) * 100"
                },
                "Enhance regulatory compliance": {
                    "Compliance audit score improvement": "Current audit score - Previous score",
                    "Regulatory change implementation time": "Average time to implement regulatory changes",
                    "Compliance training completion rate": "(Completed training / Total required) * 100",
                    "Penalty avoidance percentage": "(Avoided penalties / Potential penalties) * 100"
                },
                "Improve business continuity planning": {
                    "BCP test success rate": "(Successful tests / Total tests) * 100",
                    "Recovery time objective achievement": "(Achieved RTOs / Total RTOs) * 100",
                    "Business impact analysis coverage": "(Analyzed processes / Total processes) * 100",
                    "Disaster recovery drill effectiveness": "Weighted score of drill performance"
                },
                "Strengthen internal controls": {
                    "Control effectiveness score": "Weighted score of control performance",
                    "Control deficiency resolution rate": "(Resolved deficiencies / Total deficiencies) * 100",
                    "Segregation of duties compliance": "(Compliant access rights / Total access rights) * 100",
                    "Fraud detection and prevention rate": "(Detected/prevented fraud / Total attempts) * 100"
                },
                "Enhance environmental, social, governance (ESG) performance": {
                    "ESG rating improvement": "Current ESG rating - Previous rating",
                    "Carbon footprint reduction percentage": "((Previous emissions - Current) / Previous) * 100",
                    "Social responsibility program impact": "Weighted impact score of social programs",
                    "Governance compliance score": "Weighted governance compliance metrics"
                },
            },
        },

        "Learning & Growth Perspective": {
            "People & Culture Development": {
                "Improve employee engagement": {
                    "Employee engagement survey score": "Average survey score across engagement questions",
                    "Voluntary turnover rate reduction": "((Previous voluntary turnover - current) / previous) * 100",
                    "Employee net promoter score": "Promoters % - Detractors %",
                    "Engagement action plan completion rate": "(Completed action plans / total plans) * 100"
                },
                "Enhance workplace culture": {
                    "Culture survey score improvement": "Current culture survey score - previous score",
                    "Values alignment percentage": "(Employees aligned with core values / total employees) * 100",
                    "Employee satisfaction score": "Average satisfaction survey score",
                    "Organizational health index": "Weighted index of culture, engagement, and satisfaction metrics"
                },
                "Strengthen diversity and inclusion": {
                    "Diversity representation at all levels": "(Employees from diverse groups / total employees) * 100",
                    "Inclusion index score": "Weighted score of inclusion survey metrics",
                    "Belongingness survey results": "Average survey score",
                    "Diverse promotion rate": "(Promotions of diverse employees / total promotions) * 100"
                },
                "Improve work-life balance": {
                    "Employee work-life balance score": "Average survey score on balance metrics",
                    "Flexible work arrangement participation": "(Employees using flexible arrangements / total employees) * 100",
                    "Overtime hours reduction percentage": "((Previous overtime hours - current) / previous) * 100",
                    "Employee burnout rate reduction": "((Previous burnout % - current) / previous) * 100"
                },
                "Enhance employee wellbeing": {
                    "Wellbeing program participation rate": "(Participants / total employees) * 100",
                    "Healthcare cost trend reduction": "((Previous cost - current cost) / previous cost) * 100",
                    "Employee stress level reduction": "((Previous stress score - current) / previous) * 100",
                    "Wellbeing index score improvement": "Current wellbeing index - previous"
                },
                "Strengthen internal communication": {
                    "Internal communication effectiveness score": "Weighted survey score",
                    "Message open and read rates": "(Opened/read messages / total messages) * 100",
                    "Employee feedback response rate": "(Responded feedback / total feedback) * 100",
                    "Communication channel utilization": "(Usage of available channels / total channels) * 100"
                },
                "Improve recognition programs": {
                    "Recognition program participation rate": "(Participants / total employees) * 100",
                    "Employee recognition frequency": "Number of recognitions / total employees",
                    "Recognition program satisfaction score": "Average satisfaction survey score",
                    "Peer-to-peer recognition percentage": "(Peer recognitions / total recognitions) * 100"
                },
                "Enhance collaboration across teams": {
                    "Cross-functional project success rate": "(Successful projects / total projects) * 100",
                    "Collaboration tool adoption rate": "(Users of collaboration tools / total employees) * 100",
                    "Inter-departmental satisfaction score": "Average survey score",
                    "Knowledge sharing frequency": "Number of knowledge sharing sessions per period"
                },
                "Foster innovation culture": {
                    "Idea submission rate per employee": "Total ideas submitted / total employees",
                    "Innovation program participation": "(Participants in innovation programs / total employees) * 100",
                    "Failed project learning application rate": "(Learnings applied / failed projects) * 100",
                    "Risk-taking encouragement score": "Survey score on risk-taking perception"
                },
                "Improve change management": {
                    "Change initiative_planning success rate": "(Successful initiatives / total initiatives) * 100",
                    "Employee change readiness score": "Average readiness survey score",
                    "Change adoption rate": "(Employees adopting change / total impacted) * 100",
                    "Resistance to change reduction": "((Previous resistance % - current) / previous) * 100"
                }
            },
            "Leadership & Talent Management": {
                "Enhance leadership development": {
                    "Leadership competency score improvement": "Current score - previous score",
                    "Leadership program completion rate": "(Completed participants / total participants) * 100",
                    "360-degree feedback score improvement": "Current 360 feedback - previous feedback",
                    "Leadership bench strength index": "Weighted index of ready-now leaders"
                },
                "Improve succession planning": {
                    "Succession plan coverage percentage": "(Key positions with plan / total key positions) * 100",
                    "Key position readiness score": "Weighted readiness score of successors",
                    "Internal promotion rate": "(Internal promotions / total promotions) * 100",
                    "Succession plan effectiveness rating": "Survey/metric rating of plan success"
                },
                "Strengthen talent acquisition": {
                    "Time-to-fill open positions": "Average days from job posting to hire",
                    "Quality of hire index": "Weighted score of performance, retention, and engagement of new hires",
                    "Candidate experience score": "Average survey score from candidates",
                    "Diverse hiring percentage": "(Diverse hires / total hires) * 100"
                },
                "Enhance performance management": {
                    "Goal achievement rate": "(Goals achieved / total goals) * 100",
                    "Performance review completion rate": "(Completed reviews / total employees) * 100",
                    "Feedback quality score": "Average quality score of feedback sessions",
                    "Performance improvement plan success rate": "(Successful PIPs / total PIPs) * 100"
                },
                "Improve coaching and mentoring": {
                    "Coaching program participation rate": "(Participants / total employees) * 100",
                    "Mentoring relationship satisfaction": "Average satisfaction score",
                    "Skill development progress rate": "(Skills achieved / improvement_needed skills) * 100",
                    "Coaching effectiveness score": "Survey/metric score on coaching impact"
                },
                "Develop future leaders": {
                    "High-potential identification rate": "(High-potential employees / total employees) * 100",
                    "Leadership program success rate": "(Successful program graduates / total participants) * 100",
                    "Ready-now candidates for key roles": "Count of ready-now employees",
                    "Leadership pipeline diversity percentage": "(Diverse leaders in pipeline / total leaders) * 100"
                },
                "Enhance executive development": {
                    "Executive competency score improvement": "Current score - previous score",
                    "Strategic thinking capability assessment": "Weighted score from assessment",
                    "Executive team effectiveness score": "Survey or metric score",
                    "Board evaluation of executive performance": "Average board evaluation score"
                },
                "Improve talent retention": {
                    "Regrettable attrition rate reduction": "((Previous regrettable attrition % - current) / previous) * 100",
                    "Key talent retention percentage": "(Key talent retained / total key talent) * 100",
                    "Exit interview satisfaction score": "Average satisfaction score from exits",
                    "Retention risk identification rate": "(Identified retention risks / total employees) * 100"
                },
                "Strengthen competency frameworks": {
                    "Competency model adoption rate": "(Employees assessed / total employees) * 100",
                    "Skill gap reduction percentage": "((Previous gap - current gap) / previous) * 100",
                    "Competency assessment completion rate": "(Completed assessments / total required) * 100",
                    "Role-specific competency alignment": "(Employees meeting role competency / total employees) * 100"
                },
                "Enhance leadership pipeline": {
                    "Pipeline readiness score improvement": "Current score - previous score",
                    "Internal fill rate for leadership roles": "(Internal fills / total leadership openings) * 100",
                    "Leadership development program ROI": "((Benefit - cost) / cost) * 100",
                    "Pipeline diversity and inclusion metrics": "(Diverse employees in pipeline / total pipeline) * 100"
                }
            },
            "Technology & Digital Enablement": {
                "Enhance digital transformation": {
                    "Digital maturity score improvement": "Current maturity score - previous score",
                    "Digital initiative_planning ROI percentage": "((Benefit - cost) / cost) * 100",
                    "Digital process adoption rate": "(Processes digitized / total processes) * 100",
                    "Digital revenue contribution percentage": "(Revenue from digital channels / total revenue) * 100"
                },
                "Improve technology infrastructure": {
                    "System uptime percentage": "(Uptime / total operational time) * 100",
                    "Infrastructure cost efficiency": "Output / infrastructure cost",
                    "Technology refresh cycle compliance": "(Systems refreshed on schedule / total systems) * 100",
                    "Infrastructure scalability score": "Weighted score of scalability metrics"
                },
                "Strengthen cybersecurity measures": {
                    "Security incident reduction percentage": "((Previous incidents - current) / previous) * 100",
                    "Vulnerability remediation time": "Average time to remediate vulnerabilities",
                    "Security compliance score": "Weighted compliance score",
                    "Phishing test success rate improvement": "((Current success rate - previous) / previous) * 100"
                },
                "Enhance data analytics capabilities": {
                    "Data-driven decision percentage": "(Decisions using data / total decisions) * 100",
                    "Analytics adoption rate": "(Users leveraging analytics / total employees) * 100",
                    "Insight-to-action time reduction": "((Previous time - current time) / previous) * 100",
                    "Data quality score improvement": "Current data quality score - previous"
                },
                "Improve system integration": {
                    "Integration defect rate reduction": "((Previous defects - current) / previous) * 100",
                    "Data consistency across systems": "(Consistent data points / total data points) * 100",
                    "API utilization rate": "(API calls used / total potential calls) * 100",
                    "Integration maintenance cost reduction": "((Previous cost - current) / previous) * 100"
                },
                "Enhance automation capabilities": {
                    "Process automation rate": "(Automated processes / total processes) * 100",
                    "Automation ROI percentage": "((Benefit - cost) / cost) * 100",
                    "Manual process reduction percentage": "((Previous manual processes - current) / previous) * 100",
                    "Automation scalability score": "Weighted score of automation scalability"
                },
                "Improve IT service delivery": {
                    "IT service desk satisfaction score": "Average survey score from users",
                    "Mean time to resolution reduction": "((Previous MTTR - current MTTR) / previous) * 100",
                    "Service level agreement compliance rate": "(SLAs met / total SLAs) * 100",
                    "IT project delivery on time percentage": "(Projects delivered on time / total projects) * 100"
                },
                "Strengthen cloud adoption": {
                    "Cloud migration completion percentage": "(Completed migrations / total improvement_needed) * 100",
                    "Cloud cost optimization percentage": "((Previous cost - current) / previous) * 100",
                    "Cloud security compliance score": "Weighted score of cloud security compliance",
                    "Cloud performance reliability percentage": "(Actual cloud uptime / total uptime) * 100"
                },
                "Enhance mobile solutions": {
                    "Mobile app adoption rate": "(Active users / total users) * 100",
                    "Mobile channel satisfaction score": "Average survey score",
                    "Mobile transaction completion rate": "(Completed transactions / total attempted) * 100",
                    "Mobile security incident reduction": "((Previous incidents - current) / previous) * 100"
                },
                "Improve digital literacy": {
                    "Digital skills assessment score": "Average score on digital skill assessments",
                    "Training completion rate": "(Completed training / total required) * 100",
                    "Digital tool adoption rate": "(Users using digital tools / total employees) * 100",
                    "Self-service capability utilization": "(Usage of self-service tools / total potential usage) * 100"
                }
            },
            "Knowledge, Collaboration & Innovation Capacity": {
                "Enhance knowledge management": {
                    "Knowledge base utilization rate": "(KB accesses / total employees) * 100",
                    "Content findability score improvement": "Current score - previous score",
                    "Knowledge sharing frequency": "Number of knowledge sharing events per period",
                    "Reduced duplicate work percentage": "((Previous duplicates - current) / previous) * 100"
                },
                "Improve collaboration tools": {
                    "Tool adoption rate": "(Users using collaboration tools / total employees) * 100",
                    "Collaboration satisfaction score": "Average survey score",
                    "Remote collaboration effectiveness": "Weighted score of remote collaboration success",
                    "Cross-functional project success rate": "(Successful projects / total projects) * 100"
                },
                "Strengthen learning organization": {
                    "Average learning hours per employee": "Total learning hours / total employees",
                    "Training completion rate": "(Completed trainings / total assigned) * 100",
                    "Skill competency improvement percentage": "((Current competency - previous) / previous) * 100",
                    "Employee learning satisfaction score": "Average survey score"
                },
                "Enhance innovation processes": {
                    "Implemented innovations count": "Number of innovations implemented",
                    "Time-to-implementation for innovations": "Average time from idea to implementation",
                    "Innovation ROI percentage": "((Benefit - cost) / cost) * 100",
                    "Employee participation in innovation programs": "(Participants / total employees) * 100"
                },
                "Improve knowledge sharing": {
                    "Knowledge repository usage rate": "(Repository accesses / total employees) * 100",
                    "Frequency of knowledge sharing sessions": "Number of sessions per period",
                    "Employee satisfaction with knowledge access": "Average survey score",
                    "Reduction in duplicated tasks percentage": "((Previous duplicated tasks - current) / previous) * 100"
                },
                "Strengthen research capabilities": {
                    "Completed research projects": "Count of research projects finished",
                    "Research outcomes implemented percentage": "(Implemented outcomes / total outcomes) * 100",
                    "Research budget utilization efficiency": "(Actual spend / budgeted spend) * 100",
                    "External research collaboration count": "Count of collaborations"
                },
                "Enhance cross-functional collaboration": {
                    "Cross-functional project success rate": "(Successful projects / total projects) * 100",
                    "Participation in cross-team initiatives": "(Employees involved / total employees) * 100",
                    "Collaboration survey score": "Average survey score",
                    "Number of knowledge transfer sessions": "Total sessions conducted"
                },
                "Improve idea management": {
                    "Idea submission count": "Total ideas submitted",
                    "Approved idea implementation rate": "(Implemented ideas / approved ideas) * 100",
                    "Impact score of implemented ideas": "Weighted impact score of ideas",
                    "Employee engagement in idea programs": "(Participants / total employees) * 100"
                },
                "Strengthen continuous improvement": {
                    "Number of CI initiatives": "Total CI initiatives implemented",
                    "Process improvement impact score": "Weighted score of improvements",
                    "Employee engagement in CI programs": "(Participants / total employees) * 100",
                    "Efficiency gain percentage from CI": "((Previous process inefficiency - current) / previous) * 100"
                },
                "Enhance organizational learning": {
                    "Learning program adoption rate": "(Employees using learning programs / total employees) * 100",
                    "Skills competency improvement percentage": "((Current skill competency - previous) / previous) * 100",
                    "Employee satisfaction with learning": "Average survey score",
                    "Application of learning in business outcomes": "(Measured application of learning in tasks / total expected application) * 100"
                },
            },
            "Organizational Agility & Change Management": {
                "Improve organizational responsiveness": {
                    "Time to market for new initiatives": "Average time from decision to implementation",
                    "Change implementation speed": "((Previous implementation time - Current) / Previous) * 100",
                    "Agility index score": "Weighted score of responsiveness metrics",
                    "Adaptation success rate": "(Successfully adapted initiatives / Total initiatives) * 100"
                },
                "Enhance change readiness": {
                    "Change readiness assessment score": "Average score from readiness assessments",
                    "Employee change adoption rate": "(Employees adopting change / Total employees) * 100",
                    "Change initiative_planning success rate": "(Successful changes / Total changes) * 100",
                    "Resistance mitigation effectiveness": "((Previous resistance - Current resistance) / Previous) * 100"
                },
                "Strengthen strategic alignment": {
                    "Strategic goal alignment percentage": "(Employees understanding strategic goals / Total employees) * 100",
                    "Departmental goal alignment score": "Weighted score of departmental alignment",
                    "Strategic initiative_planning completion rate": "(Completed initiatives / Total initiatives) * 100",
                    "Performance metric alignment": "(Aligned metrics / Total metrics) * 100"
                },
                "Improve decision-making speed": {
                    "Average decision cycle time": "Time from problem identification to decision",
                    "Decision quality score": "Weighted score of decision outcomes",
                    "Empowered decision-making rate": "(Decisions made at appropriate level / Total decisions) * 100",
                    "Information-to-decision time reduction": "((Previous time - Current time) / Previous) * 100"
                },
                "Enhance organizational resilience": {
                    "Business continuity readiness score": "Weighted score of resilience capabilities",
                    "Crisis response effectiveness": "(Effective responses / Total crises) * 100",
                    "Recovery time improvement": "((Previous recovery time - Current) / Previous) * 100",
                    "Risk mitigation coverage": "(Mitigated risks / Total identified risks) * 100"
                },
            },
        },
    }

    # Getters for forms
    # Getters for forms
    def get_perspective_choices(self):
        return [(p, p) for p in self.STRATEGY_MAP_HIERARCHY.keys()]

    def get_pillar_choices(self, perspective):
        return [(p, p) for p in self.STRATEGY_MAP_HIERARCHY.get(perspective, {}).keys()]

    def get_objective_choices(self, perspective, pillar):
        return [(o, o) for o in self.STRATEGY_MAP_HIERARCHY.get(perspective, {}).get(pillar, {}).keys()]

    def get_kpi_choices(self, perspective, pillar, objective):
        return [
            (kpi, kpi)
            for kpi in self.STRATEGY_MAP_HIERARCHY.get(perspective, {})
            .get(pillar, {})
            .get(objective, {})
            .keys()
        ]

    def get_formula(self, perspective, pillar, objective, kpi):
        return (
            self.STRATEGY_MAP_HIERARCHY
            .get(perspective, {})
            .get(pillar, {})
            .get(objective, {})
            .get(kpi, "")
        )

    # @classmethod
    # def get_perspective_choices(cls):
    #     return [(p, p) for p in cls.STRATEGY_MAP_HIERARCHY.keys()]
    #
    # @classmethod
    # def get_pillar_choices(cls, perspective):
    #     return [(p, p) for p in cls.STRATEGY_MAP_HIERARCHY.get(perspective, {}).keys()]
    #
    # @classmethod
    # def get_objective_choices(cls, perspective, pillar):
    #     return [(o, o) for o in cls.STRATEGY_MAP_HIERARCHY.get(perspective, {}).get(pillar, {}).keys()]
    #
    # @classmethod
    # def get_kpi_choices(cls, perspective, pillar, objective):
    #     return [(kpi, kpi) for kpi in
    #             cls.STRATEGY_MAP_HIERARCHY.get(perspective, {}).get(pillar, {}).get(objective, {}).keys()]
    #
    # @classmethod
    # def get_formula(cls, perspective, pillar, objective, kpi):
    #     return cls.STRATEGY_MAP_HIERARCHY.get(perspective, {}).get(pillar, {}).get(objective, {}).get(kpi, "")
