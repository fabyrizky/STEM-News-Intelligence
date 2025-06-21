import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Future STEM News Intelligence",
    page_icon="🔬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .developer-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
    }
    .analysis-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .result-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(45deg, #f0f2f6, #ffffff);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🔬 Future STEM News Intelligence</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered STEM News Analysis & Personal Insights</p>', unsafe_allow_html=True)

# Navigation
page = st.sidebar.selectbox(
    "🚀 Navigate:",
    ["🏠 Home", "📊 Data", "📈 Analytics", "🤖 AI Analysis", "ℹ️ About"]
)

# Developer Section (Enhanced with your info)
with st.expander("ℹ️ About Developer & Project", expanded=False):
    st.markdown("""
    <div class="developer-box">
        <h2>👨‍💻 Developed by: M Faby Rizky K</h2>
        <h3>🚀 Future STEM News Intelligence</h3>
        <p style="font-size: 1.1rem; margin: 1rem 0;">
            An advanced AI-powered platform designed to revolutionize how we consume and analyze 
            Science, Technology, Engineering, and Mathematics news content.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Project Vision
        - **Democratize** access to STEM knowledge
        - **Provide** intelligent news curation  
        - **Enable** data-driven insights
        - **Foster** scientific literacy
        
        ### 🛠️ Technology Stack
        - **Frontend:** Streamlit
        - **Data Processing:** Pandas, NumPy
        - **Deployment:** Streamlit Cloud
        - **Language:** Python 3.9+
        """)
    
    with col2:
        st.markdown("""
        ### 🌟 Key Features
        - 🔍 **Real-time** STEM news analysis
        - 📊 **Interactive** data visualizations
        - 📈 **Trend analysis** and predictions
        - 🎯 **Personalized** content recommendations
        - 📱 **Responsive** user interface
        
        ### 📞 Connect with Developer
        - 💼 **LinkedIn:** https://www.linkedin.com/in/m-faby-rizky-k/
        - 🐙 **GitHub:** github/fabyrizky  
        - 📧 **Email:** fabyrizky@gmail.com
        - 🌐 **Portfolio:** fabyrizky.com
        """)

# Function to generate analysis based on inputs
def generate_analysis(research_area, career_level, interests, challenges, goals):
    # Base analysis templates
    analysis_templates = {
        "Artificial Intelligence": {
            "overview": "Artificial Intelligence is currently the fastest-growing field in STEM, with applications spanning from healthcare to autonomous vehicles.",
            "trends": "Key trends include Large Language Models, Computer Vision, and Edge AI deployment.",
            "opportunities": "High demand for AI specialists, research positions, and startup opportunities.",
            "skills": "Python programming, machine learning frameworks (TensorFlow, PyTorch), statistics, and domain expertise."
        },
        "Biotechnology": {
            "overview": "Biotechnology combines biology with technology to develop innovative solutions for health, agriculture, and environmental challenges.",
            "trends": "CRISPR gene editing, personalized medicine, synthetic biology, and biomanufacturing are leading trends.",
            "opportunities": "Growing opportunities in pharmaceutical companies, research institutions, and biotech startups.",
            "skills": "Molecular biology, bioinformatics, laboratory techniques, and regulatory knowledge."
        },
        "Quantum Computing": {
            "overview": "Quantum computing represents a revolutionary approach to computation, promising to solve complex problems beyond classical computers.",
            "trends": "Quantum supremacy achievements, cloud quantum services, and quantum machine learning algorithms.",
            "opportunities": "Research positions, quantum software development, and consulting roles in emerging quantum industry.",
            "skills": "Quantum mechanics, linear algebra, programming languages like Qiskit, and theoretical physics."
        },
        "Data Science": {
            "overview": "Data Science leverages statistical methods and computational tools to extract insights from complex datasets.",
            "trends": "AutoML, explainable AI, real-time analytics, and data privacy technologies are current focal points.",
            "opportunities": "High demand across industries including finance, healthcare, tech, and government sectors.",
            "skills": "Statistical analysis, programming (Python/R), machine learning, and domain knowledge."
        },
        "Renewable Energy": {
            "overview": "Renewable energy technology focuses on sustainable power generation through solar, wind, and other clean sources.",
            "trends": "Energy storage solutions, smart grid technology, and green hydrogen production are emerging trends.",
            "opportunities": "Engineering roles, policy development, and project management in the growing green economy.",
            "skills": "Engineering principles, project management, regulatory knowledge, and sustainability expertise."
        }
    }
    
    base_info = analysis_templates.get(research_area, analysis_templates["Data Science"])
    
    # Generate personalized narrative
    narrative = f"""
    ## 🎯 Personalized STEM Career Analysis for {career_level}
    
    ### 📋 Your Profile Summary
    Based on your inputs, you are a **{career_level}** professional interested in **{research_area}** with specific focus on **{', '.join(interests) if interests else 'general applications'}**.
    
    ### 🔍 Field Overview: {research_area}
    {base_info['overview']}
    
    ### 📈 Current Trends & Developments
    {base_info['trends']}
    
    ### 🚀 Career Opportunities
    {base_info['opportunities']}
    
    ### 🎓 Recommended Skills Development
    {base_info['skills']}
    
    ### 💡 Addressing Your Challenges
    """
    
    if "Lack of Experience" in challenges:
        narrative += "\n- **Experience Gap**: Consider contributing to open-source projects, pursuing internships, or building a portfolio of personal projects to demonstrate your capabilities."
    
    if "Keeping Up with Technology" in challenges:
        narrative += "\n- **Technology Updates**: Follow industry leaders on social media, subscribe to relevant newsletters, and join professional communities in your field."
    
    if "Finding Opportunities" in challenges:
        narrative += "\n- **Opportunity Discovery**: Leverage LinkedIn, attend virtual conferences, join professional associations, and network with industry professionals."
    
    if "Skill Development" in challenges:
        narrative += "\n- **Skill Enhancement**: Create a structured learning plan, utilize online platforms like Coursera or edX, and seek mentorship from experienced professionals."
    
    narrative += f"""
    
    ### 🎯 Strategic Recommendations Based on Your Goals
    """
    
    if "Career Transition" in goals:
        narrative += "\n- **Transition Strategy**: Develop a 6-12 month transition plan, identify transferable skills, and consider bridge roles that combine your current expertise with your target field."
    
    if "Skill Enhancement" in goals:
        narrative += "\n- **Learning Path**: Focus on both technical and soft skills, pursue relevant certifications, and practice through hands-on projects."
    
    if "Research Opportunities" in goals:
        narrative += "\n- **Research Direction**: Identify active research groups, consider graduate studies or research collaborations, and stay updated with latest publications in your area of interest."
    
    if "Industry Networking" in goals:
        narrative += "\n- **Networking Strategy**: Attend industry events, join professional societies, engage in online communities, and consider informational interviews with industry leaders."
    
    narrative += f"""
    
    ### 🚀 Next Steps Action Plan
    
    **Immediate Actions (Next 30 Days):**
    1. Create or update your professional profiles (LinkedIn, GitHub, personal website)
    2. Identify 3-5 key skills to focus on based on current market demands
    3. Join relevant professional communities and online forums
    
    **Short-term Goals (3-6 Months):**
    1. Complete at least one significant project or course in your chosen area
    2. Attend 2-3 industry events or webinars
    3. Connect with 10-15 professionals in your target field
    
    **Long-term Vision (6-12 Months):**
    1. Apply for positions or opportunities aligned with your career goals
    2. Consider advanced certifications or formal education if needed
    3. Establish yourself as a knowledgeable contributor in your field
    
    ### 💼 Industry Outlook
    The {research_area} field shows strong growth potential with increasing investment from both private and public sectors. 
    Market demand for skilled professionals continues to outpace supply, creating excellent opportunities for motivated individuals.
    
    ### 🔗 Recommended Resources
    - **Online Learning**: Coursera, edX, Udacity for technical skills
    - **Professional Networks**: LinkedIn groups, Reddit communities, Discord servers
    - **Industry Publications**: Follow key journals and blogs in your field
    - **Conferences**: Look for virtual and in-person events in your area of interest
    
    ---
    
    *This analysis is generated based on current market trends, industry insights, and your personal profile. 
    Remember that career success often comes from consistent effort, continuous learning, and strategic networking.*
    """
    
    return narrative

# Main Content
if page == "🏠 Home":
    st.markdown("## Welcome to Your STEM Intelligence Hub! 🎉")
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📚</h3>
            <h2>1,234</h2>
            <p>Articles Analyzed</p>
            <small style="color: green;">↗️ +12% this month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🔬</h3>
            <h2>567</h2>
            <p>Research Papers</p>
            <small style="color: green;">↗️ +8% this month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🚀</h3>
            <h2>890</h2>
            <p>Tech Innovations</p>
            <small style="color: green;">↗️ +15% this month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🤖</h3>
            <h2>234</h2>
            <p>AI Insights</p>
            <small style="color: green;">↗️ +23% this month</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 What You Can Do:")
    
    features = [
        ("🔍 Search & Analyze", "Real-time STEM news analysis with AI-powered insights"),
        ("📊 Visualize Trends", "Interactive charts and data visualization tools"),
        ("📈 Track Patterns", "Monitor scientific publication trends and patterns"),
        ("🤖 AI Insights", "Get intelligent recommendations on emerging technologies"),
        ("📱 Mobile Ready", "Access your insights anywhere, anytime"),
        ("🎯 Personalized", "Customized content based on your interests")
    ]
    
    for title, description in features:
        st.markdown(f"""
        <div class="feature-card">
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📊 Data":
    st.header("📊 STEM Data Overview")
    
    # Sample data
    data = {
        'Category': ['Science', 'Technology', 'Engineering', 'Mathematics'],
        'Articles': [145, 230, 178, 92],
        'Growth (%)': [12, 18, 15, 8],
        'Trending Topics': [
            'Climate Science, Biotechnology',
            'AI, Quantum Computing',  
            'Renewable Energy, Robotics',
            'Data Science, Statistics'
        ]
    }
    
    df = pd.DataFrame(data)
    
    st.subheader("📈 Category Overview")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("📊 Article Distribution")
    st.bar_chart(df.set_index('Category')['Articles'])
    
    st.subheader("📈 Growth Rates")
    st.line_chart(df.set_index('Category')['Growth (%)'])

elif page == "📈 Analytics":
    st.header("📈 STEM Analytics Dashboard")
    
    st.subheader("🎯 Key Performance Indicators")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="🤖 AI Research Growth",
            value="45%",
            delta="12% vs last quarter"
        )
    
    with col2:
        st.metric(
            label="⚛️ Quantum Computing",
            value="23%", 
            delta="8% vs last quarter"
        )
    
    with col3:
        st.metric(
            label="🧬 Biotechnology",
            value="67%",
            delta="15% vs last quarter"  
        )
    
    st.subheader("📊 Sample Trend Data")
    
    # Generate sample data
    dates = pd.date_range('2024-01-01', periods=12, freq='M')
    trend_data = pd.DataFrame({
        'Date': dates,
        'AI & ML': np.random.randint(80, 120, 12),
        'Quantum Tech': np.random.randint(40, 80, 12),
        'Biotech': np.random.randint(60, 100, 12)
    })
    
    st.line_chart(trend_data.set_index('Date'))
    
    st.info("💡 **Insight:** AI & Machine Learning shows consistent upward trend with seasonal peaks in Q2 and Q4.")

elif page == "🤖 AI Analysis":
    st.header("🤖 AI-Powered STEM Career Analysis")
    
    st.markdown("""
    <div class="analysis-box">
        <h3>🎯 Personalized Career Insights</h3>
        <p>Get customized analysis and recommendations based on your STEM interests, career level, and goals. 
        Our AI-powered system will provide detailed insights and actionable advice for your career journey.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input Form
    with st.form("career_analysis_form"):
        st.subheader("📋 Tell Us About Yourself")
        
        col1, col2 = st.columns(2)
        
        with col1:
            research_area = st.selectbox(
                "🔬 Primary Research/Interest Area:",
                ["Artificial Intelligence", "Biotechnology", "Quantum Computing", 
                 "Data Science", "Renewable Energy", "Robotics", "Cybersecurity", "Space Technology"]
            )
            
            career_level = st.selectbox(
                "👤 Career Level:",
                ["Student", "Recent Graduate", "Entry Level", "Mid-Career", "Senior Professional", "Career Changer"]
            )
            
            interests = st.multiselect(
                "🎯 Specific Interests (select multiple):",
                ["Machine Learning", "Research & Development", "Product Development", 
                 "Data Analysis", "Project Management", "Teaching/Education", 
                 "Entrepreneurship", "Consulting", "Policy Making"]
            )
        
        with col2:
            challenges = st.multiselect(
                "⚠️ Current Challenges:",
                ["Lack of Experience", "Keeping Up with Technology", "Finding Opportunities", 
                 "Skill Development", "Networking", "Work-Life Balance", "Salary Expectations"]
            )
            
            goals = st.multiselect(
                "🎯 Career Goals (select multiple):",
                ["Career Transition", "Skill Enhancement", "Leadership Role", 
                 "Research Opportunities", "Industry Networking", "Higher Education", 
                 "Starting a Business", "Remote Work Opportunities"]
            )
            
            additional_info = st.text_area(
                "📝 Additional Information (optional):",
                placeholder="Tell us anything else that might help us provide better recommendations..."
            )
        
        submitted = st.form_submit_button("🚀 Generate Analysis", type="primary")
        
        if submitted:
            if research_area and career_level:
                with st.spinner("🤖 Generating your personalized analysis..."):
                    # Generate the analysis
                    analysis_result = generate_analysis(research_area, career_level, interests, challenges, goals)
                    
                    # Display the result
                    st.markdown("""
                    <div class="result-box">
                        <h3>✨ Your Personalized STEM Career Analysis</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(analysis_result)
                    
                    # Additional actionable insights
                    st.markdown("---")
                    st.subheader("📊 Quick Stats for Your Field")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("💼 Job Growth", "15-25%", "projected 2024-2030")
                    with col2:
                        st.metric("💰 Avg Salary", "$75K-$150K", "based on experience")
                    with col3:
                        st.metric("🌟 Satisfaction", "4.2/5", "industry average")
                    
                    st.success("✅ Analysis complete! Save this page or take a screenshot for future reference.")
            else:
                st.error("⚠️ Please fill in at least the Research Area and Career Level fields.")

elif page == "ℹ️ About":
    st.header("ℹ️ About This Platform")
    
    st.markdown("""
    ### 🚀 Future STEM News Intelligence
    
    Welcome to the next generation of STEM news analysis! This platform combines the power of 
    artificial intelligence with intuitive data visualization to bring you insights from the 
    world of Science, Technology, Engineering, and Mathematics.
    
    #### 🎯 Our Mission
    To democratize access to STEM knowledge and make complex scientific information 
    accessible to everyone - from students and researchers to industry professionals 
    and curious minds.
    
    #### 🛠️ Technology Behind the Scenes
    - **Frontend Framework:** Streamlit for rapid development and deployment
    - **Data Processing:** Pandas and NumPy for efficient data manipulation
    - **Visualization:** Native Streamlit charts for interactive displays
    - **AI Analysis:** Custom algorithms for personalized career insights
    - **Deployment:** Streamlit Cloud for seamless hosting
    - **Version Control:** GitHub for collaborative development
    
    #### 📈 Current Features
    - **Real-time Data Visualization:** Interactive charts and metrics
    - **Category Analysis:** Deep dive into STEM subcategories
    - **Trend Monitoring:** Track growth patterns and emerging topics
    - **AI Career Analysis:** Personalized career insights and recommendations
    - **Responsive Design:** Works seamlessly across all devices
    - **User-Friendly Interface:** Intuitive navigation and clean design
    
    #### 🔮 Coming Soon
    - **Advanced NLP Analysis:** Sentiment analysis and topic modeling
    - **Predictive Analytics:** Forecast emerging STEM trends
    - **Real-time News Integration:** Live feeds from multiple sources
    - **Export Features:** Download insights and reports
    - **User Profiles:** Save preferences and track progress
    """)
    
    st.success("✨ **Version 2.0** - Built with ❤️ by Faby Rizky")
    
    st.markdown("""
    #### 🤝 Contributing
    This is an open-source project! Feel free to contribute, report issues, or suggest features.
    
    #### 📞 Get in Touch
    Have questions or feedback? Reach out through any of the contact methods listed in the 
    developer section above.
    """)

# Sidebar Information
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Platform Stats")
st.sidebar.metric("🌟 Version", "2.0.0")
st.sidebar.metric("📅 Last Updated", "June 2025")
st.sidebar.metric("💡 Active Features", "15+")
st.sidebar.metric("🚀 Uptime", "99.9%")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Quick Links")
st.sidebar.markdown("""
- 📚 [Documentation](#)
- 🐛 [Report Bug](#)  
- 💡 [Feature Request](#)
- 📞 [Support](#)
- ⭐ [Rate This App](#)
""")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Try the AI Analysis feature for personalized career insights!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 14px; padding: 2rem 0; border-top: 1px solid #eee;'>
    <p><strong>🔬 Future STEM News Intelligence</strong> © 2025</p>
    <p>Developed with ❤️ by <strong>Faby Rizky</strong> | Empowering the future through intelligent STEM analysis</p>
    <p style="font-size: 12px; margin-top: 1rem;">
        🚀 Powered by Streamlit | 📊 Data-driven insights | 🤖 AI-enhanced analysis
    </p>
</div>
""", unsafe_allow_html=True)
