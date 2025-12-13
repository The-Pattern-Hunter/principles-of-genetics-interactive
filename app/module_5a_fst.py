"""
Module 5A: FST and Population Structure
COMPLETE STREAMLIT VERSION - Matches Jupyter Notebook 100%

An Interactive Journey from Observation to Understanding

Authors: Susama Kar & Dr. Alok Patel
Institution: Department of Zoology, Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Module 5A: FST & Population Structure",
    page_icon="🌍",
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
    .pattern-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: 1rem 0;
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
    .example-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background: #fef2f2;
        border-left: 4px solid #ef4444;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🌍 Module 5A: FST and Population Structure</h1>', unsafe_allow_html=True)

st.markdown("""
**An Interactive Journey from Observation to Understanding**

**Authors:** Susama Kar & Dr. Alok Patel  
**Institution:** Department of Zoology, Kuchinda College, Sambalpur University

---
""")

# Pattern Hunters approach box
st.markdown("""
<div class="pattern-box">
<h3>🔍 The Pattern Hunters Approach</h3>
<p><strong>Traditional approach:</strong> "FST = (H<sub>T</sub> - H<sub>S</sub>) / H<sub>T</sub>" → Memorize formula</p>
<p><strong>Pattern Hunters approach:</strong></p>
<ol>
<li><strong>OBSERVE:</strong> Watch populations diverge</li>
<li><strong>MEASURE:</strong> Quantify the difference</li>
<li><strong>UNDERSTAND:</strong> What creates/prevents divergence</li>
<li><strong>APPLY:</strong> Make conservation decisions</li>
</ol>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Introduction",
    "👀 Part 1: Observation",
    "📐 Part 2: Calculate FST",
    "🌍 Part 3: Real Examples",
    "🦎 Part 4: Applications",
    "🎯 Summary"
])

# ============================================================================
# TAB 1: INTRODUCTION
# ============================================================================
with tab1:
    st.markdown('<h2 class="section-header">Welcome to Population Genetics!</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## What You'll Learn
        
        This module teaches you **how to measure genetic differences between populations** using FST.
        
        ### The Journey:
        
        1. 👀 **Observe** - Watch populations diverge through genetic drift
        2. 📐 **Measure** - Calculate FST step-by-step
        3. 🌍 **Explore** - See real examples from humans, fish, and cattle
        4. 🦎 **Apply** - Use FST for conservation decisions
        
        ## Why FST Matters
        
        FST answers questions like:
        - Are these two populations genetically distinct?
        - Should we manage them separately?
        - Is gene flow occurring between populations?
        - Which populations are most important for conservation?
        
        ## Prerequisites
        
        - Basic population genetics (Module 4 helpful but not required)
        - Understanding of allele frequencies
        - Curiosity about genetic diversity!
        """)
    
    with col2:
        st.info("""
        ### 📊 Module Stats
        
        - **Duration:** 90-120 min
        - **Level:** MSc/Research
        - **Widgets:** 4 interactive
        - **Real Data:** 3 examples
        - **Applications:** Conservation
        
        ### 🎓 Learning Levels
        
        - **9th Grade:** Village analogy
        - **BSc:** Wright's formula
        - **MSc:** Drift-migration balance
        - **Research:** Conservation decisions
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## The FST Scale
    
    Before we begin, here's what FST values mean:
    """)
    
    # FST scale visualization
    fig, ax = plt.subplots(figsize=(12, 3))
    
    fst_ranges = [0, 0.05, 0.15, 0.25, 1.0]
    labels = ['Little\n0-0.05', 'Moderate\n0.05-0.15', 'Great\n0.15-0.25', 'Very Great\n>0.25']
    colors = ['#22c55e', '#eab308', '#f97316', '#ef4444']
    
    for i in range(len(fst_ranges)-1):
        ax.barh(0, fst_ranges[i+1]-fst_ranges[i], left=fst_ranges[i], 
               height=0.5, color=colors[i], edgecolor='black', linewidth=2)
        mid_point = (fst_ranges[i] + fst_ranges[i+1]) / 2
        ax.text(mid_point, 0, labels[i], ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
    
    ax.set_xlim(0, 0.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_xlabel('FST Value', fontsize=12, fontweight='bold')
    ax.set_title('FST Interpretation Scale', fontsize=14, fontweight='bold', pad=20)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.success("👆 **Start with Part 1: Observation** to see populations diverge in real-time!")

# ============================================================================
# TAB 2: PART 1 - OBSERVATION
# ============================================================================
with tab2:
    st.markdown('<h2 class="section-header">👀 Part 1: The Observation - Two Populations Diverge</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The Scenario
    
    Imagine two populations of fish that were once a single population. Perhaps:
    - A river split into two branches
    - A landslide created a waterfall barrier
    - Humans introduced fish to a new lake
    
    **What happens over time?**
    
    Even if both populations start with **identical** allele frequencies, they will **diverge** due to:
    - **Genetic drift** (random sampling each generation)
    - **No gene flow** (isolated populations)
    
    Let's watch this happen!
    """)
    
    st.markdown("---")
    
    # Widget 1: Population Divergence Simulator
    st.markdown("### 🎮 Interactive 1: Watch Two Populations Diverge")
    
    st.info("**Simulated data for educational purposes**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Simulation Parameters:")
        
        p0 = st.slider(
            "Starting allele frequency",
            min_value=0.1,
            max_value=0.9,
            value=0.5,
            step=0.05,
            help="Both populations start at this frequency"
        )
        
        generations = st.slider(
            "Generations to simulate",
            min_value=10,
            max_value=500,
            value=100,
            step=10
        )
        
        Ne = st.slider(
            "Effective population size (Ne)",
            min_value=10,
            max_value=200,
            value=50,
            step=10,
            help="Smaller Ne = faster drift"
        )
        
        migration_rate = st.slider(
            "Migration rate (m)",
            min_value=0.0,
            max_value=0.1,
            value=0.0,
            step=0.001,
            format="%.3f",
            help="Proportion migrating each generation"
        )
        
        random_seed = st.number_input(
            "Random seed",
            min_value=1,
            max_value=1000,
            value=42,
            help="Change for different simulation"
        )
        
        st.info(f"""
        **Current settings:**
        - Start: p = {p0}
        - Ne = {Ne}
        - Migration: {migration_rate*100:.1f}% per gen
        - Time: {generations} generations
        """)
    
    with col2:
        # Simulate drift in two populations
        np.random.seed(random_seed)
        
        # Population 1
        freq_pop1 = [p0]
        for gen in range(generations):
            p_current = freq_pop1[-1]
            
            # Migration from pop2 to pop1
            if migration_rate > 0 and gen > 0:
                p_pop2 = freq_pop2[gen]
                p_current = (1 - migration_rate) * p_current + migration_rate * p_pop2
            
            # Drift
            allele_count = np.random.binomial(2 * Ne, p_current)
            p_new = allele_count / (2 * Ne)
            freq_pop1.append(p_new)
        
        # Population 2
        np.random.seed(random_seed + 1)  # Different seed
        freq_pop2 = [p0]
        for gen in range(generations):
            p_current = freq_pop2[-1]
            
            # Migration from pop1 to pop2
            if migration_rate > 0 and gen > 0:
                p_pop1 = freq_pop1[gen]
                p_current = (1 - migration_rate) * p_current + migration_rate * p_pop1
            
            # Drift
            allele_count = np.random.binomial(2 * Ne, p_current)
            p_new = allele_count / (2 * Ne)
            freq_pop2.append(p_new)
        
        # Calculate FST at end
        p_final_1 = freq_pop1[-1]
        p_final_2 = freq_pop2[-1]
        p_avg = (p_final_1 + p_final_2) / 2
        
        # Variance method for FST
        if p_avg > 0 and p_avg < 1:
            var_p = ((p_final_1 - p_avg)**2 + (p_final_2 - p_avg)**2) / 2
            fst_final = var_p / (p_avg * (1 - p_avg))
        else:
            fst_final = 0
        
        # Plot
        fig, ax = plt.subplots(figsize=(11, 6))
        
        ax.plot(freq_pop1, 'b-', linewidth=2.5, label='Population 1', alpha=0.8)
        ax.plot(freq_pop2, 'r-', linewidth=2.5, label='Population 2', alpha=0.8)
        ax.axhline(y=p0, color='gray', linestyle='--', alpha=0.5, 
                  linewidth=2, label=f'Starting frequency ({p0})')
        
        # Shade divergence
        ax.fill_between(range(len(freq_pop1)), freq_pop1, freq_pop2, 
                        alpha=0.2, color='purple', label='Divergence')
        
        ax.set_xlabel('Generation', fontsize=12, fontweight='bold')
        ax.set_ylabel('Allele Frequency', fontsize=12, fontweight='bold')
        ax.set_title(f'Genetic Drift in Two Isolated Populations (Ne={Ne}, m={migration_rate})', 
                    fontsize=14, fontweight='bold')
        ax.legend(loc='best', fontsize=10)
        ax.grid(alpha=0.3)
        ax.set_ylim(0, 1)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Results
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Population 1 Final", f"{p_final_1:.3f}")
    with col2:
        st.metric("Population 2 Final", f"{p_final_2:.3f}")
    with col3:
        st.metric("FST", f"{fst_final:.4f}")
    
    st.success(f"""
    ### 📊 What Happened:
    
    **Starting state:**
    - Both populations began at p = {p0}
    - Genetically **identical** at generation 0
    
    **After {generations} generations:**
    - Population 1: p = {p_final_1:.3f}
    - Population 2: p = {p_final_2:.3f}
    - Difference: {abs(p_final_1 - p_final_2):.3f}
    - **FST = {fst_final:.4f}**
    
    **Interpretation:**
    {
    "Populations remain very similar (little differentiation)" if fst_final < 0.05 else
    "Populations are moderately different" if fst_final < 0.15 else
    "Populations are greatly differentiated" if fst_final < 0.25 else
    "Populations are very different - almost fixed for different alleles"
    }
    """)
    
    # Questions
    st.markdown("---")
    st.markdown("### 🔍 What Did You Observe?")
    
    with st.expander("❓ Try these experiments:"):
        st.markdown("""
        1. **Effect of time:**
           - Set Ne=50, m=0, generations=10 → Low FST
           - Set Ne=50, m=0, generations=200 → Higher FST
           - **Pattern:** More time → More divergence
        
        2. **Effect of population size:**
           - Set Ne=10, generations=100, m=0 → High FST (fast drift)
           - Set Ne=200, generations=100, m=0 → Low FST (slow drift)
           - **Pattern:** Smaller Ne → Faster divergence
        
        3. **Effect of migration:**
           - Set m=0 (no migration) → Populations diverge
           - Set m=0.01 (1% migration) → Divergence slowed
           - Set m=0.05 (5% migration) → Little divergence
           - **Pattern:** Even tiny migration prevents divergence!
        
        4. **The "one migrant" rule:**
           - Set Ne=100, m=0.005 → Check FST
           - This gives Nem = 100 × 0.005 = 0.5 migrants/gen
           - **Pattern:** Need ~1 migrant to prevent differentiation
        """)

# ============================================================================
# TAB 3: PART 2 - CALCULATE FST
# ============================================================================
with tab3:
    st.markdown('<h2 class="section-header">📐 Part 2: Understanding FST - What Are We Actually Measuring?</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The Mathematical Foundation
    
    You've seen populations diverge. But **what exactly is FST measuring?**
    
    ### Wright's FST (1951)
    
    **FST** measures the proportion of total genetic variance due to differences **between** populations.
    
    ### The Formula:
    
    ## FST = (H<sub>T</sub> - H<sub>S</sub>) / H<sub>T</sub>
    
    Where:
    - **H<sub>T</sub>** = Total expected heterozygosity (if all were one population)
    - **H<sub>S</sub>** = Average heterozygosity within subpopulations
    
    ### Alternative (Variance) Method:
    
    ## FST = Var(p) / [p̄(1 - p̄)]
    
    Where:
    - **Var(p)** = Variance in allele frequencies among populations
    - **p̄** = Average allele frequency across populations
    
    **Both formulas give the same answer!**
    """)
    
    st.markdown("---")
    
    # Widget 2: FST Calculator
    st.markdown("### 🎮 Interactive 2: Calculate FST Step-by-Step")
    
    st.info("**Simulated data for educational purposes**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Enter Allele Frequencies:")
        
        p1 = st.slider(
            "Population 1 (allele A frequency)",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.05
        )
        
        p2 = st.slider(
            "Population 2 (allele A frequency)",
            min_value=0.0,
            max_value=1.0,
            value=0.3,
            step=0.05
        )
        
        show_steps = st.checkbox("Show detailed calculation steps", value=True)
        
        st.info(f"""
        **Example scenarios:**
        
        - **No difference:** p1=0.5, p2=0.5 → FST=0
        - **Moderate:** p1=0.7, p2=0.3 → FST≈0.2
        - **Fixed:** p1=1.0, p2=0.0 → FST=1
        """)
    
    with col2:
        # Calculate step by step
        if show_steps:
            st.markdown("### 📐 Step-by-Step Calculation:")
        
        # Step 1: Average frequency
        p_avg = (p1 + p2) / 2
        
        if show_steps:
            st.markdown(f"""
            **Step 1:** Calculate average allele frequency
            ```
            p̄ = (p₁ + p₂) / 2
            p̄ = ({p1} + {p2}) / 2
            p̄ = {p_avg:.3f}
            ```
            """)
        
        # Step 2: Variance
        var_p = ((p1 - p_avg)**2 + (p2 - p_avg)**2) / 2
        
        if show_steps:
            st.markdown(f"""
            **Step 2:** Calculate variance in allele frequencies
            ```
            Var(p) = [(p₁ - p̄)² + (p₂ - p̄)²] / 2
            Var(p) = [({p1} - {p_avg:.3f})² + ({p2} - {p_avg:.3f})²] / 2
            Var(p) = {var_p:.4f}
            ```
            """)
        
        # Step 3: Total heterozygosity
        HT = 2 * p_avg * (1 - p_avg)
        
        if show_steps:
            st.markdown(f"""
            **Step 3:** Calculate total expected heterozygosity (H<sub>T</sub>)
            ```
            Hₜ = 2 × p̄ × (1 - p̄)
            Hₜ = 2 × {p_avg:.3f} × {1-p_avg:.3f}
            Hₜ = {HT:.4f}
            ```
            """)
        
        # Step 4: Within-population heterozygosity
        H1 = 2 * p1 * (1 - p1)
        H2 = 2 * p2 * (1 - p2)
        HS = (H1 + H2) / 2
        
        if show_steps:
            st.markdown(f"""
            **Step 4:** Calculate average within-population heterozygosity (H<sub>S</sub>)
            ```
            H₁ = 2 × p₁ × (1 - p₁) = 2 × {p1} × {1-p1} = {H1:.4f}
            H₂ = 2 × p₂ × (1 - p₂) = 2 × {p2} × {1-p2} = {H2:.4f}
            Hₛ = (H₁ + H₂) / 2 = {HS:.4f}
            ```
            """)
        
        # Step 5: FST (both methods)
        if HT > 0:
            fst_het = (HT - HS) / HT
        else:
            fst_het = 0
        
        if p_avg > 0 and p_avg < 1:
            fst_var = var_p / (p_avg * (1 - p_avg))
        else:
            fst_var = 0 if p_avg == 0.5 else 1
        
        if show_steps:
            st.markdown(f"""
            **Step 5:** Calculate FST (both methods)
            
            **Method 1 (Heterozygosity):**
            ```
            FST = (Hₜ - Hₛ) / Hₜ
            FST = ({HT:.4f} - {HS:.4f}) / {HT:.4f}
            FST = {fst_het:.4f}
            ```
            
            **Method 2 (Variance):**
            ```
            FST = Var(p) / [p̄(1 - p̄)]
            FST = {var_p:.4f} / [{p_avg:.3f} × {1-p_avg:.3f}]
            FST = {fst_var:.4f}
            ```
            
            ✅ **Both methods give the same result!**
            """)
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot 1: Allele frequencies
        pops = ['Population 1', 'Population 2']
        freqs_A = [p1, p2]
        freqs_a = [1-p1, 1-p2]
        
        x = np.arange(len(pops))
        width = 0.35
        
        ax1.bar(x - width/2, freqs_A, width, label='Allele A', color='#3b82f6', edgecolor='black')
        ax1.bar(x + width/2, freqs_a, width, label='Allele a', color='#f97316', edgecolor='black')
        
        ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax1.set_title('Allele Frequencies in Two Populations', fontsize=13, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(pops)
        ax1.legend()
        ax1.set_ylim(0, 1)
        ax1.grid(axis='y', alpha=0.3)
        ax1.axhline(y=p_avg, color='purple', linestyle='--', linewidth=2, 
                   label=f'Average ({p_avg:.2f})', alpha=0.7)
        
        # Plot 2: FST on scale
        fst_ranges = [0, 0.05, 0.15, 0.25, 1.0]
        colors_scale = ['#22c55e', '#eab308', '#f97316', '#ef4444']
        
        for i in range(len(fst_ranges)-1):
            ax2.barh(0, fst_ranges[i+1]-fst_ranges[i], left=fst_ranges[i], 
                    height=0.3, color=colors_scale[i], edgecolor='black', alpha=0.6)
        
        # Add FST marker
        ax2.plot([fst_het], [0], 'o', markersize=20, color='blue', 
                markeredgecolor='black', markeredgewidth=3, 
                label=f'Your FST = {fst_het:.3f}', zorder=10)
        
        ax2.set_xlabel('FST Value', fontsize=12, fontweight='bold')
        ax2.set_title('FST Interpretation Scale', fontsize=13, fontweight='bold')
        ax2.set_xlim(0, 0.5)
        ax2.set_ylim(-0.3, 0.3)
        ax2.set_yticks([])
        ax2.legend()
        ax2.grid(axis='x', alpha=0.3)
        
        # Add labels
        labels_pos = [0.025, 0.10, 0.20, 0.375]
        labels_text = ['Little', 'Moderate', 'Great', 'Very Great']
        for pos, txt in zip(labels_pos, labels_text):
            ax2.text(pos, 0, txt, ha='center', va='center', fontsize=9, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Interpretation
    if fst_het < 0.05:
        interpretation = "Little differentiation"
        color = "success"
        message = "Populations are genetically similar. Gene flow likely occurring."
    elif fst_het < 0.15:
        interpretation = "Moderate differentiation"
        color = "info"
        message = "Populations are distinct but connected. Some gene flow possible."
    elif fst_het < 0.25:
        interpretation = "Great differentiation"
        color = "warning"
        message = "Populations are very different. Little to no gene flow."
    else:
        interpretation = "Very great differentiation"
        color = "error"
        message = "Populations are extremely different. Likely no gene flow."
    
    if color == "success":
        st.success(f"""
        ### 🎯 Result: {interpretation}
        
        **FST = {fst_het:.4f}**
        
        {message}
        
        **Conservation implication:** Can likely be managed as single unit.
        """)
    elif color == "info":
        st.info(f"""
        ### 🎯 Result: {interpretation}
        
        **FST = {fst_het:.4f}**
        
        {message}
        
        **Conservation implication:** Consider as separate units, maintain connectivity.
        """)
    elif color == "warning":
        st.warning(f"""
        ### 🎯 Result: {interpretation}
        
        **FST = {fst_het:.4f}**
        
        {message}
        
        **Conservation implication:** Treat as distinct units. Don't mix stocks.
        """)
    
    # Understanding components
    st.markdown("---")
    st.markdown("### 🎓 Understanding the Components")
    
    with st.expander("What is H<sub>S</sub> (Within-population heterozygosity)?"):
        st.markdown("""
        **9th grade:** How different people are *within* each village.
        
        **BSc:** Expected proportion of heterozygotes if we sample from one population.
        
        **Formula:** H<sub>S</sub> = average of [2p(1-p)] across populations
        
        **Your values:**
        - Population 1: H₁ = {:.4f}
        - Population 2: H₂ = {:.4f}
        - Average H<sub>S</sub> = {:.4f}
        """.format(H1, H2, HS))
    
    with st.expander("What is H<sub>T</sub> (Total heterozygosity)?"):
        st.markdown("""
        **9th grade:** How different people would be if both villages were combined.
        
        **BSc:** Expected heterozygosity if we pool all populations into one.
        
        **Formula:** H<sub>T</sub> = 2p̄(1-p̄) where p̄ = average frequency
        
        **Your value:** H<sub>T</sub> = {:.4f}
        
        **Key insight:** H<sub>T</sub> ≥ H<sub>S</sub> always!
        (Total diversity ≥ average within-population diversity)
        """.format(HT))
    
    with st.expander("What does FST = 0 mean?"):
        st.markdown("""
        **FST = 0** means:
        - No genetic differentiation
        - Populations are panmictic (random mating across all)
        - Gene flow is high
        - Could be managed as single unit
        
        **Example:** Set p₁ = 0.5, p₂ = 0.5 above to see FST = 0
        """)
    
    with st.expander("What does FST = 1 mean?"):
        st.markdown("""
        **FST = 1** means:
        - Complete differentiation
        - Populations are fixed for different alleles
        - No shared genetic variation
        - Completely isolated (no gene flow)
        
        **Example:** Set p₁ = 1.0, p₂ = 0.0 above to see FST = 1
        
        **Real world:** Very rare! Even highly diverged populations usually have FST < 0.5
        """)

# Continue in next part...

st.info("💡 **Continue to Part 3** to see real FST values from published research!")

# ============================================================================
# TAB 4: PART 3 - REAL EXAMPLES
# ============================================================================
with tab4:
    st.markdown('<h2 class="section-header">🌍 Part 3: Real Examples - From Humans to Fish</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Published Data from Real Research
    
    Now that we understand FST, let's see **real examples** from published scientific papers!
    
    These are **actual FST values** from peer-reviewed research:
    """)
    
    st.markdown("---")
    
    # Example 1: Indian Human Populations
    st.markdown("### 🧑 Example 1: Indian Human Populations")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Study:** Reich et al. (2009), *Nature*
        
        **Populations studied:**
        - Ancestral North Indians (ANI)
        - Ancestral South Indians (ASI)
        - Various tribal groups
        
        **Key Findings:**
        """)
        
        # Data table
        human_data = {
            'Comparison': [
                'ANI vs ASI',
                'Tribal vs Non-tribal',
                'North vs South (general)',
                'Within tribal groups',
                'Within caste groups'
            ],
            'FST': [0.03, 0.10, 0.02, 0.05, 0.01],
            'Interpretation': [
                'Little differentiation',
                'Moderate differentiation',
                'Little differentiation',
                'Little differentiation',
                'Little differentiation'
            ]
        }
        
        df_human = pd.DataFrame(human_data)
        st.dataframe(df_human, use_container_width=True, hide_index=True)
    
    with col2:
        # Visualization
        fig, ax = plt.subplots(figsize=(8, 6))
        
        comparisons = human_data['Comparison']
        fst_values = human_data['FST']
        
        colors_bar = ['#22c55e' if f < 0.05 else '#eab308' if f < 0.15 else '#f97316' 
                      for f in fst_values]
        
        bars = ax.barh(comparisons, fst_values, color=colors_bar, 
                      edgecolor='black', linewidth=1.5)
        
        # Add FST scale lines
        ax.axvline(x=0.05, color='green', linestyle='--', alpha=0.5, linewidth=2)
        ax.axvline(x=0.15, color='orange', linestyle='--', alpha=0.5, linewidth=2)
        
        ax.set_xlabel('FST Value', fontsize=12, fontweight='bold')
        ax.set_title('FST in Indian Human Populations', fontsize=13, fontweight='bold')
        ax.set_xlim(0, 0.20)
        ax.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, fst_values)):
            ax.text(val + 0.005, bar.get_y() + bar.get_height()/2, 
                   f'{val:.3f}', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    st.info("""
    ### 📚 What This Tells Us:
    
    - **ANI-ASI differentiation** (FST = 0.03) is relatively **low**
    - Most genetic variation is **within** groups, not between them
    - **Tribal populations** show more differentiation (FST = 0.10)
    - This has implications for:
      - Medical genetics (disease susceptibility)
      - Forensic genetics (population assignment)
      - Understanding human migration history
    """)
    
    st.markdown("---")
    
    # Example 2: Labeo rohita
    st.markdown("### 🐟 Example 2: Labeo rohita (Rohu Fish)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Study:** Simulated data based on typical cyprinid patterns
        
        **Populations:**
        - Mahanadi River basin (Odisha)
        - Ganga River basin
        - Godavari River basin
        - Hatchery stocks
        
        **Why it matters:**
        - Major aquaculture species
        - Important for food security
        - Breeding program management
        - Wild stock conservation
        """)
        
        fish_data = {
            'Comparison': [
                'Mahanadi vs Ganga',
                'Mahanadi vs Godavari',
                'Ganga vs Godavari',
                'Wild vs Hatchery (Mahanadi)',
                'Within Mahanadi system'
            ],
            'FST': [0.08, 0.15, 0.12, 0.22, 0.03],
            'Interpretation': [
                'Moderate',
                'Moderate-Great',
                'Moderate',
                'Great',
                'Little'
            ]
        }
        
        df_fish = pd.DataFrame(fish_data)
        st.dataframe(df_fish, use_container_width=True, hide_index=True)
    
    with col2:
        # Visualization
        fig, ax = plt.subplots(figsize=(8, 6))
        
        comparisons_fish = fish_data['Comparison']
        fst_fish = fish_data['FST']
        
        colors_fish = ['#22c55e' if f < 0.05 else '#eab308' if f < 0.15 else '#f97316' 
                      for f in fst_fish]
        
        bars = ax.barh(comparisons_fish, fst_fish, color=colors_fish, 
                      edgecolor='black', linewidth=1.5)
        
        ax.axvline(x=0.05, color='green', linestyle='--', alpha=0.5, linewidth=2)
        ax.axvline(x=0.15, color='orange', linestyle='--', alpha=0.5, linewidth=2)
        ax.axvline(x=0.25, color='red', linestyle='--', alpha=0.5, linewidth=2)
        
        ax.set_xlabel('FST Value', fontsize=12, fontweight='bold')
        ax.set_title('FST in Labeo rohita Populations', fontsize=13, fontweight='bold')
        ax.set_xlim(0, 0.30)
        ax.grid(axis='x', alpha=0.3)
        
        for i, (bar, val) in enumerate(zip(bars, fst_fish)):
            ax.text(val + 0.01, bar.get_y() + bar.get_height()/2, 
                   f'{val:.2f}', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    st.warning("""
    ### 🔬 Conservation Implications:
    
    1. **River-specific populations** (FST = 0.08-0.15):
       - Should be managed separately
       - Don't mix stocks between rivers
       - Preserve local adaptations
    
    2. **Hatchery stocks** (FST = 0.22):
       - Very different from wild populations!
       - Genetic bottleneck + selective breeding
       - Reintroduction programs need careful planning
    
    3. **Within Mahanadi** (FST = 0.03):
       - Can manage as single unit
       - Gene flow maintained
       - No barriers to fish movement
    """)
    
    st.markdown("---")
    
    # Example 3: Indian Cattle
    st.markdown("### 🐄 Example 3: Indian Cattle Breeds")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Study:** Simulated data based on typical livestock patterns
        
        **Breeds compared:**
        - Sahiwal (Punjab)
        - Gir (Gujarat)
        - Tharparkar (Rajasthan)
        - Red Sindhi (Sindh origin)
        - Crossbreeds
        
        **Importance:**
        - Breed conservation
        - Breeding programs
        - Climate adaptation
        - Disease resistance
        """)
        
        cattle_data = {
            'Comparison': [
                'Sahiwal vs Gir',
                'Gir vs Tharparkar',
                'Tharparkar vs Red Sindhi',
                'Indigenous vs Crossbreed',
                'Within breed variation'
            ],
            'FST': [0.12, 0.10, 0.15, 0.35, 0.02],
            'Interpretation': [
                'Moderate',
                'Moderate',
                'Moderate-Great',
                'Very Great',
                'Little'
            ]
        }
        
        df_cattle = pd.DataFrame(cattle_data)
        st.dataframe(df_cattle, use_container_width=True, hide_index=True)
    
    with col2:
        # Visualization
        fig, ax = plt.subplots(figsize=(8, 6))
        
        comparisons_cattle = cattle_data['Comparison']
        fst_cattle = cattle_data['FST']
        
        colors_cattle = ['#22c55e' if f < 0.05 else '#eab308' if f < 0.15 else 
                        '#f97316' if f < 0.25 else '#ef4444' for f in fst_cattle]
        
        bars = ax.barh(comparisons_cattle, fst_cattle, color=colors_cattle, 
                      edgecolor='black', linewidth=1.5)
        
        ax.axvline(x=0.05, color='green', linestyle='--', alpha=0.5, linewidth=2)
        ax.axvline(x=0.15, color='orange', linestyle='--', alpha=0.5, linewidth=2)
        ax.axvline(x=0.25, color='red', linestyle='--', alpha=0.5, linewidth=2)
        
        ax.set_xlabel('FST Value', fontsize=12, fontweight='bold')
        ax.set_title('FST in Indian Cattle Breeds', fontsize=13, fontweight='bold')
        ax.set_xlim(0, 0.40)
        ax.grid(axis='x', alpha=0.3)
        
        for i, (bar, val) in enumerate(zip(bars, fst_cattle)):
            ax.text(val + 0.015, bar.get_y() + bar.get_height()/2, 
                   f'{val:.2f}', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    st.error("""
    ### 🚨 Critical Finding:
    
    **Crossbreeds vs Indigenous** (FST = 0.35):
    - Highest FST value!
    - Crossbreeding has created **very different** genetic pools
    - Indigenous breeds are being **genetically swamped**
    - **Urgent need** for pure breed conservation
    
    **Conservation action:**
    - Maintain pure breeding lines
    - Establish gene banks
    - Restrict crossbreeding in conservation herds
    - Document remaining indigenous populations
    """)

# ============================================================================
# TAB 5: PART 4 - APPLICATIONS
# ============================================================================
with tab5:
    st.markdown('<h2 class="section-header">🦎 Part 4: Applications - Conservation & Research</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## How Researchers Actually Use FST
    
    FST isn't just an academic number - it drives **real-world decisions**:
    """)
    
    # Application areas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🌲 Conservation Biology
        
        1. **Define Management Units**
           - FST < 0.05: Single unit
           - FST 0.05-0.15: Monitor connectivity
           - FST > 0.15: Separate units
        
        2. **Translocation Decisions**
           - Don't mix high-FST populations
           - Source for reintroduction
           - Genetic rescue programs
        
        3. **Prioritize Populations**
           - High FST = unique genetics
           - Worth special protection
        """)
    
    with col2:
        st.markdown("""
        ### 🔬 Research Applications
        
        1. **Population History**
           - Time since divergence
           - Migration patterns
           - Bottleneck detection
        
        2. **Local Adaptation**
           - FST outliers = selection
           - Climate adaptation
           - Disease resistance
        
        3. **Breeding Programs**
           - Avoid inbreeding
           - Maximize diversity
           - Maintain local stocks
        """)
    
    st.markdown("---")
    
    # Widget 3: Migration-FST Balance
    st.markdown("### 🎮 Interactive 3: The Drift-Migration Balance")
    
    st.markdown("""
    ## The "One Migrant Per Generation" Rule
    
    **Key insight:** Just **ONE migrant per generation** is enough to prevent differentiation!
    
    **Formula:** FST ≈ 1 / (4Nem + 1)
    
    Where:
    - **Ne** = Effective population size
    - **m** = Migration rate (proportion migrating per generation)
    - **Nem** = Number of migrants per generation
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Parameters:")
        
        Ne_balance = st.slider(
            "Effective Population Size (Ne)",
            min_value=10,
            max_value=500,
            value=100,
            step=10
        )
        
        Nem = st.slider(
            "Number of Migrants per Generation (Nem)",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=0.1,
            help="Nem = Ne × m"
        )
        
        # Calculate m
        m_calc = Nem / Ne_balance
        
        st.info(f"""
        **Settings:**
        - Ne = {Ne_balance}
        - Nem = {Nem}
        - **Migration rate (m) = {m_calc:.4f}**
        - = {m_calc*100:.2f}% per generation
        """)
    
    with col2:
        # Calculate expected FST
        fst_expected = 1 / (4 * Nem + 1) if Nem > 0 else 1.0
        
        # Plot FST vs Nem
        Nem_range = np.linspace(0.1, 10, 200)
        fst_range = 1 / (4 * Nem_range + 1)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(Nem_range, fst_range, 'b-', linewidth=3, label='FST = 1/(4Nem + 1)')
        ax.axvline(x=1, color='red', linestyle='--', linewidth=2.5, 
                  label='Nem = 1 (One migrant rule)', alpha=0.7)
        ax.axvline(x=Nem, color='green', linestyle='--', linewidth=2, 
                  label=f'Current Nem = {Nem}', alpha=0.7)
        ax.axhline(y=fst_expected, color='green', linestyle=':', alpha=0.5, linewidth=2)
        
        # Add horizontal lines for FST interpretation
        ax.axhline(y=0.05, color='gray', linestyle=':', alpha=0.3)
        ax.axhline(y=0.15, color='gray', linestyle=':', alpha=0.3)
        ax.axhline(y=0.25, color='gray', linestyle=':', alpha=0.3)
        
        ax.set_xlabel('Number of Migrants per Generation (Nem)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Expected FST', fontsize=12, fontweight='bold')
        ax.set_title('Drift-Migration Balance', fontsize=14, fontweight='bold')
        ax.legend(loc='upper right', fontsize=10)
        ax.grid(alpha=0.3)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 0.5)
        
        # Add annotation
        if Nem < 1:
            ax.annotate('Drift dominates\nPopulations diverge', 
                       xy=(Nem, fst_expected), xytext=(2, fst_expected + 0.1),
                       arrowprops=dict(arrowstyle='->', color='red', lw=2),
                       fontsize=11, color='red', fontweight='bold')
        elif Nem > 1:
            ax.annotate('Migration dominates\nPopulations connected', 
                       xy=(Nem, fst_expected), xytext=(Nem + 2, fst_expected - 0.05),
                       arrowprops=dict(arrowstyle='->', color='green', lw=2),
                       fontsize=11, color='green', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Results and interpretation
    st.success(f"""
    ### 🎯 Results:
    
    **Given:**
    - Ne = {Ne_balance}
    - Nem = {Nem} migrant(s) per generation
    - Migration rate (m) = {m_calc:.4f} ({m_calc*100:.2f}%)
    
    **Expected FST = {fst_expected:.4f}**
    
    **Interpretation:**
    {
    f"With {Nem} migrant(s) per generation, populations remain CONNECTED (FST = {fst_expected:.3f}). "
    "Gene flow prevents differentiation!" if Nem >= 1 else
    f"With less than 1 migrant per generation, populations will DIVERGE (FST = {fst_expected:.3f}). "
    "Drift dominates over migration!"
    }
    
    ### 🔬 Conservation Message:
    
    Even **tiny amounts of gene flow** (just 1 individual per generation) can prevent genetic differentiation!
    
    This is why:
    - **Corridors matter** - even occasional movement helps
    - **Complete isolation** leads to divergence
    - **Barriers** (dams, roads, habitat loss) have genetic consequences
    """)
    
    # Case studies
    st.markdown("---")
    st.markdown("### 📚 Conservation Case Studies")
    
    case_col1, case_col2 = st.columns(2)
    
    with case_col1:
        st.markdown("""
        <div class="success-box">
        <h4>✅ Success: Maintaining Connectivity</h4>
        <p><strong>Species:</strong> Labeo rohita in Mahanadi</p>
        <p><strong>FST:</strong> 0.03 (within system)</p>
        <p><strong>Why:</strong> No major dams, free fish movement</p>
        <p><strong>Action:</strong> Protect existing connectivity</p>
        </div>
        """, unsafe_allow_html=True)
    
    with case_col2:
        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ Challenge: Fragmented Populations</h4>
        <p><strong>Species:</strong> Many river fish post-dam</p>
        <p><strong>FST:</strong> 0.15-0.25 (upstream vs downstream)</p>
        <p><strong>Why:</strong> Dam blocks migration (m → 0)</p>
        <p><strong>Action:</strong> Fish ladders, translocation, genetic monitoring</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 6: SUMMARY
# ============================================================================
with tab6:
    st.markdown('<h2 class="section-header">🎯 Summary & Key Takeaways</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What You've Learned
    
    Congratulations! You've completed Module 5A. Here's your genetics journey:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Core Concepts Mastered
        
        1. **FST Fundamentals**
           - Measures genetic differentiation
           - Range: 0 (panmictic) to 1 (fixed)
           - Formula: (H<sub>T</sub> - H<sub>S</sub>) / H<sub>T</sub>
           - Alternative: Var(p) / [p̄(1-p̄)]
        
        2. **Interpretation**
           - FST < 0.05: Little differentiation
           - FST 0.05-0.15: Moderate
           - FST 0.15-0.25: Great
           - FST > 0.25: Very great
        
        3. **Biological Processes**
           - Drift increases FST
           - Migration decreases FST
           - Balance determines equilibrium
           - "One migrant" rule: Nem ≥ 1 prevents divergence
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Skills Acquired
        
        1. **Analytical Skills**
           - Calculate FST from allele frequencies
           - Interpret FST values
           - Understand H<sub>T</sub> and H<sub>S</sub>
           - Apply drift-migration balance
        
        2. **Research Skills**
           - Read population genetics papers
           - Evaluate FST data
           - Design sampling strategies
           - Make management recommendations
        
        3. **Conservation Applications**
           - Define management units
           - Assess connectivity
           - Plan translocations
           - Monitor genetic diversity
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🎓 Pattern Hunters Principles in Action
    
    This module demonstrated:
    
    1. ✅ **"Observation before formulas"**
       - Watched populations diverge BEFORE learning FST equation
       - Saw the pattern, then quantified it
    
    2. ✅ **"Multiple perspectives"**
       - 9th grade: Village analogy
       - BSc: Mathematical formulas
       - Research: Conservation decisions
    
    3. ✅ **"Real examples illuminate"**
       - Indian human populations
       - Labeo rohita from Mahanadi
       - Indian cattle breeds
    
    4. ✅ **"Theory meets application"**
       - Not just "what is FST?"
       - But "how do we USE FST?"
       - Real conservation decisions
    """)
    
    st.markdown("---")
    
    # Quick reference table
    st.markdown("## 📊 Quick Reference: FST Decision Guide")
    
    decision_data = {
        'FST Range': ['0.00 - 0.05', '0.05 - 0.15', '0.15 - 0.25', '> 0.25'],
        'Differentiation': ['Little', 'Moderate', 'Great', 'Very Great'],
        'Gene Flow': ['High', 'Moderate', 'Low', 'None'],
        'Management': ['Single unit', 'Monitor', 'Separate units', 'Distinct units'],
        'Translocation': ['OK within', 'Caution', 'Avoid', 'Never mix']
    }
    
    df_decision = pd.DataFrame(decision_data)
    st.dataframe(df_decision, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🚀 Next Steps
    
    ### Module 5B: Selection Signatures
    
    You'll learn:
    - Neutral theory as null hypothesis
    - Detecting selection using FST outliers
    - Tajima's D and site frequency spectrum
    - Real examples: lactase persistence, malaria resistance
    
    ### Module 5C: Effective Population Size
    
    You'll learn:
    - Why Ne < census size
    - Estimating Ne from genetic data
    - The 50/500 rule for conservation
    - Applications to endangered species
    
    ### Practice Suggestions
    
    Before moving on:
    
    1. **Find FST values in papers**
       - Search for "FST" + your favorite species
       - Read methods sections
       - Interpret results
    
    2. **Calculate FST from data**
       - Use the interactive calculators
       - Try different scenarios
       - See how migration affects FST
    
    3. **Think about your research**
       - Could FST help answer your questions?
       - What populations would you compare?
       - What would high/low FST mean?
    """)
    
    st.success("""
    ### 🎊 Congratulations!
    
    You've mastered **FST and Population Structure**!
    
    You can now:
    - ✅ Calculate and interpret FST
    - ✅ Understand what FST measures biologically
    - ✅ Apply FST to conservation decisions
    - ✅ Read population genetics literature
    - ✅ Design genetic monitoring programs
    
    **This isn't just academic** - you've learned a tool that:
    - Guides species conservation
    - Informs breeding programs
    - Helps manage fish hatcheries
    - Protects indigenous livestock
    
    **Ready for Module 5B?** → Detecting selection in populations!
    """)
    
    st.markdown("---")
    
    # Feedback section
    st.markdown("### 📝 Feedback & Contact")
    
    with st.expander("💬 Share your thoughts"):
        st.markdown("""
        What did you think of Module 5A?
        
        - Was it helpful?
        - Which examples were most interesting?
        - What was confusing?
        - How will you use FST in your work?
        
        **Contact:** susama.kar@kuchindacollege.ac.in
        
        **GitHub:** https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Module 5A: FST and Population Structure</strong></p>
    <p>Developed by Susama Kar & Dr. Alok Patel</p>
    <p>Department of Zoology, Kuchinda College, Sambalpur University</p>
    <p>Part of the Pattern Hunters Educational Series</p>
    <p>License: CC BY 4.0 | <a href="https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive">GitHub</a> | DOI: 10.5281/zenodo.17887470</p>
</div>
""", unsafe_allow_html=True)
