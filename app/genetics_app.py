"""
Principles of Genetics Interactive - Streamlit Web App
Complete genetics education from Mendelian to Population Genomics

Authors: Dr. Alok Patel & Ms. Susama Kar
Institution: Kuchinda College, Sambalpur University
License: CC BY 4.0
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Genetics Interactive",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better mobile experience
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1e3a8a;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .module-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: #f3f4f6;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #3b82f6;
        color: white;
        border-radius: 0.5rem;
        padding: 0.75rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://via.placeholder.com/300x100/1e3a8a/ffffff?text=Genetics+Interactive", 
                 use_column_width=True)

st.sidebar.markdown("## 📚 Navigation")

page = st.sidebar.radio(
    "Select Module:",
    [
        "🏠 Home",
        "1️⃣ Module 1: Poisson & Mapping",
        "2️⃣ Module 2: Interference & COC",
        "3️⃣ Module 3: Linkage vs LD",
        "4️⃣ Module 4: Mendelian → Population",
        "5️⃣ Module 5A: FST & Structure",
        "6️⃣ Module 5B: Selection Signatures",
        "7️⃣ Module 5C: Effective Pop Size",
        "📖 About & Resources",
        "💬 Feedback"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎓 Quick Stats")
st.sidebar.metric("Total Modules", "7")
st.sidebar.metric("Total Hours", "~15")
st.sidebar.metric("Interactive Widgets", "10+")
st.sidebar.metric("Practice Problems", "50+")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📞 Contact
**Email:** susama.kar@kuchindacollege.ac.in  
**GitHub:** [View Code](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive)  
**DOI:** 10.5281/zenodo.17887470
""")

# ============================================================================
# HOME PAGE
# ============================================================================

if page == "🏠 Home":
    st.markdown('<h1 class="main-header">Principles of Genetics Interactive</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; font-size: 1.2rem; color: #4b5563; margin: 1rem 0;'>
        <strong>From Mendelian Genetics to Conservation Genomics</strong><br>
        A Complete Interactive Learning Journey
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 🎯 Pattern Hunters\nDiscover patterns BEFORE formulas")
    
    with col2:
        st.success("### 🌍 Regional Examples\nIndian biodiversity throughout")
    
    with col3:
        st.warning("### 🆓 Open Access\nFree forever, use anywhere")
    
    st.markdown("---")
    
    # Module overview
    st.markdown("## 📚 7 Complete Modules")
    
    modules_data = {
        "Module": ["Module 1", "Module 2", "Module 3", "Module 4", 
                   "Module 5A", "Module 5B", "Module 5C"],
        "Topic": [
            "Poisson & Basic Mapping",
            "Interference & COC",
            "Linkage vs LD",
            "Mendelian → Population",
            "FST & Population Structure",
            "Selection Signatures",
            "Effective Population Size"
        ],
        "Duration": ["90-120 min", "90-120 min", "60-90 min", "60-90 min",
                     "90-120 min", "120-150 min", "90-120 min"],
        "Level": ["BSc", "BSc-MSc", "BSc-MSc", "BSc-MSc", 
                  "MSc-Research", "MSc-Research", "BSc-Research"],
        "Widgets": ["✓", "✓", "✓", "✓", "✓✓✓", "✓✓✓", "✓"]
    }
    
    df = pd.DataFrame(modules_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Learning paths
    st.markdown("## 🎯 Choose Your Learning Path")
    
    path_col1, path_col2 = st.columns(2)
    
    with path_col1:
        st.markdown("""
        <div class='module-card'>
        <h3>🎓 BSc Complete Course</h3>
        <p><strong>Duration:</strong> 12-15 hours</p>
        <p><strong>Modules:</strong> 1 → 2 → 3 → 4 → 5A</p>
        <p><strong>Outcome:</strong> NEP 2020 compliant genetics education</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='module-card'>
        <h3>🔬 Population Genomics Specialist</h3>
        <p><strong>Duration:</strong> 6-8 hours</p>
        <p><strong>Modules:</strong> Quick review 1-2 → 3 → 4 → 5A → 5B → 5C</p>
        <p><strong>Outcome:</strong> Research-ready in population genomics</p>
        </div>
        """, unsafe_allow_html=True)
    
    with path_col2:
        st.markdown("""
        <div class='module-card'>
        <h3>🌱 Complete Beginner</h3>
        <p><strong>Duration:</strong> 8-10 hours</p>
        <p><strong>Modules:</strong> 1 → 2 → 4 → 5A</p>
        <p><strong>Outcome:</strong> Solid foundation in genetics</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='module-card'>
        <h3>🦎 Conservation Genetics</h3>
        <p><strong>Duration:</strong> 4-6 hours</p>
        <p><strong>Modules:</strong> 5A → 5B → 5C</p>
        <p><strong>Outcome:</strong> Apply genetics to conservation</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Getting started
    st.markdown("## 🚀 Getting Started")
    
    start_col1, start_col2, start_col3 = st.columns(3)
    
    with start_col1:
        st.markdown("""
        ### 1️⃣ Choose Module
        Select from sidebar →
        Start with Module 1 or jump to your interest
        """)
    
    with start_col2:
        st.markdown("""
        ### 2️⃣ Explore Interactively
        Play with sliders and widgets
        Discover patterns yourself
        """)
    
    with start_col3:
        st.markdown("""
        ### 3️⃣ Practice & Apply
        Solve practice problems
        Apply to real data
        """)
    
    # Quick stats
    st.markdown("---")
    st.markdown("## 📊 Package Statistics")
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    stat_col1.metric("Total Modules", "7", "Complete pathway")
    stat_col2.metric("Total Hours", "~15", "Interactive content")
    stat_col3.metric("Widgets", "10+", "Hands-on exploration")
    stat_col4.metric("Examples", "15+", "Real data")

# ============================================================================
# MODULE 1: POISSON & MAPPING
# ============================================================================

elif page == "1️⃣ Module 1: Poisson & Mapping":
    st.title("Module 1: Poisson Distribution & Genetic Mapping")
    
    st.markdown("""
    ### 🎯 Learning Objectives
    - Understand why recombination frequency ≤ 50%
    - Discover the Poisson distribution pattern
    - Calculate recombination frequencies
    - Order genes from three-point cross data
    """)
    
    tab1, tab2, tab3 = st.tabs(["📖 Concept", "🎮 Interactive", "📝 Practice"])
    
    with tab1:
        st.markdown("""
        ## The Shape of Uncertainty
        
        Crossovers during meiosis are RANDOM events. But random doesn't mean 
        unpredictable! Random events follow patterns called **probability distributions**.
        
        ### The Poisson Distribution
        
        When events happen:
        - **Independently** (one doesn't affect another)
        - At a **constant average rate**
        - In **fixed intervals**
        
        They follow a Poisson distribution!
        """)
        
        # Simple example
        st.info("""
        **9th Grade Analogy:** Imagine a bag with 100 marbles (50 red, 50 blue). 
        Every time you pick one, you might switch bags or stay with same bag. 
        Over many picks, you'll switch about 50% of the time maximum!
        """)
    
    with tab2:
        st.markdown("## 🎮 Interactive: Poisson Distribution Explorer")
        
        # Parameters
        col1, col2 = st.columns(2)
        
        with col1:
            distance = st.slider(
                "Genetic Distance (map units)",
                min_value=1,
                max_value=50,
                value=10,
                help="Distance between two genes"
            )
        
        with col2:
            n_chromatids = st.slider(
                "Number of Chromatids",
                min_value=100,
                max_value=1000,
                value=400,
                step=100
            )
        
        # Calculate Poisson probabilities
        mean_crossovers = distance / 50  # Morgan to map units
        
        # Probabilities for 0, 1, 2, 3, 4 crossovers
        crossovers = np.arange(0, 5)
        probs = stats.poisson.pmf(crossovers, mean_crossovers)
        
        # Separate odd and even
        odd_prob = probs[1] + probs[3]  # 1 and 3 crossovers
        even_prob = probs[0] + probs[2] + probs[4]  # 0, 2, 4 crossovers
        
        # Calculate RF
        rf_calculated = odd_prob / (odd_prob + even_prob) * 100
        
        # Plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot 1: Poisson distribution
        colors = ['#3b82f6' if i % 2 == 0 else '#f97316' for i in crossovers]
        ax1.bar(crossovers, probs, color=colors, alpha=0.7, edgecolor='black')
        ax1.set_xlabel('Number of Crossovers', fontsize=12)
        ax1.set_ylabel('Probability', fontsize=12)
        ax1.set_title(f'Crossover Distribution (Distance = {distance} cM)', fontsize=14)
        ax1.legend(['Even (Parental)', 'Odd (Recombinant)'])
        ax1.grid(axis='y', alpha=0.3)
        
        # Plot 2: RF vs Distance
        distances = np.linspace(0, 100, 100)
        rfs = []
        for d in distances:
            m = d / 50
            p = stats.poisson.pmf(np.arange(0, 10), m)
            odd = p[1] + p[3] + p[5] + p[7] + p[9]
            even = p[0] + p[2] + p[4] + p[6] + p[8]
            rfs.append(odd / (odd + even) * 100)
        
        ax2.plot(distances, rfs, 'b-', linewidth=2)
        ax2.axhline(y=50, color='r', linestyle='--', label='50% Maximum')
        ax2.axvline(x=distance, color='g', linestyle='--', alpha=0.5, label=f'Current ({distance} cM)')
        ax2.set_xlabel('Genetic Distance (cM)', fontsize=12)
        ax2.set_ylabel('Recombination Frequency (%)', fontsize=12)
        ax2.set_title('Why RF Never Exceeds 50%', fontsize=14)
        ax2.legend()
        ax2.grid(alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Results
        st.success(f"""
        ### 📊 Results:
        - **Odd crossovers (Recombinants):** {odd_prob:.1%}
        - **Even crossovers (Parentals):** {even_prob:.1%}
        - **Calculated RF:** {rf_calculated:.1f}%
        - **Maximum possible RF:** 50%
        
        **Interpretation:** As distance increases, odd and even crossovers balance 
        at 50%-50%, so RF approaches but never exceeds 50%!
        """)
    
    with tab3:
        st.markdown("## 📝 Practice Problems")
        
        st.markdown("""
        ### Problem 1: Basic RF Calculation
        
        In a test cross between AaBb × aabb, you observe:
        - A-B- : 450
        - A-bb : 50
        - aaB- : 50  
        - aabb : 450
        
        **Total offspring:** 1000
        """)
        
        with st.expander("💡 See Solution"):
            st.markdown("""
            **Step 1:** Identify recombinants  
            Recombinants are minority classes: A-bb (50) and aaB- (50)  
            Total recombinants = 50 + 50 = 100
            
            **Step 2:** Calculate RF  
            RF = (Recombinants / Total) × 100  
            RF = (100 / 1000) × 100 = **10%**
            
            **Step 3:** Interpret  
            Genes A and B are 10 map units apart (10 cM)
            """)

# ============================================================================
# PLACEHOLDER FOR OTHER MODULES
# ============================================================================

elif page in ["2️⃣ Module 2: Interference & COC", "3️⃣ Module 3: Linkage vs LD",
               "4️⃣ Module 4: Mendelian → Population"]:
    st.title(page[4:])  # Remove emoji prefix
    st.info("🚧 Module content coming soon! This is a demonstration of the app structure.")
    
    st.markdown("""
    This module will include:
    - 📖 Conceptual explanations at multiple levels
    - 🎮 Interactive widgets and visualizations  
    - 📝 Practice problems with solutions
    - 🔬 Real data examples from Indian biodiversity
    """)

# Module 5A will be shown next...

# Continued in next part...
