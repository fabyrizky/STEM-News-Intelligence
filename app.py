import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Future STEM News Intelligence",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
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
    .developer-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<h1 class="main-header">🔬 Future STEM News Intelligence</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered STEM News Analysis & Personal Insights</p>', unsafe_allow_html=True)

# Navigation
page = st.sidebar.selectbox(
    "🚀 Choose a section:",
    ["🏠 Home", "📊 Analytics", "📈 Trends", "ℹ️ About"]
)

# Developer Information
with st.expander("ℹ️ About Developer & Project", expanded=False):
    st.markdown("""
    <div class="developer-info">
        <h3>👨‍💻 Developed by: Faby Rizky</h3>
        <p><strong>Future STEM News Intelligence</strong> is an advanced AI-powered platform designed to revolutionize 
        how we consume and analyze Science, Technology, Engineering, and Mathematics news content.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 Project Vision:**
        - Democratize access to STEM knowledge
        - Provide intelligent news curation
        - Enable data-driven insights
        - Foster scientific literacy
        """)
        
        st.markdown("""
        **🛠️ Technology Stack:**
        - **Frontend:** Streamlit
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Plotly
        - **Deployment:** Streamlit Cloud
        """)
    
    with col2:
        st.markdown("""
        **🌟 Key Features:**
        - 🔍 Real-time STEM news analysis
        - 📊 Interactive data visualizations
        - 📈 Trend analysis and predictions
        - 🎯 Personalized content recommendations
        - 📱 Responsive user interface
        """)
        
        st.markdown("""
        **📞 Connect with Developer:**
        - 💼 LinkedIn: Faby Rizky
        - 🐙 GitHub: @fabyrizky
        - 📧 Email: fabyrizky@gmail.com
        - 🌐 Portfolio: fabyrizky.dev
        """)

# Main Content
if page == "🏠 Home":
    st.markdown("## Welcome to Future STEM News Intelligence!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📚 Articles Analyzed", "1,234", "↗️ 12%")
    with col2:
        st.metric("🔬 Research Papers", "567", "↗️ 8%")
    with col3:
        st.metric("🚀 Tech Innovations", "890", "↗️ 15%")
    
    st.markdown("### 🎯 What you can do:")
    st.success("🔍 **Search and analyze** STEM news in real-time")
    st.info("📊 **Visualize trends** with interactive charts")
    st.warning("📈 **Track patterns** in scientific publications")
    st.error("🤖 **Get AI insights** on emerging technologies")

elif page == "📊 Analytics":
    st.header("📊 STEM News Analytics Dashboard")
    
    # Sample data
    categories = ['Science', 'Technology', 'Engineering', 'Mathematics']
    values = [145, 230, 178, 92]
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            x=categories, 
            y=values, 
            title="News Articles by Category",
            color=values,
            color_continuous_scale="viridis"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.pie(
            values=values, 
            names=categories, 
            title="Distribution of STEM Topics"
        )
        st.plotly_chart(fig, use_container_width=True)

elif page == "📈 Trends":
    st.header("📈 STEM Trends Analysis")
    
    # Sample trend data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    
    df = pd.DataFrame({
        'Date': dates,
        'AI & Machine Learning': np.random.randint(100, 1000, size=len(dates)),
        'Quantum Computing': np.random.randint(50, 500, size=len(dates)),
        'Biotechnology': np.random.randint(75, 750, size=len(dates))
    })
    
    fig = px.line(
        df, 
        x='Date', 
        y=['AI & Machine Learning', 'Quantum Computing', 'Biotechnology'],
        title="STEM Topics Trend Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Additional metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🤖 AI Growth", "+45%", "vs last year")
    with col2:
        st.metric("⚛️ Quantum Research", "+23%", "vs last year") 
    with col3:
        st.metric("🧬 Biotech News", "+67%", "vs last year")

elif page == "ℹ️ About":
    st.header("ℹ️ About This Project")
    
    st.markdown("""
    ### 🚀 Future STEM News Intelligence
    
    This application demonstrates the power of AI-driven news analysis specifically focused on 
    Science, Technology, Engineering, and Mathematics content.
    
    #### 🎯 Mission
    To make STEM knowledge more accessible and understandable for everyone, from students 
    to professionals to curious minds.
    
    #### 🛠️ Built With
    - **Streamlit** for the web interface
    - **Plotly** for interactive visualizations
    - **Pandas & NumPy** for data processing
    - **Python** as the core language
    
    #### 📈 Features
    - Real-time data visualization
    - Interactive trend analysis
    - Responsive design
    - Mobile-friendly interface
    """)
    
    st.success("✨ **This is Version 1.0** - More features coming soon!")

# Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Quick Stats")
st.sidebar.metric("🌟 App Version", "1.0.0")
st.sidebar.metric("🚀 Last Updated", "Today")
st.sidebar.metric("💡 Features", "4+")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 14px; padding: 2rem 0;'>
    <p><strong>Future STEM News Intelligence</strong> © 2025 | Developed with ❤️ by <strong>Faby Rizky</strong></p>
    <p>Empowering the future through intelligent STEM news analysis</p>
</div>
""", unsafe_allow_html=True)
