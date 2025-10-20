from management_project.models import Vision, OrganizationalProfile


class MissionService:
    SECTOR_MISSION_MAP = {
        'education': [
            "To provide inclusive and equitable learning opportunities",
            "To empower learners with innovative tools and resources",
            "To foster critical thinking, creativity, and problem-solving",
            "To strengthen teacher development and instructional excellence",
            "To integrate technology for enhanced educational outcomes",
            "To bridge digital and educational divides globally",
            "To promote lifelong learning and continuous growth",
            "To cultivate leadership and community engagement",
            "To support research and innovation in education",
            "To implement sustainable and resilient educational practices",
        ],

        'healthcare': [
            "To provide accessible and quality healthcare for all",
            "To empower communities with preventive health knowledge",
            "To leverage technology for better patient outcomes",
            "To reduce disparities in healthcare access globally",
            "To advance medical research and innovation",
            "To ensure safe and reliable medical services",
            "To promote mental health and well-being",
            "To improve public health education and awareness",
            "To foster collaboration across healthcare providers",
            "To innovate for sustainable healthcare delivery",
        ],

        'information_technology': [
            "To enable digital transformation and business growth",
            "To provide secure and reliable IT solutions",
            "To foster innovation in technology and software",
            "To integrate AI, automation, and cloud technologies",
            "To optimize operations through data-driven insights",
            "To enhance user experiences and engagement",
            "To support scalable and sustainable IT solutions",
            "To empower learning and collaboration in tech communities",
            "To drive adoption of emerging technologies responsibly",
            "To unlock business potential through technology",
        ],

        'finance_banking': [
            "To provide accessible and inclusive financial services",
            "To ensure transparency, trust, and security in banking",
            "To promote financial literacy and wealth creation",
            "To innovate digital payment and financial solutions",
            "To optimize financial operations with insights and analytics",
            "To support entrepreneurs and small businesses",
            "To advance responsible and ethical finance practices",
            "To enable equitable access to banking globally",
            "To drive efficiency and sustainability in financial services",
            "To foster trust and integrity across financial ecosystems",
        ],

        'agriculture': [
            "To advance sustainable and climate-resilient farming",
            "To empower farmers with technology and knowledge",
            "To ensure food security and equitable access",
            "To improve agricultural supply chains efficiently",
            "To implement precision agriculture and data analytics",
            "To adopt environmentally responsible practices",
            "To strengthen rural economies and livelihoods",
            "To foster innovation in crops and livestock management",
            "To promote research and development in agritech",
            "To integrate renewable energy in agricultural operations",
        ],

        'manufacturing': [
            "To deliver high-quality products efficiently",
            "To adopt sustainable and responsible manufacturing",
            "To innovate in automation, IoT, and smart factories",
            "To ensure workforce safety and skill development",
            "To optimize supply chains and production processes",
            "To implement lean and data-driven operations",
            "To collaborate for research and product innovation",
            "To expand markets responsibly and sustainably",
            "To enhance customization and flexibility in products",
            "To lead in industry innovation and sustainability",
        ],

        'energy_utilities': [
            "To provide reliable and sustainable energy solutions",
            "To integrate renewable and clean energy sources",
            "To optimize energy efficiency and reduce waste",
            "To leverage technology for smart energy management",
            "To promote community access to clean energy",
            "To ensure safety and regulatory compliance",
            "To advance energy storage and grid technologies",
            "To foster collaboration across energy sectors",
            "To reduce carbon footprint and environmental impact",
            "To innovate for a sustainable energy future",
        ],

        'environment_sustainability': [
            "To protect ecosystems and natural resources",
            "To promote sustainable development and practices",
            "To reduce environmental impact and emissions",
            "To foster climate resilience and adaptation",
            "To implement circular economy principles",
            "To educate and inspire environmental stewardship",
            "To innovate sustainable products and services",
            "To empower organizations with ESG strategies",
            "To collaborate globally for environmental protection",
            "To lead initiatives for a green and sustainable future",
        ],

        'transport_logistics': [
            "To deliver goods and people efficiently and safely",
            "To optimize supply chains and logistics operations",
            "To integrate technology for smart mobility solutions",
            "To reduce environmental impact in transportation",
            "To ensure reliability and customer satisfaction",
            "To enhance infrastructure and connectivity",
            "To implement data-driven fleet and cargo management",
            "To adopt sustainable fuels and operations",
            "To foster innovation in mobility and logistics",
            "To empower workforce skills and training",
        ],

        'tourism_hospitality': [
            "To provide memorable and safe travel experiences",
            "To promote sustainable and responsible tourism",
            "To support local communities and cultures",
            "To innovate hospitality and customer service",
            "To enhance accessibility for all travelers",
            "To integrate technology for personalized experiences",
            "To train and empower hospitality professionals",
            "To offer inclusive and diverse travel options",
            "To optimize operations and service delivery",
            "To lead in sustainable tourism and hospitality practices",
        ],

        'construction_real_estate': [
            "To build sustainable and resilient infrastructure",
            "To design innovative living and working spaces",
            "To adopt green building and resource-efficient practices",
            "To deliver high-quality projects on time and budget",
            "To implement digital solutions for project management",
            "To ensure safety, compliance, and durability",
            "To promote affordable and accessible housing",
            "To foster community collaboration in construction projects",
            "To integrate smart technologies in buildings",
            "To lead in sustainable real estate and development",
        ],

        'telecommunications': [
            "To connect people and businesses reliably",
            "To provide secure, high-speed communication networks",
            "To innovate in mobile, broadband, and IoT solutions",
            "To expand digital access to underserved areas",
            "To enhance customer experience and satisfaction",
            "To adopt sustainable and energy-efficient operations",
            "To implement AI and analytics for network optimization",
            "To foster global collaboration across telecom ecosystems",
            "To ensure regulatory compliance and safety",
            "To lead in telecommunications innovation",
        ],

        'research_development': [
            "To advance knowledge and scientific discovery",
            "To foster cross-industry and collaborative innovation",
            "To translate research into practical solutions",
            "To invest in talent, skills, and capacity building",
            "To ensure ethical and responsible research practices",
            "To leverage data and technology in research",
            "To enhance global access to research outputs",
            "To enable entrepreneurship from research outcomes",
            "To adopt sustainable and scalable R&D practices",
            "To lead in innovation for societal impact",
        ],

        'public_sector': [
            "To ensure transparent and accountable governance",
            "To provide accessible and efficient public services",
            "To promote social equity and citizen participation",
            "To implement digital and smart government solutions",
            "To strengthen policy planning and execution",
            "To empower public sector workforce and capabilities",
            "To optimize resource allocation and service delivery",
            "To foster collaboration across agencies and stakeholders",
            "To enhance transparency through data and reporting",
            "To lead innovation in public administration",
        ],

        'creative_media': [
            "To inspire creativity and cultural expression",
            "To engage audiences with meaningful content",
            "To promote diversity and inclusion in media",
            "To innovate in digital, traditional, and interactive media",
            "To support artists, creators, and creative industries",
            "To leverage technology for content delivery",
            "To ensure high-quality production standards",
            "To adopt sustainable media and production practices",
            "To implement data-driven audience insights",
            "To lead in creativity, engagement, and impact",
        ],

        'retail_wholesale': [
            "To provide seamless and satisfying shopping experiences",
            "To optimize supply chain and inventory management",
            "To leverage data for customer insights and personalization",
            "To support local businesses and ethical sourcing",
            "To innovate in retail technology and e-commerce",
            "To ensure product quality, safety, and compliance",
            "To adopt sustainable and responsible business practices",
            "To enhance customer loyalty and engagement",
            "To improve logistics and delivery efficiency",
            "To lead in customer-centric retail strategies",
        ],

        'ecommerce': [
            "To connect buyers and sellers efficiently online",
            "To provide secure and seamless digital transactions",
            "To optimize logistics, delivery, and fulfillment",
            "To personalize experiences using AI and analytics",
            "To expand global access to marketplaces",
            "To support small and medium enterprises online",
            "To ensure product quality and authenticity",
            "To adopt sustainable e-commerce practices",
            "To enhance customer service and engagement",
            "To lead in digital marketplace innovation",
        ],

        'professional_services': [
            "To deliver excellence in advisory and consulting services",
            "To provide innovative and actionable client solutions",
            "To ensure trust, integrity, and professionalism",
            "To foster talent development and continuous learning",
            "To leverage technology for efficient service delivery",
            "To expand global reach and collaboration",
            "To optimize client outcomes through insights",
            "To implement scalable professional solutions",
            "To promote thought leadership and research",
            "To lead in professional services innovation",
        ],

        'hospitality_food': [
            "To delight guests with exceptional experiences",
            "To provide safe, sustainable, and high-quality food",
            "To innovate in hospitality and dining services",
            "To integrate technology for efficiency and personalization",
            "To support local communities and suppliers",
            "To enhance staff training and professional development",
            "To adopt eco-friendly and sustainable operations",
            "To optimize guest satisfaction and loyalty",
            "To implement scalable and innovative solutions",
            "To lead in hospitality and food services excellence",
        ],

        'mining_resources': [
            "To extract resources responsibly and sustainably",
            "To innovate in mining technologies and safety",
            "To reduce environmental impact in operations",
            "To optimize resource utilization and efficiency",
            "To engage and empower local communities",
            "To comply with environmental and ethical standards",
            "To invest in rehabilitation and reclamation projects",
            "To integrate data and analytics for decision-making",
            "To adopt renewable energy and low-impact practices",
            "To lead in sustainable mining and resource management",
        ],
    }

    def __init__(self, org_obj: OrganizationalProfile):
        self.org = org_obj
        self.sector_name = org_obj.sector_name

    def get_choices(self):
        """Return list of tuples for form select."""
        missions = self.SECTOR_MISSION_MAP.get(self.sector_name, [])
        return [(m, m) for m in missions]

    def validate_choice(self, mission_statement):
        if mission_statement not in self.SECTOR_MISSION_MAP.get(self.sector_name, []):
            raise ValueError(f"Invalid mission '{mission_statement}' for sector '{self.sector_name}'.")

    def create_mission(self, mission_statement):
        self.validate_choice(mission_statement)
        return Mission.objects.create(
            organization_name=self.org,
            mission_statement=mission_statement
        )
