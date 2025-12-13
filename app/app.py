"""
Module 1: Genetic Mapping - Poisson Distribution and the 50% Recombination Limit
COMPLETE STREAMLIT VERSION - Matches Jupyter Notebook 100%

Authors: Susama Kar & Dr. Alok Patel
Institution: Department of Zoology, Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Module 1: Genetic Mapping",
    page_icon="🧬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1e3a8a;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #3b82f6;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background: #eff6ff;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background: #f0fdf4;
        border-left: 4px solid #22c55e;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background: #fef3c7;
        border-left: 4px solid #eab308;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #f1f5f9;
        border-radius: 4px 4px 0 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🧬 Genetic Mapping: Poisson Distribution and the 50% Recombination Limit</h1>', unsafe_allow_html=True)

st.markdown("""
**Interactive Learning Module**

**Authors:** Susama Kar & Dr. Alok Patel  
**Institution:** Department of Zoology, Kuchinda College, Sambalpur University

---
""")

# Navigation tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Introduction",
    "🧬 Part 1: Poisson Distribution",
    "📈 Part 2: 50% RF Limit", 
    "🎲 Part 3: Simulation",
    "🐟 Part 4: Labeo rohita",
    "🎯 Summary"
])

# ============================================================================
# TAB 1: INTRODUCTION
# ============================================================================
with tab1:
    st.markdown('<h2 class="section-header">Welcome to Genetic Mapping!</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## What You'll Learn
        
        This module teaches you **why recombination frequency can never exceed 50%** through:
        
        1. 🧬 **Poisson Distribution** - The "shape" of crossover patterns
        2. 📈 **Mathematical Relationship** - How RF relates to distance
        3. 🎲 **Simulation** - See it happen in real-time
        4. 🐟 **Real Example** - Apply to actual fish genetics
        
        ## Learning Levels
        
        This module works at **THREE levels**:
        
        - 🎓 **9th Grade:** Simple analogies and visual patterns
        - 🎓 **BSc:** Full biological and mathematical treatment
        - 🎓 **Research:** Real data analysis and mapping functions
        
        Choose your level, or work through all three!
        """)
    
    with col2:
        st.info("""
        ### 📊 Quick Stats
        
        - **Duration:** 60-90 min
        - **Interactive Widgets:** 5
        - **Real Examples:** 1
        - **Practice Questions:** Yes
        - **Prerequisites:** Basic biology
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Pattern Hunters Philosophy
    
    We'll follow the **distribution-first** approach:
    
    1. **First:** OBSERVE the pattern (Poisson distribution)
    2. **Then:** UNDERSTAND the constraints (why 50%?)
    3. **Finally:** APPLY to real problems (Labeo rohita)
    
    ### No Formula Memorization! 
    
    You'll **discover patterns** instead of memorizing equations. By the end, you'll understand:
    
    - Why crossovers follow Poisson distribution
    - Why RF can never exceed 50% (mathematical inevitability)
    - How to map genes using real data
    - How to apply this to conservation genetics
    """)
    
    st.success("👆 **Click the tabs above** to navigate through the module. Start with **Part 1: Poisson Distribution**!")

# ============================================================================
# TAB 2: PART 1 - POISSON DISTRIBUTION
# ============================================================================
with tab2:
    st.markdown('<h2 class="section-header">🧬 Part 1: Understanding the Poisson Distribution</h2>', unsafe_allow_html=True)
    
    # Biology explanation
    st.markdown("""
    ### The Biology
    
    During meiosis, crossovers occur randomly along chromosomes. The number of crossovers in a region follows a **Poisson distribution** because:
    
    1. Events are **rare** (crossovers don't happen everywhere)
    2. Events are **independent** (one crossover doesn't affect others nearby - for now!)
    3. Events occur with **constant average rate** (μ = map distance)
    
    ### The Math
    
    The Poisson distribution tells us the probability of k crossovers:
    
    **P(k crossovers) = (μᵏ × e⁻ᵘ) / k!**
    
    Where:
    - **μ** = average number of crossovers = map distance (in Morgans)
    - **k** = actual number of crossovers (0, 1, 2, 3, ...)
    - **e** = 2.718... (Euler's number)
    
    ### The Key Insight 💡
    
    **Odd crossovers** (1, 3, 5, ...) → **Recombinant gametes** 🧬  
    **Even crossovers** (0, 2, 4, ...) → **Parental gametes** 🧬
    
    As distance increases, these balance out at **50%**!
    """)
    
    st.markdown("---")
    
    # Widget 1: Single Poisson Distribution
    st.markdown("### 🎮 Interactive Widget 1: Explore Single Distribution")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Controls:")
        mu = st.slider(
            "μ (Map Distance in Morgans)",
            min_value=0.1,
            max_value=3.0,
            value=1.0,
            step=0.1,
            help="Average number of crossovers in the region"
        )
        
        st.markdown(f"""
        **Current Settings:**
        - Map distance (μ): **{mu}** Morgan
        - In centiMorgans: **{mu*100:.0f} cM**
        - Expected crossovers: **{mu:.2f}**
        """)
        
        st.info("""
        **Try these values:**
        - μ = 0.2 (short distance)
        - μ = 1.0 (medium)
        - μ = 3.0 (long)
        
        Watch how RF changes!
        """)
    
    with col2:
        # Calculate Poisson probabilities
        k = np.arange(0, 15)
        pmf = poisson.pmf(k, mu)
        
        # Separate odd and even
        odd_prob = np.sum(pmf[1::2])  # 1, 3, 5, 7...
        even_prob = np.sum(pmf[0::2])  # 0, 2, 4, 6...
        
        # Calculate RF
        rf = odd_prob / (odd_prob + even_prob) * 100
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        colors = ['steelblue' if i % 2 == 0 else 'coral' for i in k]
        bars = ax.bar(k, pmf, color=colors, edgecolor='black', alpha=0.7, linewidth=1.5)
        
        ax.set_xlabel('Number of Crossovers (k)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Probability', fontsize=12, fontweight='bold')
        ax.set_title(f'Poisson Distribution (μ = {mu})', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        ax.set_ylim(0, max(pmf) * 1.1)
        
        # Legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='steelblue', edgecolor='black', label='Even (Parental)'),
            Patch(facecolor='coral', edgecolor='black', label='Odd (Recombinant)')
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=11)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Results
    st.success(f"""
    ### 📊 Results for μ = {mu}:
    
    - **Probability of EVEN crossovers (Parental):** {even_prob:.1%}
    - **Probability of ODD crossovers (Recombinant):** {odd_prob:.1%}
    - **Recombination Frequency (RF):** **{rf:.1f}%**
    - **Distance from 50% limit:** {abs(50 - rf):.1f}%
    
    💡 **Notice:** As μ increases toward infinity, RF approaches 50% asymptotically!
    """)
    
    # Questions to think about
    st.markdown("---")
    st.markdown("### 💡 Questions to Think About")
    
    with st.expander("❓ Click to see questions"):
        st.markdown("""
        1. What happens to the distribution shape as μ increases?
        2. Why do blue bars (even) and orange bars (odd) eventually balance out?
        3. Set μ = 3.0. Is RF close to 50%? Why doesn't it exceed 50%?
        4. At what μ value does RF first exceed 40%? (Try different values!)
        5. What's the most probable number of crossovers when μ = 2.0?
        6. Why are there NO negative crossovers? (Think about biology!)
        """)
    
    # Widget 2: Compare Four Distributions
    st.markdown("---")
    st.markdown("### 🎮 Interactive Widget 2: Compare Four Distributions")
    
    st.markdown("""
    Compare **four different map distances** simultaneously to see how distribution shape changes!
    
    **Suggested combinations to try:**
    - 📏 Very short to very long: 0.2, 0.5, 1.0, 2.0
    - 📏 All short distances: 0.1, 0.2, 0.3, 0.4
    - 📏 All long distances: 1.5, 2.0, 2.5, 3.0
    - 📏 Geometric progression: 0.25, 0.5, 1.0, 2.0
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mu1 = st.slider("μ₁:", 0.1, 3.0, 0.2, 0.1, key='mu1')
    with col2:
        mu2 = st.slider("μ₂:", 0.1, 3.0, 0.5, 0.1, key='mu2')
    with col3:
        mu3 = st.slider("μ₃:", 0.1, 3.0, 1.0, 0.1, key='mu3')
    with col4:
        mu4 = st.slider("μ₄:", 0.1, 3.0, 2.0, 0.1, key='mu4')
    
    # Plot four distributions
    mu_values = [mu1, mu2, mu3, mu4]
    colors_dist = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444']
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    rf_values = []
    
    for idx, (mu_val, color_dist) in enumerate(zip(mu_values, colors_dist)):
        ax = axes[idx]
        k = np.arange(0, 15)
        pmf = poisson.pmf(k, mu_val)
        
        # Calculate RF
        odd_prob = np.sum(pmf[1::2])
        even_prob = np.sum(pmf[0::2])
        rf = odd_prob / (odd_prob + even_prob) * 100
        rf_values.append(rf)
        
        # Plot
        bar_colors = ['steelblue' if i % 2 == 0 else 'coral' for i in k]
        ax.bar(k, pmf, color=bar_colors, edgecolor='black', alpha=0.7, linewidth=1.2)
        
        ax.set_title(f'μ = {mu_val} → RF = {rf:.1f}%', fontsize=13, fontweight='bold', color=color_dist)
        ax.set_xlabel('Number of Crossovers (k)', fontsize=10)
        ax.set_ylabel('Probability', fontsize=10)
        ax.grid(axis='y', alpha=0.3)
        ax.set_ylim(0, max(pmf) * 1.1)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    # Comparison table
    st.markdown("### 📊 Comparison Table:")
    
    df = pd.DataFrame({
        'Distribution': ['μ₁', 'μ₂', 'μ₃', 'μ₄'],
        'Map Distance (μ)': mu_values,
        'Distance (cM)': [f'{m*100:.0f}' for m in mu_values],
        'RF (%)': [f'{rf:.2f}' for rf in rf_values],
        'Distance from 50%': [f'{abs(50-rf):.2f}%' for rf in rf_values]
    })
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.info("""
    **Key Observation:** 
    As map distance (μ) increases, RF gets closer and closer to 50%, but never exceeds it!
    This is a **mathematical law**, not just biology.
    """)

# ============================================================================
# TAB 3: PART 2 - 50% RF LIMIT
# ============================================================================
with tab3:
    st.markdown('<h2 class="section-header">📈 Part 2: The 50% Recombination Frequency Limit</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### The Mathematical Relationship
    
    The relationship between map distance (μ) and recombination frequency (RF) is:
    
    ### RF = (1 - e⁻²ᵘ) / 2
    
    This formula emerges directly from the Poisson distribution!
    
    ### Key Insights:
    
    1. ✅ As μ → ∞, RF → 0.5 (50%)
    2. ✅ RF increases with distance, but **asymptotically**
    3. ✅ For small μ, RF ≈ μ (linear approximation)
    4. ✅ For large μ, RF plateaus at 50%
    
    ### Why 50% Maximum?
    
    **The Answer:** Mathematics of the Poisson distribution!
    
    When crossovers are far apart:
    - Odd crossovers (1, 3, 5, ...) happen **50% of the time**
    - Even crossovers (0, 2, 4, ...) happen **50% of the time**
    - They **balance perfectly** → RF = 50%
    
    This is why **unlinked genes** (on different chromosomes) also show 50% RF!
    """)
    
    st.markdown("---")
    
    # Widget 3: RF vs Distance Curve
    st.markdown("### 🎮 Interactive Widget 3: RF vs Distance Relationship")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("#### Controls:")
        max_mu = st.slider(
            "Maximum μ to display",
            min_value=1.0,
            max_value=5.0,
            value=3.0,
            step=0.5,
            help="How far along the x-axis to plot"
        )
        
        show_50_line = st.checkbox("Show 50% limit line", value=True)
        show_linear = st.checkbox("Show linear approximation", value=True)
        
        st.info("""
        **Explore:**
        - Set max μ = 5.0 to see full asymptote
        - Compare linear vs actual curve
        - See where they diverge
        """)
    
    with col2:
        # Calculate RF vs distance
        mu_range = np.linspace(0, max_mu, 500)
        rf_range = (1 - np.exp(-2 * mu_range)) / 2 * 100
        
        # Linear approximation (for small mu)
        rf_linear = mu_range * 100
        
        # Plot
        fig, ax = plt.subplots(figsize=(12, 7))
        
        # Main curve
        ax.plot(mu_range, rf_range, 'b-', linewidth=3, label='Actual RF = (1 - e⁻²ᵘ)/2')
        
        # 50% line
        if show_50_line:
            ax.axhline(y=50, color='red', linestyle='--', linewidth=2, 
                      label='50% Maximum', alpha=0.7)
            ax.fill_between(mu_range, rf_range, 50, alpha=0.1, color='red')
        
        # Linear approximation
        if show_linear:
            # Only plot where it makes sense
            mu_linear = mu_range[mu_range <= 0.5]
            rf_linear_plot = mu_linear * 100
            ax.plot(mu_linear, rf_linear_plot, 'g--', linewidth=2, 
                   label='Linear approx (RF ≈ μ)', alpha=0.7)
        
        ax.set_xlabel('Map Distance μ (Morgans)', fontsize=13, fontweight='bold')
        ax.set_ylabel('Recombination Frequency (%)', fontsize=13, fontweight='bold')
        ax.set_title('Why RF Never Exceeds 50%', fontsize=15, fontweight='bold')
        ax.legend(loc='lower right', fontsize=11)
        ax.grid(alpha=0.3)
        ax.set_xlim(0, max_mu)
        ax.set_ylim(0, 55)
        
        # Add annotations
        if max_mu >= 2.0:
            ax.annotate('Asymptotic approach to 50%', 
                       xy=(2.5, 48), xytext=(1.5, 40),
                       arrowprops=dict(arrowstyle='->', color='red', lw=2),
                       fontsize=11, color='red', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Show specific values
    st.markdown("### 📊 Key Distance-RF Relationships:")
    
    key_distances = [0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0]
    key_rfs = [(1 - np.exp(-2*mu))/2 * 100 for mu in key_distances]
    
    df_rf = pd.DataFrame({
        'Map Distance (μ)': key_distances,
        'Map Distance (cM)': [int(mu*100) for mu in key_distances],
        'RF (%)': [f'{rf:.2f}' for rf in key_rfs],
        'Gap to 50%': [f'{50-rf:.2f}%' for rf in key_rfs]
    })
    
    st.dataframe(df_rf, use_container_width=True, hide_index=True)
    
    st.warning("""
    ### 🔍 Important Observations:
    
    1. **At μ = 1.0 Morgan (100 cM):** RF is already ~43%
    2. **At μ = 2.0 Morgans:** RF is ~46.5%
    3. **At μ = 3.0 Morgans:** RF is ~48.8%
    4. **The gap to 50% shrinks** but never closes!
    
    This is why we need **mapping functions** to correct observed RF back to actual distance!
    """)

# ============================================================================
# TAB 4: PART 3 - CROSSOVER SIMULATION
# ============================================================================
with tab4:
    st.markdown('<h2 class="section-header">🎲 Part 3: Crossover Simulation</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Understanding Through Simulation
    
    Let's **simulate actual meiotic events** and count recombinants!
    
    We'll:
    1. Simulate many meioses
    2. For each meiosis, randomly determine number of crossovers (Poisson)
    3. Count odd vs even crossovers
    4. Calculate RF from simulation
    5. Compare to theoretical prediction
    
    This helps you **see** why the math works!
    """)
    
    st.markdown("---")
    
    # Widget 4: Crossover Simulator
    st.markdown("### 🎮 Interactive Widget 4: Crossover Simulator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Simulation Parameters:")
        
        map_distance_cm = st.slider(
            "Map Distance (cM)",
            min_value=5,
            max_value=50,
            value=20,
            step=5,
            help="Distance between two genes"
        )
        
        n_meioses = st.slider(
            "Number of Meioses",
            min_value=50,
            max_value=1000,
            value=200,
            step=50,
            help="How many meiotic events to simulate"
        )
        
        random_seed = st.slider(
            "Random Seed",
            min_value=1,
            max_value=100,
            value=42,
            step=1,
            help="Change for different random results"
        )
        
        # Convert to Morgans
        mu_sim = map_distance_cm / 100
        
        st.info(f"""
        **Settings:**
        - Distance: {map_distance_cm} cM = {mu_sim} M
        - Expected μ: {mu_sim}
        - Simulating: {n_meioses} meioses
        """)
        
        if st.button("🔄 Run New Simulation", help="Click to re-run with current settings"):
            random_seed = np.random.randint(1, 100)
    
    with col2:
        # Run simulation
        np.random.seed(random_seed)
        
        # Generate crossover counts for each meiosis
        crossover_counts = np.random.poisson(mu_sim, n_meioses)
        
        # Classify as parental or recombinant
        is_odd = crossover_counts % 2 == 1
        n_recombinant = np.sum(is_odd)
        n_parental = n_meioses - n_recombinant
        
        # Calculate observed RF
        rf_observed = (n_recombinant / n_meioses) * 100
        
        # Calculate theoretical RF
        rf_theoretical = (1 - np.exp(-2 * mu_sim)) / 2 * 100
        
        # Plot histogram
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Left plot: Histogram of crossover counts
        max_count = min(15, max(crossover_counts) + 2)
        bins = np.arange(0, max_count + 1) - 0.5
        
        colors_hist = ['steelblue' if i % 2 == 0 else 'coral' for i in range(max_count)]
        counts, _, bars = ax1.hist(crossover_counts, bins=bins, 
                                    edgecolor='black', linewidth=1.2, alpha=0.7)
        
        # Color bars
        for i, bar in enumerate(bars):
            if i < len(colors_hist):
                bar.set_facecolor(colors_hist[i])
        
        ax1.set_xlabel('Number of Crossovers', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax1.set_title(f'Simulated Crossover Distribution (n={n_meioses})', 
                     fontsize=13, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        
        # Right plot: Comparison bar chart
        categories = ['Parental\n(Even)', 'Recombinant\n(Odd)']
        values = [n_parental, n_recombinant]
        colors_bar = ['steelblue', 'coral']
        
        bars = ax2.bar(categories, values, color=colors_bar, edgecolor='black', 
                      linewidth=2, alpha=0.7)
        ax2.set_ylabel('Count', fontsize=12, fontweight='bold')
        ax2.set_title('Parental vs Recombinant Gametes', fontsize=13, fontweight='bold')
        ax2.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{val}\n({val/n_meioses*100:.1f}%)',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Results
    st.success(f"""
    ### 🎯 Simulation Results:
    
    **Observed:**
    - Parental gametes (even crossovers): **{n_parental}** ({n_parental/n_meioses*100:.1f}%)
    - Recombinant gametes (odd crossovers): **{n_recombinant}** ({n_recombinant/n_meioses*100:.1f}%)
    - **Observed RF: {rf_observed:.2f}%**
    
    **Theoretical:**
    - **Expected RF: {rf_theoretical:.2f}%**
    
    **Difference:** {abs(rf_observed - rf_theoretical):.2f}% (due to random sampling!)
    
    💡 **Try running multiple times** with different random seeds. The observed RF will vary around the theoretical value!
    """)
    
    st.info("""
    ### 🔬 What This Shows:
    
    1. **Random variation** is normal in biological experiments
    2. **Larger sample sizes** (more meioses) give more accurate RF estimates
    3. **Theoretical predictions** match simulation on average
    4. **Poisson distribution** accurately describes crossover patterns
    
    This is how real genetic mapping experiments work!
    """)

# ============================================================================
# TAB 5: PART 4 - LABEO ROHITA
# ============================================================================
with tab5:
    st.markdown('<h2 class="section-header">🐟 Part 4: Real Example - Labeo rohita (Rohu)</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Background
    
    **Labeo rohita** (Rohu) is an economically important carp species in India, found prominently in the **Mahanadi River system** of Odisha.
    
    Researchers have identified microsatellite markers for:
    - **Growth traits** (important for aquaculture)
    - **Disease resistance**
    - **Population structure**
    
    Let's use recombination frequency data to **map three genes** and determine their order on the chromosome!
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.info("""
        ### 📍 Species Information:
        
        - **Common name:** Rohu
        - **Scientific name:** *Labeo rohita*
        - **Habitat:** Rivers, especially Mahanadi
        - **Importance:** Major aquaculture species
        - **Genome:** Studied for QTL mapping
        
        ### 🧬 Three Loci:
        - **Locus A:** Growth-related microsatellite
        - **Locus B:** Disease resistance marker
        - **Locus C:** Population structure SNP
        """)
    
    with col2:
        st.image("https://via.placeholder.com/400x300/3b82f6/ffffff?text=Labeo+rohita", 
                caption="Labeo rohita (Rohu) from Mahanadi River")
    
    st.markdown("---")
    
    # Widget 5: Gene Mapper
    st.markdown("### 🎮 Interactive Widget 5: Three-Point Cross Gene Mapper")
    
    st.markdown("""
    **Task:** Given recombination frequencies between pairs of loci, determine:
    1. Gene order (which gene is in the middle?)
    2. Map distances
    3. Draw the genetic map
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Recombination Frequencies:")
        
        rf_ab = st.slider(
            "RF between A and B (%)",
            min_value=5.0,
            max_value=45.0,
            value=18.0,
            step=1.0,
            help="Observed recombination frequency"
        )
        
        rf_bc = st.slider(
            "RF between B and C (%)",
            min_value=5.0,
            max_value=45.0,
            value=12.0,
            step=1.0,
            help="Observed recombination frequency"
        )
        
        show_calculation = st.checkbox("Show step-by-step calculation", value=True)
        
        st.info("""
        **Typical values:**
        - RF(A-B) = 18%
        - RF(B-C) = 12%
        
        **Your task:**
        Determine RF(A-C) and gene order!
        """)
    
    with col2:
        # Calculate possible orders
        # If genes are A-B-C, then RF(A-C) = RF(A-B) + RF(B-C)
        # If genes are A-C-B, then RF(A-B) = RF(A-C) + RF(C-B)
        # If genes are B-A-C, then RF(B-C) = RF(B-A) + RF(A-C)
        
        # Calculate what RF(A-C) would be for each order
        rf_ac_if_abc = rf_ab + rf_bc  # A-B-C order
        rf_ac_if_acb = abs(rf_ab - rf_bc)  # A-C-B order
        rf_ac_if_bac = abs(rf_bc - rf_ab)  # B-A-C order (same as A-C-B)
        
        # The correct order is the one where middle distance = sum of outer - other
        # Most likely: distances are additive, so middle gene has sum of others
        
        # Determine most likely order
        if rf_ab > rf_bc:
            # A and B are furthest apart
            if show_calculation:
                st.markdown("""
                ### 📐 Step-by-Step Calculation:
                
                **Step 1:** Identify largest RF
                - RF(A-B) = {:.1f}% ← Largest
                - RF(B-C) = {:.1f}%
                
                **Step 2:** The two genes with largest RF are at the ends
                - A and B are at the ends
                - C must be in the middle!
                
                **Step 3:** Determine order
                - Possible orders: A-C-B or B-C-A (same map)
                - RF(A-B) should equal RF(A-C) + RF(C-B)
                
                **Step 4:** Calculate expected RF(A-C)
                - If C is between A and B:
                - RF(A-C) = RF(A-B) - RF(C-B)
                - RF(A-C) = {:.1f}% - {:.1f}% = {:.1f}%
                
                **Gene Order: A --- C --- B**
                """.format(rf_ab, rf_bc, rf_ab, rf_bc, rf_ab, rf_bc, abs(rf_ab - rf_bc)))
            
            gene_order = "A --- C --- B"
            dist_ac = abs(rf_ab - rf_bc)
            dist_cb = rf_bc
            
        else:
            # B and C are furthest OR equal
            if show_calculation:
                st.markdown("""
                ### 📐 Step-by-Step Calculation:
                
                **Step 1:** Compare RFs
                - RF(A-B) = {:.1f}%
                - RF(B-C) = {:.1f}% ← Larger or equal
                
                **Step 2:** Gene order analysis
                - If B-C are furthest, A is in middle
                - Order: B --- A --- C
                
                **Step 3:** Verify
                - RF(B-C) should equal RF(B-A) + RF(A-C)
                - RF(A-C) = RF(B-C) - RF(A-B)
                - RF(A-C) = {:.1f}% - {:.1f}% = {:.1f}%
                
                **Gene Order: B --- A --- C**
                """.format(rf_ab, rf_bc, rf_bc, rf_ab, abs(rf_bc - rf_ab)))
            
            gene_order = "B --- A --- C"
            dist_ba = rf_ab
            dist_ac = abs(rf_bc - rf_ab)
        
        # Draw genetic map
        fig, ax = plt.subplots(figsize=(12, 4))
        
        if "A --- C --- B" in gene_order:
            # Positions
            pos_a = 0
            pos_c = dist_ac
            pos_b = dist_ac + dist_cb
            
            # Draw line
            ax.plot([pos_a, pos_b], [0.5, 0.5], 'k-', linewidth=3)
            
            # Draw genes
            for pos, label, color in [(pos_a, 'A', '#3b82f6'), 
                                       (pos_c, 'C', '#10b981'), 
                                       (pos_b, 'B', '#ef4444')]:
                ax.plot(pos, 0.5, 'o', markersize=20, color=color, 
                       markeredgecolor='black', markeredgewidth=2)
                ax.text(pos, 0.3, label, ha='center', fontsize=16, fontweight='bold')
            
            # Add distances
            ax.text((pos_a + pos_c)/2, 0.65, f'{dist_ac:.1f} cM', 
                   ha='center', fontsize=12, fontweight='bold')
            ax.text((pos_c + pos_b)/2, 0.65, f'{dist_cb:.1f} cM', 
                   ha='center', fontsize=12, fontweight='bold')
            
        else:
            # B --- A --- C
            pos_b = 0
            pos_a = dist_ba
            pos_c = dist_ba + dist_ac
            
            # Draw line
            ax.plot([pos_b, pos_c], [0.5, 0.5], 'k-', linewidth=3)
            
            # Draw genes
            for pos, label, color in [(pos_b, 'B', '#ef4444'), 
                                       (pos_a, 'A', '#3b82f6'), 
                                       (pos_c, 'C', '#10b981')]:
                ax.plot(pos, 0.5, 'o', markersize=20, color=color, 
                       markeredgecolor='black', markeredgewidth=2)
                ax.text(pos, 0.3, label, ha='center', fontsize=16, fontweight='bold')
            
            # Add distances
            ax.text((pos_b + pos_a)/2, 0.65, f'{dist_ba:.1f} cM', 
                   ha='center', fontsize=12, fontweight='bold')
            ax.text((pos_a + pos_c)/2, 0.65, f'{dist_ac:.1f} cM', 
                   ha='center', fontsize=12, fontweight='bold')
        
        ax.set_xlim(-5, max(pos_b, pos_c) + 5 if 'pos_c' in locals() else rf_ab + rf_bc + 5)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title('Genetic Map of Labeo rohita Chromosome', 
                    fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    st.success(f"""
    ### 🎯 Mapping Results:
    
    **Gene Order:** {gene_order}
    
    **Map Distances:**
    - First interval: {rf_ab if 'B --- A --- C' in gene_order else abs(rf_ab - rf_bc):.1f} cM
    - Second interval: {abs(rf_bc - rf_ab) if 'B --- A --- C' in gene_order else rf_bc:.1f} cM
    - **Total map length:** {max(rf_ab, rf_bc, abs(rf_ab + rf_bc)):.1f} cM
    
    **Interpretation for Aquaculture:**
    - These markers can be used for **marker-assisted selection**
    - Knowing gene order helps in **QTL mapping**
    - Useful for **breeding programs** in Mahanadi hatcheries
    """)

# ============================================================================
# TAB 6: SUMMARY
# ============================================================================
with tab6:
    st.markdown('<h2 class="section-header">🎯 Summary & Key Takeaways</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What You've Learned
    
    Congratulations! You've completed Module 1. Here's what you now understand:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Core Concepts
        
        1. **Poisson Distribution**
           - Describes crossover patterns
           - Parameter μ = map distance
           - Odd crossovers → recombinants
           - Even crossovers → parentals
        
        2. **50% RF Limit**
           - Mathematical inevitability
           - Odd and even balance at 50%
           - Asymptotic approach
           - Why unlinked genes show 50% RF
        
        3. **RF-Distance Relationship**
           - RF = (1 - e⁻²ᵘ) / 2
           - Linear for small distances
           - Asymptotic for large distances
           - Need mapping functions for correction
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Skills Acquired
        
        1. **Analysis Skills**
           - Interpret Poisson distributions
           - Calculate RF from data
           - Determine gene order
           - Draw genetic maps
        
        2. **Pattern Recognition**
           - See distribution shapes
           - Understand asymptotic behavior
           - Recognize mathematical constraints
        
        3. **Real Applications**
           - Map genes in real organisms
           - Apply to aquaculture
           - Understand QTL mapping
           - Conservation genetics
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🎓 Pattern Hunters Principles Demonstrated
    
    This module exemplified the **Pattern Hunters philosophy**:
    
    1. ✅ **"Uncertainty has shape"**
       - Crossovers follow Poisson distribution
       - Not random chaos, but predictable pattern
    
    2. ✅ **"Shape creates constraints"**
       - Distribution structure → 50% RF limit
       - Mathematical law, not biological accident
    
    3. ✅ **"Reality modifies theory"**
       - (We'll see this in Module 2 with interference!)
    
    4. ✅ **"Strategic design resolves ambiguity"**
       - Three-point crosses determine gene order
       - Two-point crosses alone are ambiguous
    
    5. ✅ **"Local examples illuminate universal principles"**
       - Labeo rohita follows same laws as any organism
       - Mahanadi River genetics = universal genetics
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🚀 Next Steps
    
    ### Module 2: Interference and Coefficient of Coincidence
    
    You'll learn:
    - Why crossovers DON'T always follow pure Poisson
    - How interference modifies expectations
    - Haldane vs Kosambi mapping functions
    - Real data from earthworms and fish
    
    ### Practice Suggestions
    
    Before moving to Module 2:
    
    1. **Experiment with widgets**
       - Try extreme values
       - Test your predictions
       - See patterns clearly
    
    2. **Work with real data**
       - Find genetic mapping papers
       - Calculate RF from data
       - Draw maps
    
    3. **Teach someone else**
       - Best way to solidify understanding
       - Explain why RF ≤ 50%
       - Use Poisson distribution
    """)
    
    st.success("""
    ### 🎊 Congratulations!
    
    You've completed **Module 1: Genetic Mapping**!
    
    You now understand one of the most fundamental concepts in genetics:
    **Why recombination frequency can never exceed 50%**
    
    This isn't just memorized - you've **discovered** it through:
    - Exploring distributions
    - Running simulations
    - Analyzing real data
    - Seeing the pattern emerge
    
    **Ready for Module 2?** → Click to continue your genetics journey!
    """)
    
    st.markdown("---")
    
    # Feedback section
    st.markdown("### 📝 Feedback")
    
    with st.expander("💬 Share your thoughts (optional)"):
        st.markdown("""
        What did you think of this module?
        
        - Was it helpful?
        - Which widgets did you like most?
        - What was confusing?
        - Suggestions for improvement?
        
        **Contact:** susama.kar@kuchindacollege.ac.in
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Module 1: Genetic Mapping - Poisson Distribution and 50% RF Limit</strong></p>
    <p>Developed by Susama Kar & Dr. Alok Patel</p>
    <p>Department of Zoology, Kuchinda College, Sambalpur University</p>
    <p>Part of the Pattern Hunters Educational Series</p>
    <p>License: CC BY 4.0 | <a href="https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive">GitHub</a> | DOI: 10.5281/zenodo.17887470</p>
</div>
""", unsafe_allow_html=True)
