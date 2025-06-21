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
    ["🏠 Home", "📊 Data", "📈 Analytics", "ℹ️ About"]
)

# Developer Section (Enhanced with your info)
with st.expander("ℹ️ About Developer & Project", expanded=False):
    st.markdown("""
    <div class="developer-box">
        <h2>👨‍💻 Developed by: Faby Rizky</h2>
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
        - 💼 **LinkedIn:** Faby Rizky
        - 🐙 **GitHub:** @fabyrizky  
        - 📧 **Email:** fabyrizky@gmail.com
        - 🌐 **Portfolio:** fabyrizky.dev
        """)

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
    - **Deployment:** Streamlit Cloud for seamless hosting
    - **Version Control:** GitHub for collaborative development
    
    #### 📈 Current Features
    - **Real-time Data Visualization:** Interactive charts and metrics
    - **Category Analysis:** Deep dive into STEM subcategories
    - **Trend Monitoring:** Track growth patterns and emerging topics
    - **Responsive Design:** Works seamlessly across all devices
    - **User-Friendly Interface:** Intuitive navigation and clean design
    
    #### 🔮 Coming Soon
    - **Advanced NLP Analysis:** Sentiment analysis and topic modeling
    - **Predictive Analytics:** Forecast emerging STEM trends
    - **Personalization:** Customized content recommendations
    - **API Integration:** Real-time news feeds from multiple sources
    - **Export Features:** Download insights and reports
    """)
    
    st.success("✨ **Version 1.0** - Built with ❤️ by Faby Rizky")
    
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
st.sidebar.metric("🌟 Version", "1.0.0")
st.sidebar.metric("📅 Last Updated", "June 2025")
st.sidebar.metric("💡 Active Features", "12+")
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
st.sidebar.info("💡 **Tip:** Use the navigation menu to explore different sections of the platform!")

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
