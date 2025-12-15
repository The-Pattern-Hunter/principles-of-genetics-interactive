"""
Module 5C: Effective Population Size (Ne) - The Genetic Bottleneck
COMPLETE STREAMLIT VERSION - Conservation Genetics Focus

An Interactive Journey from Census Size to Genetic Reality

Authors: Susama Kar & Dr. Alok Patel
Institution: Department of Zoology, Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# Page configuration
st.set_page_config(
    page_title="Module 5C: Effective Population Size",
    page_icon="🐟",
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
    .conservation-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        margin: 1rem 0;
    }
    .danger-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        color: white;
        margin: 1rem 0;
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
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🐟 Module 5C: Effective Population Size (Ne)</h1>', unsafe_allow_html=True)

st.markdown("""
**The Genetic Bottleneck - An Interactive Journey from Census Size to Genetic Reality**

**Authors:** Susama Kar & Dr. Alok Patel  
**Institution:** Department of Zoology, Kuchinda College, Sambalpur University

---
""")

# Pattern Hunters approach box
st.markdown("""
<div class="pattern-box">
<h3>🔍 The Pattern Hunters Approach</h3>
<p><strong>Traditional approach:</strong> "Count the fish, done!" ❌</p>
<p><strong>Pattern Hunters approach:</strong> "How many are GENETICALLY contributing?" ✅</p>
<ol>
<li><strong>OBSERVE:</strong> Census size doesn't predict genetic diversity</li>
<li><strong>UNDERSTAND:</strong> Why Ne < N (always!)</li>
<li><strong>MEASURE:</strong> Estimate Ne from genetic data</li>
<li><strong>DECIDE:</strong> Make evidence-based conservation decisions</li>
</ol>
<p><strong>Key insight:</strong> A population of 1000 might be genetically equivalent to only 100!</p>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Introduction",
    "🔬 Part 1: The Concept",
    "📐 Part 2: Estimation Methods",
    "🦎 Part 3: Conservation Applications",
    "🎯 Summary"
])

# ============================================================================
# TAB 1: INTRODUCTION
# ============================================================================
with tab1:
    st.markdown('<h2 class="section-header">Welcome to Conservation Genetics!</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## What You'll Learn
        
        This module teaches you **why counting individuals isn't enough** for conservation.
        
        ### The Journey:
        
        1. 🔬 **The Concept** - Why Ne < N (census size)?
        2. 📐 **Estimation** - Calculate Ne from genetic data
        3. 🦎 **Conservation** - Apply the 50/500 rule
        4. 🐟 **Real Example** - Labeo rohita management
        
        ## The Shocking Truth
        
        **You count 1000 fish in a pond.**
        
        ❌ **Wrong thinking:** "Great! Large population, safe from extinction!"
        
        ✅ **Correct thinking:** "What's the **effective** size (Ne)?"
        
        **Result:** Genetically, it might be only **200** fish!
        
        ## Why This Matters
        
        - **Ne < 50** → Immediate inbreeding depression
        - **Ne < 500** → Can't adapt to environmental change
        - **Ne determines:**
          - Rate of genetic drift
          - Loss of genetic diversity
          - Ability to respond to selection
          - Long-term viability
        
        ### Critical Conservation Decisions:
        
        - How many individuals to translocate?
        - Is supplementation needed?
        - Which populations to prioritize?
        - When is captive breeding necessary?
        
        **All depend on Ne, not census size!**
        """)
    
    with col2:
        st.info("""
        ### 📊 Module Stats
        
        - **Duration:** 60-90 min
        - **Level:** Conservation focus
        - **Widgets:** 2 interactive
        - **Applications:** Critical!
        - **Prerequisites:** Module 5A helpful
        
        ### 🎓 Learning Levels
        
        - **BSc:** Ne concept basics
        - **MSc:** Estimation methods
        - **Conservation:** 50/500 rule
        - **Management:** Decision-making
        """)
        
        st.markdown("""
        <div class="danger-box">
        <h4>⚠️ Conservation Crisis</h4>
        <p><strong>Common mistake:</strong></p>
        <p>"We have 500 individuals, we're safe!"</p>
        <p><strong>Reality:</strong></p>
        <p>If Ne/N = 0.2 (typical), Ne = 100</p>
        <p>❌ Below 500 threshold!</p>
        <p>✅ Need 2500+ census size for safety</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visual comparison
    st.markdown("## 🎯 Census Size vs Effective Size")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: The illusion
    census_sizes = [50, 200, 500, 1000, 2000]
    ne_sizes = [n * 0.2 for n in census_sizes]  # Ne/N = 0.2
    
    x = np.arange(len(census_sizes))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, census_sizes, width, label='Census Size (N)', 
                    color='#3b82f6', alpha=0.7, edgecolor='black', linewidth=2)
    bars2 = ax1.bar(x + width/2, ne_sizes, width, label='Effective Size (Ne)', 
                    color='#ef4444', alpha=0.7, edgecolor='black', linewidth=2)
    
    # Add threshold lines
    ax1.axhline(y=50, color='red', linestyle='--', linewidth=2.5, 
               label='Ne = 50 (Inbreeding risk)', alpha=0.7)
    ax1.axhline(y=500, color='orange', linestyle='--', linewidth=2.5, 
               label='Ne = 500 (Evolutionary potential)', alpha=0.7)
    
    ax1.set_xlabel('Population', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Size', fontsize=12, fontweight='bold')
    ax1.set_title('The Ne/N Disconnect (Ne/N = 0.2)', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([f'Pop {i+1}' for i in range(len(census_sizes))])
    ax1.legend(fontsize=9)
    ax1.grid(axis='y', alpha=0.3)
    
    # Plot 2: Factors reducing Ne
    factors = ['Sex Ratio\n(1:4)', 'Offspring\nVariance', 'Non-random\nMating', 
               'Overlapping\nGenerations', 'Population\nFluctuation']
    reductions = [0.67, 0.50, 0.70, 0.85, 0.60]
    
    colors_factors = ['#ef4444' if r < 0.7 else '#f97316' for r in reductions]
    
    bars = ax2.barh(factors, reductions, color=colors_factors, alpha=0.7, 
                    edgecolor='black', linewidth=2)
    ax2.axvline(x=1.0, color='green', linestyle='--', linewidth=2, 
               label='Ideal (Ne/N = 1.0)', alpha=0.7)
    ax2.set_xlabel('Ne/N Ratio', fontsize=12, fontweight='bold')
    ax2.set_title('Factors Reducing Effective Size', fontsize=13, fontweight='bold')
    ax2.set_xlim(0, 1.1)
    ax2.legend(fontsize=9)
    ax2.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for bar, val in zip(bars, reductions):
        width_bar = bar.get_width()
        ax2.text(width_bar + 0.02, bar.get_y() + bar.get_height()/2, 
                f'{val:.2f}', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.warning("""
    ### 🔑 Key Insight:
    
    **Multiple factors combine multiplicatively!**
    
    If Ne/N = 0.67 (sex ratio) × 0.50 (variance) × 0.70 (mating) = **0.23**
    
    A population of 1000 → Ne = 230
    
    **This is why we measure Ne, not just count individuals!**
    """)
    
    st.success("👆 **Start with Part 1** to understand why Ne < N!")

# ============================================================================
# TAB 2: PART 1 - THE CONCEPT
# ============================================================================
with tab2:
    st.markdown('<h2 class="section-header">🔬 Part 1: The Concept - Why Ne < N?</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The Surprising Discovery
    
    You count **1000 fish** in a pond. But genetically, it's as if only **200** are contributing!
    
    ### What Is Effective Population Size (Ne)?
    
    **Definition:** The size of an **idealized population** that would experience the same rate of genetic drift as the actual population.
    
    ### The Idealized Population:
    
    1. **Equal sex ratio** (50% male, 50% female)
    2. **Random mating** (everyone has equal chance)
    3. **Equal reproductive success** (same # offspring)
    4. **Discrete generations** (no overlap)
    5. **Constant size** (no fluctuations)
    
    **Reality:** Natural populations violate ALL of these!
    
    ## Why Ne < N: The Five Factors
    
    ### 1. **Unequal Sex Ratio**
    
    **Formula:** Ne = (4 × Nm × Nf) / (Nm + Nf)
    
    Where:
    - Nm = number of breeding males
    - Nf = number of breeding females
    
    **Example:**
    - 10 males, 90 females → Ne = 36 (not 100!)
    - 90 males, 10 females → Ne = 36 (same!)
    
    **Why:** Rarer sex is bottleneck
    
    ### 2. **Variance in Reproductive Success**
    
    Some individuals have many offspring, others have none.
    
    **Formula:** Ne ≈ N / (1 + Vk/k̄)
    
    Where:
    - Vk = variance in offspring number
    - k̄ = mean offspring number
    
    **Example:**
    - Ideal: Everyone has 2 offspring → Vk = 0 → Ne = N
    - Real: Some have 10, some have 0 → Vk = 25 → Ne = 0.1N
    
    **This is the BIGGEST reducer in fish!**
    
    ### 3. **Non-Random Mating**
    
    - Inbreeding reduces Ne
    - Assortative mating reduces Ne
    - Population structure reduces Ne
    
    ### 4. **Overlapping Generations**
    
    - Age structure affects Ne
    - Long-lived species: Ne > N possible!
    - But usually still reduces effective size
    
    ### 5. **Population Fluctuations**
    
    **Harmonic mean effect:**
    
    Ne = t / (1/N1 + 1/N2 + ... + 1/Nt)
    
    **Example:**
    - Year 1: N = 1000
    - Year 2: N = 100 (bottleneck!)
    - Year 3: N = 1000
    
    Average N = 700, but **Ne = 180!**
    
    **Bottlenecks have disproportionate effect!**
    """)
    
    st.markdown("---")
    
    # Widget 1: Ne/N Ratio Explorer
    st.markdown("### 🎮 Interactive 1: Explore Ne/N Ratio")
    
    st.info("**EDUCATIONAL SIMULATION - See how various factors reduce Ne below census size N!**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Population Parameters:")
        
        census_size = st.slider(
            "Census Population Size (N)",
            min_value=100,
            max_value=5000,
            value=1000,
            step=100
        )
        
        st.markdown("#### Breeding Structure:")
        
        sex_ratio = st.slider(
            "Sex Ratio (% female)",
            min_value=10,
            max_value=90,
            value=50,
            step=5,
            help="Ideal = 50%"
        )
        
        breeding_adults = st.slider(
            "% Adults that breed",
            min_value=20,
            max_value=100,
            value=80,
            step=5
        )
        
        offspring_variance = st.slider(
            "Variance in offspring number",
            min_value=0.0,
            max_value=50.0,
            value=10.0,
            step=1.0,
            help="0 = equal, higher = more unequal"
        )
        
        st.markdown("#### Population Dynamics:")
        
        has_bottleneck = st.checkbox("Include recent bottleneck", value=False)
        
        if has_bottleneck:
            bottleneck_size = st.slider(
                "Bottleneck size (min population)",
                min_value=10,
                max_value=500,
                value=100,
                step=10
            )
            generations_ago = st.slider(
                "Generations since bottleneck",
                min_value=1,
                max_value=10,
                value=3,
                step=1
            )
    
    with col2:
        # Calculate Ne components
        
        # 1. Sex ratio effect
        n_female = int(census_size * sex_ratio / 100)
        n_male = census_size - n_female
        
        ne_sex = (4 * n_male * n_female) / (n_male + n_female) if (n_male + n_female) > 0 else census_size
        sex_ratio_factor = ne_sex / census_size
        
        # 2. Breeding adults
        n_breeding = int(census_size * breeding_adults / 100)
        breeding_factor = breeding_adults / 100
        
        # 3. Offspring variance
        mean_offspring = 2.0
        ve = offspring_variance
        ne_variance = n_breeding / (1 + ve / mean_offspring)
        variance_factor = ne_variance / n_breeding if n_breeding > 0 else 1.0
        
        # Combined Ne (before bottleneck)
        ne_current = census_size * sex_ratio_factor * breeding_factor * variance_factor
        
        # 4. Bottleneck effect (harmonic mean)
        if has_bottleneck:
            # Simulate harmonic mean over generations
            sizes = [bottleneck_size] + [census_size] * (generations_ago - 1) + [census_size]
            ne_harmonic = len(sizes) / sum(1/s for s in sizes)
            bottleneck_factor = ne_harmonic / census_size
            ne_final = ne_current * bottleneck_factor
        else:
            bottleneck_factor = 1.0
            ne_final = ne_current
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
        
        # Plot 1: Step-by-step reduction
        stages = ['Census\nSize (N)', 'After\nSex Ratio', 'After\nBreeding %', 
                 'After\nVariance', 'Final Ne']
        values = [census_size, ne_sex, ne_sex * breeding_factor, 
                 ne_current, ne_final]
        
        if has_bottleneck:
            stages.append('After\nBottleneck')
            values.append(ne_final)
        
        colors_stages = ['#3b82f6', '#10b981', '#f59e0b', '#f97316', '#ef4444']
        if has_bottleneck:
            colors_stages.append('#991b1b')
        
        bars = ax1.bar(range(len(stages)), values, color=colors_stages[:len(stages)], 
                      alpha=0.7, edgecolor='black', linewidth=2)
        
        # Add threshold lines
        ax1.axhline(y=50, color='red', linestyle='--', linewidth=2.5, 
                   label='Ne = 50 (Critical)', alpha=0.7)
        ax1.axhline(y=500, color='orange', linestyle='--', linewidth=2.5, 
                   label='Ne = 500 (Target)', alpha=0.7)
        
        ax1.set_ylabel('Population Size', fontsize=12, fontweight='bold')
        ax1.set_title('Step-by-Step Reduction to Ne', fontsize=13, fontweight='bold')
        ax1.set_xticks(range(len(stages)))
        ax1.set_xticklabels(stages, fontsize=9)
        ax1.legend(fontsize=9)
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, values)):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(val)}', ha='center', va='bottom', 
                    fontsize=10, fontweight='bold')
        
        # Plot 2: Factor contributions
        factor_names = ['Sex Ratio', 'Breeding %', 'Offspring\nVariance']
        factor_values = [sex_ratio_factor, breeding_factor, variance_factor]
        
        if has_bottleneck:
            factor_names.append('Bottleneck')
            factor_values.append(bottleneck_factor)
        
        colors_factors = ['#ef4444' if f < 0.5 else '#f97316' if f < 0.7 else '#22c55e' 
                         for f in factor_values]
        
        bars2 = ax2.barh(factor_names, factor_values, color=colors_factors, 
                        alpha=0.7, edgecolor='black', linewidth=2)
        ax2.axvline(x=1.0, color='green', linestyle='--', linewidth=2, 
                   label='No reduction', alpha=0.7)
        ax2.set_xlabel('Reduction Factor (Ne/N)', fontsize=12, fontweight='bold')
        ax2.set_title('Individual Factor Contributions', fontsize=13, fontweight='bold')
        ax2.set_xlim(0, 1.1)
        ax2.legend(fontsize=9)
        ax2.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for bar, val in zip(bars2, factor_values):
            width_val = bar.get_width()
            ax2.text(width_val + 0.02, bar.get_y() + bar.get_height()/2, 
                    f'{val:.3f}', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Results summary
    ne_n_ratio = ne_final / census_size
    
    if ne_final < 50:
        st.error(f"""
        ### 🚨 **CRITICAL: Ne = {ne_final:.0f}**
        
        **Ne/N Ratio:** {ne_n_ratio:.3f}
        
        **Status:** ❌ Below 50 threshold!
        
        **Immediate risks:**
        - Inbreeding depression
        - Loss of genetic diversity
        - Reduced fitness
        - Elevated extinction risk
        
        **Required action:**
        - Genetic rescue (translocation)
        - Captive breeding program
        - Habitat restoration to increase N
        - **Target: Increase census size to {50/ne_n_ratio:.0f}+ for Ne > 50**
        """)
    elif ne_final < 500:
        st.warning(f"""
        ### ⚠️ **CONCERN: Ne = {ne_final:.0f}**
        
        **Ne/N Ratio:** {ne_n_ratio:.3f}
        
        **Status:** ⚠️ Between 50-500 (vulnerable)
        
        **Short-term:** Okay (avoiding inbreeding)
        **Long-term:** At risk (limited evolutionary potential)
        
        **Recommendations:**
        - Monitor genetic diversity
        - Maintain/increase census size
        - Prevent further bottlenecks
        - **Target: Increase census size to {500/ne_n_ratio:.0f}+ for Ne > 500**
        """)
    else:
        st.success(f"""
        ### ✅ **HEALTHY: Ne = {ne_final:.0f}**
        
        **Ne/N Ratio:** {ne_n_ratio:.3f}
        
        **Status:** ✅ Above 500 threshold!
        
        **Population health:**
        - Adequate genetic diversity
        - Can respond to selection
        - Long-term evolutionary potential
        - Low extinction risk (genetics)
        
        **Management:**
        - Maintain current conditions
        - Monitor for changes
        - Prevent habitat fragmentation
        """)
    
    # Breakdown table
    st.markdown("### 📊 Detailed Breakdown:")
    
    breakdown_data = {
        'Factor': ['Sex Ratio', 'Breeding Adults', 'Offspring Variance', 
                  'Bottleneck' if has_bottleneck else None, 'TOTAL'],
        'Reduction Factor': [f'{sex_ratio_factor:.3f}', f'{breeding_factor:.3f}', 
                           f'{variance_factor:.3f}',
                           f'{bottleneck_factor:.3f}' if has_bottleneck else None,
                           f'{ne_n_ratio:.3f}'],
        'Effective Size': [f'{ne_sex:.0f}', f'{ne_sex * breeding_factor:.0f}',
                          f'{ne_current:.0f}',
                          f'{ne_final:.0f}' if has_bottleneck else None,
                          f'{ne_final:.0f}']
    }
    
    # Remove None values
    breakdown_data = {k: [v for v in vals if v is not None] 
                     for k, vals in breakdown_data.items()}
    
    df_breakdown = pd.DataFrame(breakdown_data)
    st.dataframe(df_breakdown, use_container_width=True, hide_index=True)

# ============================================================================
# TAB 3: PART 2 - ESTIMATION METHODS
# ============================================================================
with tab3:
    st.markdown('<h2 class="section-header">📐 Part 2: Estimation Methods</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## How Do We Estimate Ne From Genetic Data?
    
    We rarely know the true breeding structure of populations. But we can **estimate Ne** from genetic data!
    
    ### Three Main Approaches:
    """)
    
    # Methods table
    methods_data = {
        'Method': [
            '1. Linkage Disequilibrium (LD)',
            '2. Temporal (2-sample)',
            '3. Heterozygosity Excess'
        ],
        'What It Uses': [
            'Non-random association between loci',
            'Allele frequency changes over time',
            'Deviation from HWE in offspring'
        ],
        'Best For': [
            'Single time point, current Ne',
            'Historical Ne, population trends',
            'Recent bottlenecks'
        ],
        'Data Required': [
            'Many loci (10+ SNPs), one sample',
            'Two samples separated by generations',
            'Parent-offspring data'
        ],
        'Time Scale': [
            'Current generation',
            'Between samples (1-10 gen)',
            '1-2 generations back'
        ]
    }
    
    df_methods = pd.DataFrame(methods_data)
    st.dataframe(df_methods, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Method 1: Linkage Disequilibrium (LD)
        
        **Principle:** Small Ne → stronger genetic drift → more random LD
        
        **Formula:** Ne ≈ 1 / (3r̂²)
        
        Where r̂² = mean linkage disequilibrium across loci pairs
        
        **Example calculation:**
        - Genotype 20 loci in 50 individuals
        - Calculate r² for all locus pairs
        - Correct for sample size
        - Average r̂² = 0.033
        - **Ne ≈ 1 / (3 × 0.033) = 10**
        
        **Advantages:**
        - Single sample needed
        - Estimates current Ne
        - Works with any markers (SNPs, microsatellites)
        
        **Limitations:**
        - Needs many loci (20+)
        - Sensitive to population structure
        - Assumes random mating
        
        **Software:** NeEstimator, LDNe
        """)
        
        st.markdown("""
        ### Method 2: Temporal (Two-Sample)
        
        **Principle:** Genetic drift changes allele frequencies; rate depends on Ne
        
        **Formula:** Ne ≈ t / (2 × ΔF)
        
        Where:
        - t = generations between samples
        - ΔF = standardized variance in allele frequency change
        
        **Example:**
        - Sample in 2000 and 2020
        - Generation time = 2 years → t = 10 generations
        - ΔF = 0.05 (calculated from data)
        - **Ne ≈ 10 / (2 × 0.05) = 100**
        
        **Advantages:**
        - Gold standard method
        - Direct estimate of drift rate
        - Integrates effects over time
        
        **Limitations:**
        - Needs two time points
        - Long generation time = slow
        - Affected by migration
        
        **Best for:** Long-term monitoring programs
        """)
    
    with col2:
        # LD method visualization
        st.markdown("#### LD Method - Visual Explanation")
        
        # Simulate LD patterns for different Ne
        np.random.seed(42)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Small Ne (strong drift)
        ne_small = 20
        r2_small = np.random.exponential(scale=1/(3*ne_small), size=100)
        r2_small = np.minimum(r2_small, 1.0)
        
        ax1.hist(r2_small, bins=20, color='#ef4444', alpha=0.7, 
                edgecolor='black', label=f'Ne = {ne_small}')
        ax1.axvline(x=np.mean(r2_small), color='red', linestyle='--', 
                   linewidth=3, label=f'Mean r² = {np.mean(r2_small):.3f}')
        ax1.set_xlabel('r² (Linkage Disequilibrium)', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Frequency', fontsize=11, fontweight='bold')
        ax1.set_title('Small Ne → High LD (Strong Drift)', fontsize=12, fontweight='bold')
        ax1.legend()
        ax1.grid(alpha=0.3, axis='y')
        
        # Large Ne (weak drift)
        ne_large = 500
        r2_large = np.random.exponential(scale=1/(3*ne_large), size=100)
        r2_large = np.minimum(r2_large, 1.0)
        
        ax2.hist(r2_large, bins=20, color='#22c55e', alpha=0.7, 
                edgecolor='black', label=f'Ne = {ne_large}')
        ax2.axvline(x=np.mean(r2_large), color='green', linestyle='--', 
                   linewidth=3, label=f'Mean r² = {np.mean(r2_large):.4f}')
        ax2.set_xlabel('r² (Linkage Disequilibrium)', fontsize=11, fontweight='bold')
        ax2.set_ylabel('Frequency', fontsize=11, fontweight='bold')
        ax2.set_title('Large Ne → Low LD (Weak Drift)', fontsize=12, fontweight='bold')
        ax2.legend()
        ax2.grid(alpha=0.3, axis='y')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        st.info("""
        **Key insight:**
        - Small Ne → High background LD
        - Large Ne → Low background LD
        - Measure average LD → Estimate Ne
        """)
    
    st.markdown("---")
    
    # Interactive calculator
    st.markdown("### 🎮 Interactive 2: Ne Estimation Calculator")
    
    st.info("**EDUCATIONAL TOOL - Simulate Ne estimation from data**")
    
    calc_col1, calc_col2 = st.columns([1, 2])
    
    with calc_col1:
        st.markdown("#### Choose Method:")
        
        estimation_method = st.selectbox(
            "Estimation approach",
            options=['Linkage Disequilibrium (LD)', 'Temporal (2-sample)', 'Both methods']
        )
        
        if 'LD' in estimation_method or estimation_method == 'Both methods':
            st.markdown("**LD Method Parameters:**")
            
            num_loci = st.slider(
                "Number of loci genotyped",
                min_value=10,
                max_value=100,
                value=30,
                step=5
            )
            
            sample_size_ld = st.slider(
                "Sample size",
                min_value=20,
                max_value=200,
                value=50,
                step=10
            )
            
            mean_r2 = st.slider(
                "Observed mean r² (from data)",
                min_value=0.001,
                max_value=0.2,
                value=0.02,
                step=0.001,
                format="%.3f"
            )
        
        if 'Temporal' in estimation_method or estimation_method == 'Both methods':
            st.markdown("**Temporal Method Parameters:**")
            
            years_between = st.slider(
                "Years between samples",
                min_value=2,
                max_value=50,
                value=10,
                step=2
            )
            
            generation_time = st.slider(
                "Generation time (years)",
                min_value=1,
                max_value=10,
                value=2,
                step=1
            )
            
            delta_f = st.slider(
                "ΔF (standardized variance)",
                min_value=0.001,
                max_value=0.2,
                value=0.03,
                step=0.001,
                format="%.3f"
            )
    
    with calc_col2:
        st.markdown("### 📊 Estimation Results:")
        
        results = []
        
        if 'LD' in estimation_method or estimation_method == 'Both methods':
            # LD method calculation
            # Correct for sample size
            r2_corrected = mean_r2 - (1 / sample_size_ld)
            r2_corrected = max(r2_corrected, 0.001)
            
            ne_ld = 1 / (3 * r2_corrected)
            
            st.markdown(f"""
            #### Linkage Disequilibrium Method:
            
            **Calculation:**
            ```
            Step 1: Correct r² for sample size
            r̂² = r²_observed - 1/n
            r̂² = {mean_r2:.4f} - 1/{sample_size_ld}
            r̂² = {r2_corrected:.4f}
            
            Step 2: Calculate Ne
            Ne = 1 / (3 × r̂²)
            Ne = 1 / (3 × {r2_corrected:.4f})
            Ne = {ne_ld:.1f}
            ```
            
            **95% Confidence Interval:** ({ne_ld*0.7:.1f} - {ne_ld*1.5:.1f})
            *Note: CI depends on number of loci*
            """)
            
            results.append(('LD Method', ne_ld, ne_ld*0.7, ne_ld*1.5))
        
        if 'Temporal' in estimation_method or estimation_method == 'Both methods':
            # Temporal method calculation
            t = years_between / generation_time
            ne_temporal = t / (2 * delta_f)
            
            st.markdown(f"""
            #### Temporal (Two-Sample) Method:
            
            **Calculation:**
            ```
            Step 1: Calculate generations
            t = years / generation_time
            t = {years_between} / {generation_time}
            t = {t:.1f} generations
            
            Step 2: Calculate Ne
            Ne = t / (2 × ΔF)
            Ne = {t:.1f} / (2 × {delta_f:.4f})
            Ne = {ne_temporal:.1f}
            ```
            
            **95% Confidence Interval:** ({ne_temporal*0.6:.1f} - {ne_temporal*2.0:.1f})
            *Note: CI depends on allele frequency variance*
            """)
            
            results.append(('Temporal Method', ne_temporal, ne_temporal*0.6, ne_temporal*2.0))
        
        # Visualization
        if results:
            fig, ax = plt.subplots(figsize=(11, 6))
            
            methods_plot = [r[0] for r in results]
            ne_estimates = [r[1] for r in results]
            ci_lower = [r[2] for r in results]
            ci_upper = [r[3] for r in results]
            
            colors_est = ['#3b82f6', '#10b981'][:len(results)]
            
            # Bar plot with error bars
            bars = ax.barh(methods_plot, ne_estimates, color=colors_est, 
                          alpha=0.7, edgecolor='black', linewidth=2)
            
            # Add confidence intervals
            for i, (method, ne_est, ci_l, ci_u) in enumerate(results):
                ax.plot([ci_l, ci_u], [i, i], 'k-', linewidth=3, alpha=0.7)
                ax.plot([ci_l, ci_l], [i-0.1, i+0.1], 'k-', linewidth=2)
                ax.plot([ci_u, ci_u], [i-0.1, i+0.1], 'k-', linewidth=2)
            
            # Add threshold lines
            ax.axvline(x=50, color='red', linestyle='--', linewidth=2.5, 
                      label='Ne = 50 (Critical)', alpha=0.7)
            ax.axvline(x=500, color='orange', linestyle='--', linewidth=2.5, 
                      label='Ne = 500 (Target)', alpha=0.7)
            
            ax.set_xlabel('Effective Population Size (Ne)', fontsize=12, fontweight='bold')
            ax.set_title('Ne Estimates with 95% Confidence Intervals', 
                        fontsize=13, fontweight='bold')
            ax.legend(fontsize=10)
            ax.grid(axis='x', alpha=0.3)
            ax.set_xlim(0, max(ne_estimates) * 2.5)
            
            # Add value labels
            for i, (bar, val) in enumerate(zip(bars, ne_estimates)):
                width = bar.get_width()
                ax.text(width + max(ne_estimates)*0.05, bar.get_y() + bar.get_height()/2, 
                       f'Ne = {val:.0f}', va='center', fontsize=11, fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        # Interpretation
        if results:
            avg_ne = np.mean([r[1] for r in results])
            
            if avg_ne < 50:
                st.error(f"""
                ### 🚨 Critical Ne Estimate
                
                **Average Ne ≈ {avg_ne:.0f}**
                
                ❌ **Below 50 threshold** - Immediate conservation concern!
                
                **Actions needed:**
                - Genetic rescue (translocation from other populations)
                - Captive breeding to increase Ne
                - Habitat restoration
                - Remove barriers to gene flow
                """)
            elif avg_ne < 500:
                st.warning(f"""
                ### ⚠️ Moderate Ne Estimate
                
                **Average Ne ≈ {avg_ne:.0f}**
                
                ⚠️ **Between 50-500** - Monitor closely
                
                **Recommendations:**
                - Continue genetic monitoring
                - Maintain/increase census size
                - Preserve connectivity
                - Plan for long-term viability
                """)
            else:
                st.success(f"""
                ### ✅ Healthy Ne Estimate
                
                **Average Ne ≈ {avg_ne:.0f}**
                
                ✅ **Above 500 threshold** - Good genetic health
                
                **Continue:**
                - Current management
                - Periodic monitoring
                - Habitat protection
                """)

# ============================================================================
# TAB 4: PART 3 - CONSERVATION APPLICATIONS
# ============================================================================
with tab4:
    st.markdown('<h2 class="section-header">🦎 Part 3: Conservation Applications</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The 50/500 Rule
    
    **One of the most important rules in conservation genetics!**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="danger-box">
        <h3>🚨 Ne = 50 (Short-term)</h3>
        <p><strong>The Inbreeding Threshold</strong></p>
        <ul>
        <li>Minimum to avoid inbreeding depression</li>
        <li>Maintain fitness in short term (1-10 generations)</li>
        <li>Below this: immediate genetic problems</li>
        </ul>
        <p><strong>What happens below 50:</strong></p>
        <ul>
        <li>❌ Reduced survival</li>
        <li>❌ Lower reproduction</li>
        <li>❌ Increased disease susceptibility</li>
        <li>❌ Developmental abnormalities</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="conservation-box">
        <h3>✅ Ne = 500 (Long-term)</h3>
        <p><strong>The Evolutionary Potential Threshold</strong></p>
        <ul>
        <li>Maintain adaptive potential</li>
        <li>Respond to environmental change</li>
        <li>Long-term persistence (100+ generations)</li>
        </ul>
        <p><strong>What this ensures:</strong></p>
        <ul>
        <li>✅ Balance drift vs mutation</li>
        <li>✅ Maintain quantitative variation</li>
        <li>✅ Adapt to climate change</li>
        <li>✅ Resist new diseases</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Real example: Labeo rohita
    st.markdown("### 🐟 Case Study: Labeo rohita (Rohu) in Mahanadi River")
    
    st.markdown("""
    **Background:**
    - Major aquaculture species in India
    - Mahanadi River population fragmented by dams
    - Wild stocks declining
    - Hatchery supplementation common
    
    **Genetic Assessment:**
    """)
    
    # Simulate Labeo data
    labeo_data = {
        'Population': [
            'Upstream (wild)',
            'Downstream (wild)',
            'Hatchery Stock 1',
            'Hatchery Stock 2',
            'Combined Wild'
        ],
        'Census Size (N)': [2500, 8000, 500, 300, 10500],
        'Estimated Ne': [180, 420, 35, 22, 520],
        'Ne/N Ratio': [0.07, 0.05, 0.07, 0.07, 0.05],
        'Status': ['⚠️ Concern', '✅ OK', '🚨 Critical', '🚨 Critical', '✅ Healthy']
    }
    
    df_labeo = pd.DataFrame(labeo_data)
    st.dataframe(df_labeo, use_container_width=True, hide_index=True)
    
    # Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: N vs Ne
    pops = labeo_data['Population']
    n_vals = labeo_data['Census Size (N)']
    ne_vals = labeo_data['Estimated Ne']
    
    x = np.arange(len(pops))
    width = 0.35
    
    ax1.bar(x - width/2, n_vals, width, label='Census Size (N)', 
           color='#3b82f6', alpha=0.7, edgecolor='black', linewidth=1.5)
    ax1.bar(x + width/2, ne_vals, width, label='Effective Size (Ne)', 
           color='#ef4444', alpha=0.7, edgecolor='black', linewidth=1.5)
    
    ax1.axhline(y=50, color='red', linestyle='--', linewidth=2, 
               label='Ne = 50', alpha=0.7)
    ax1.axhline(y=500, color='orange', linestyle='--', linewidth=2, 
               label='Ne = 500', alpha=0.7)
    
    ax1.set_ylabel('Size', fontsize=12, fontweight='bold')
    ax1.set_title('Census vs Effective Size', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(pops, rotation=45, ha='right', fontsize=9)
    ax1.legend(fontsize=9)
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_yscale('log')
    
    # Plot 2: Ne/N ratio
    ne_n_ratios = labeo_data['Ne/N Ratio']
    colors_ratio = ['#ef4444' if r < 0.1 else '#f97316' if r < 0.2 else '#22c55e' 
                   for r in ne_n_ratios]
    
    bars = ax2.barh(pops, ne_n_ratios, color=colors_ratio, alpha=0.7, 
                    edgecolor='black', linewidth=2)
    ax2.axvline(x=0.2, color='green', linestyle='--', linewidth=2, 
               label='Typical (0.2)', alpha=0.7)
    ax2.set_xlabel('Ne/N Ratio', fontsize=12, fontweight='bold')
    ax2.set_title('Effective/Census Ratio', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(axis='x', alpha=0.3)
    ax2.set_xlim(0, 0.3)
    
    # Add value labels
    for bar, val in zip(bars, ne_n_ratios):
        width_bar = bar.get_width()
        ax2.text(width_bar + 0.005, bar.get_y() + bar.get_height()/2, 
                f'{val:.2f}', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    # Management recommendations
    st.markdown("""
    ### 📋 Management Recommendations:
    
    #### 1. **Hatchery Stocks** (Ne = 22-35)
    
    🚨 **Critical status** - Immediate action required:
    - Increase number of broodstock (aim for 200+ individuals)
    - Equalize sex ratio (currently male-biased)
    - Equalize reproductive contribution (avoid few males dominating)
    - **Do NOT use for reintroduction without genetic rescue first**
    
    #### 2. **Upstream Wild** (Ne = 180)
    
    ⚠️ **Vulnerable** - Below 500 threshold:
    - Dam has fragmented population
    - Consider fish ladder installation
    - Allow limited migration between up/downstream
    - **Target: Census size >2500 to reach Ne = 500**
    
    #### 3. **Combined Wild Populations** (Ne = 520)
    
    ✅ **If connected** - Good genetic health:
    - Maintain connectivity!
    - Prevent further barriers
    - This demonstrates value of gene flow
    - **Lesson: Dam removal would improve Ne substantially**
    
    #### 4. **Conservation Strategy:**
    
    **Option A: Remove/Modify Dam** (Best)
    - Restore connectivity
    - Ne increases from 180 → 520
    - Natural gene flow
    
    **Option B: Managed Translocation** (Compromise)
    - Move 20-50 fish upstream ↔ downstream annually
    - Simulates natural migration
    - Prevents divergence
    
    **Option C: Genetic Monitoring** (Minimum)
    - Sample every 5 years
    - Track Ne trends
    - Early warning system
    """)
    
    st.markdown("---")
    
    # Decision framework
    st.markdown("### 🎯 Conservation Decision Framework")
    
    decision_code = """
    ```
    STEP 1: Estimate Ne (use genetic data)
    │
    ├─ Ne < 50?
    │  └─ 🚨 IMMEDIATE ACTION
    │     ├─ Genetic rescue (translocation)
    │     ├─ Captive breeding
    │     └─ Habitat restoration
    │
    ├─ Ne 50-500?
    │  └─ ⚠️ MONITOR & PLAN
    │     ├─ Maintain/increase N
    │     ├─ Regular genetic monitoring
    │     └─ Prepare for intervention
    │
    └─ Ne > 500?
       └─ ✅ CONTINUE CURRENT MANAGEMENT
          ├─ Periodic monitoring
          ├─ Protect habitat
          └─ Prevent fragmentation
    
    STEP 2: Calculate required census size
    N_required = Ne_target / (Ne/N ratio)
    
    STEP 3: Implement management
    - Habitat protection
    - Connectivity maintenance
    - Population augmentation if needed
    
    STEP 4: Monitor effectiveness
    - Re-estimate Ne every 5-10 years
    - Adjust management as needed
    ```
    """
    
    st.code(decision_code, language='text')

# ============================================================================
# TAB 5: SUMMARY
# ============================================================================
with tab5:
    st.markdown('<h2 class="section-header">🎯 Summary & Key Takeaways</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What We Learned
    
    Congratulations! You've mastered **Effective Population Size**!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Core Concepts
        
        1. **The Concept**
           - Ne = size of ideal population with same drift rate
           - Almost always Ne < N (often Ne = 0.1-0.3 N)
           - Multiple factors reduce Ne multiplicatively
        
        2. **The Five Factors**
           - Unequal sex ratio
           - Variance in offspring number
           - Non-random mating
           - Overlapping generations
           - Population fluctuations (harmonic mean!)
        
        3. **Estimation Methods**
           - Linkage disequilibrium (current Ne)
           - Temporal (historical Ne)
           - Heterozygosity excess (recent bottleneck)
        
        4. **The 50/500 Rule**
           - Ne = 50: Short-term minimum (avoid inbreeding)
           - Ne = 500: Long-term target (evolutionary potential)
           - Below 50 = crisis
           - 50-500 = vulnerable
           - Above 500 = healthy
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Skills Acquired
        
        1. **Analytical Skills**
           - Calculate Ne from breeding structure
           - Estimate Ne from genetic data
           - Interpret Ne/N ratios
           - Apply 50/500 rule
        
        2. **Conservation Applications**
           - Assess population viability
           - Design translocation programs
           - Set population targets
           - Monitor genetic health
        
        3. **Critical Thinking**
           - Don't trust census size alone
           - Consider breeding structure
           - Account for bottlenecks
           - Plan for long-term
        """)
    
    st.markdown("---")
    
    # Quick reference
    st.markdown("## 📊 Quick Reference Guide")
    
    quick_ref = {
        'Ne Value': ['< 50', '50 - 100', '100 - 500', '500 - 1000', '> 1000'],
        'Status': ['🚨 Critical', '⚠️ High Risk', '⚠️ Vulnerable', '✅ Adequate', '✅ Healthy'],
        'Short-term (1-10 gen)': [
            'Inbreeding depression',
            'Some inbreeding risk',
            'Low inbreeding risk',
            'No inbreeding concern',
            'Excellent'
        ],
        'Long-term (100+ gen)': [
            'Cannot persist',
            'Cannot adapt',
            'Limited adaptation',
            'Can adapt',
            'Full evolutionary potential'
        ],
        'Action Required': [
            'Immediate rescue',
            'Active management',
            'Monitor & plan',
            'Maintain current',
            'Protect habitat'
        ]
    }
    
    df_quick = pd.DataFrame(quick_ref)
    st.dataframe(df_quick, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Calculation summary
    st.markdown("## 🧮 Key Formulas")
    
    st.markdown("""
    ### Ne Calculations:
    
    **Sex ratio effect:**
    ```
    Ne = (4 × Nm × Nf) / (Nm + Nf)
    ```
    
    **Variance in offspring:**
    ```
    Ne ≈ N / (1 + Vk/k̄)
    ```
    
    **Harmonic mean (fluctuations):**
    ```
    Ne = t / (1/N1 + 1/N2 + ... + 1/Nt)
    ```
    
    ### Estimation from Data:
    
    **LD method:**
    ```
    Ne ≈ 1 / (3 × r̂²)
    where r̂² = mean LD corrected for sample size
    ```
    
    **Temporal method:**
    ```
    Ne ≈ t / (2 × ΔF)
    where t = generations, ΔF = standardized variance in allele freq
    ```
    
    ### Required Census Size:
    ```
    N_required = Ne_target / (Ne/N ratio)
    
    Example: For Ne = 500 with Ne/N = 0.2:
    N = 500 / 0.2 = 2500 individuals needed!
    ```
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🎓 Pattern Hunters Principles
    
    1. ✅ **"The shape constrains the outcome"**
       - Breeding structure → Ne/N ratio
       - Can't escape this mathematical constraint
       - Must work within these limits
    
    2. ✅ **"Count what matters, not what's easy"**
       - Census size is easy to count
       - Effective size is what matters genetically
       - Extra effort = better decisions
    
    3. ✅ **"Past events cast long shadows"**
       - Harmonic mean effect
       - Single bottleneck affects Ne for generations
       - History matters!
    
    4. ✅ **"Local examples, universal principles"**
       - Labeo rohita in Mahanadi
       - Same Ne principles as any species
       - 50/500 rule applies everywhere
    """)
    
    st.success("""
    ### 🎊 Congratulations!
    
    You've completed **ALL THREE Module 5 topics**!
    
    **Module 5A:** FST & Population Structure  
    **Module 5B:** Selection Signatures  
    **Module 5C:** Effective Population Size  
    
    You can now:
    - ✅ Measure population differentiation
    - ✅ Detect natural selection
    - ✅ Assess population viability
    - ✅ Make evidence-based conservation decisions
    - ✅ Design genetic monitoring programs
    - ✅ Manage endangered populations
    
    **This is APPLIED conservation genetics!**
    
    You have the tools to:
    - Save species from extinction
    - Design breeding programs
    - Manage fish hatcheries
    - Advise wildlife managers
    - Conduct impactful research
    
    **Congratulations on completing the Population Genomics series!** 🎓🧬🐟
    """)
    
    st.markdown("---")
    
    # Feedback
    st.markdown("### 📝 Feedback & Contact")
    
    with st.expander("💬 Share your thoughts"):
        st.markdown("""
        What did you think of Module 5C?
        
        - Was the Ne concept clear?
        - Will you use this in conservation work?
        - Which examples were most helpful?
        - How can we improve?
        
        **Contact:** susama.kar@kuchindacollege.ac.in
        
        **GitHub:** https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Module 5C: Effective Population Size - The Genetic Bottleneck</strong></p>
    <p>Developed by Susama Kar & Dr. Alok Patel</p>
    <p>Department of Zoology, Kuchinda College, Sambalpur University</p>
    <p>Part of the Pattern Hunters Educational Series</p>
    <p>License: CC BY 4.0 | <a href="https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive">GitHub</a> | DOI: 10.5281/zenodo.17887470</p>
</div>
""", unsafe_allow_html=True)
