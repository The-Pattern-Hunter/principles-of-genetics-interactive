"""
Module 4: From Mendelian to Population Genetics
COMPLETE ENHANCED VERSION - The Conceptual Bridge

When Individual Outcomes Become Population Patterns

Authors: Susama Kar & Dr. Alok Patel
Institution: Department of Zoology, Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Page configuration
st.set_page_config(
    page_title="Module 4: Mendelian to Population",
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
    .bridge-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: 1rem 0;
    }
    .aha-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        margin: 1rem 0;
    }
    .transition-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        margin: 1rem 0;
    }
    .null-model-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        color: #1e3a8a;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🧬 From Mendelian to Population Genetics</h1>', unsafe_allow_html=True)

st.markdown("""
**The Conceptual Bridge - When Individual Outcomes Become Population Patterns**

**Authors:** Susama Kar & Dr. Alok Patel  
**Institution:** Department of Zoology, Kuchinda College, Sambalpur University

---
""")

# THE BRIDGE - Enhanced Pattern Hunters
st.markdown("""
<div class="bridge-box">
<h3>🌉 The Pattern Hunters Journey: Crossing the Conceptual Bridge</h3>

<h4>The Fundamental Question:</h4>
<p><strong>"How does Mendelian genetics (individuals, pedigrees, ratios) relate to population genetics (frequencies, HWE, evolution)?"</strong></p>

<h4>The Gap Students Face:</h4>
<ul>
<li>📚 <strong>BSc Semester 3:</strong> Mendel's laws, 3:1 ratios, pedigrees</li>
<li>❓ <strong>??? Confusion ???</strong></li>
<li>📚 <strong>MSc Semester 1:</strong> p² + 2pq + q², FST, selection</li>
</ul>

<h4>The Pattern Hunters Bridge:</h4>
<ol>
<li><strong>OBSERVE:</strong> Individual crosses give ratios (3:1, 1:2:1)</li>
<li><strong>SCALE UP:</strong> Many crosses → frequencies emerge</li>
<li><strong>DISCOVER:</strong> Ratios ARE frequencies when n is large!</li>
<li><strong>UNDERSTAND:</strong> Same biology, different perspective</li>
<li><strong>CONNECT:</strong> HWE is the "null model" (like neutral theory!)</li>
</ol>

<h4>Core Insight:</h4>
<p><strong>"Statistics emerges from repetition"</strong> - One cross = ratio. Many crosses = frequency. Population genetics IS Mendelian genetics at scale!</p>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Introduction",
    "🎲 Part 1: Ratios → Frequencies",
    "🧮 Part 2: Hardy-Weinberg",
    "🔗 Part 3: Connections",
    "🎯 Summary"
])

# Tab 1: Introduction
with tab1:
    st.markdown('<h2 class="section-header">The Conceptual Gap</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## The Problem
        
        Students learn two genetics courses but don't see the connection:
        
        ### 📚 Mendelian Genetics (BSc)
        - Punnett squares, 3:1 ratios
        - Individual families
        - **Focus:** What happens in THIS cross?
        
        ### 📚 Population Genetics (MSc)
        - Hardy-Weinberg, p² + 2pq + q²
        - Entire populations
        - **Focus:** What happens in THIS population?
        
        ## The Answer
        
        **They're the SAME thing at different scales!**
        
        When n → ∞:
        - Ratios → Frequencies
        - Punnett square → Hardy-Weinberg
        - Individual → Population
        """)
    
    with col2:
        st.info("""
        ### 📊 Module Stats
        - Duration: 60-90 min
        - Level: BSc/MSc bridge
        - Importance: ⭐⭐⭐⭐⭐
        """)
        
        st.markdown("""
        <div class="aha-box">
        <h4>💡 "Aha!" Moment</h4>
        <p><strong>p² + 2pq + q²</strong></p>
        <p>is just</p>
        <p><strong>1:2:1 ratio</strong></p>
        <p>as frequencies! 🤯</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visual
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    np.random.seed(42)
    
    sample_sizes = [1, 4, 20, 100, 500, 10000]
    
    for idx, (ax, n) in enumerate(zip(axes.flat, sample_sizes)):
        offspring = np.random.choice(['AA', 'Aa', 'aa'], size=n, p=[0.25, 0.5, 0.25])
        counts = Counter(offspring)
        
        genotypes = ['AA', 'Aa', 'aa']
        obs_counts = [counts.get(g, 0) for g in genotypes]
        exp_counts = [n*0.25, n*0.5, n*0.25]
        
        x = np.arange(3)
        width = 0.35
        
        ax.bar(x - width/2, obs_counts, width, label='Observed',
               color='#ef4444', alpha=0.7, edgecolor='black')
        ax.bar(x + width/2, exp_counts, width, label='Expected',
               color='#3b82f6', alpha=0.7, edgecolor='black')
        
        ax.set_title(f'n = {n}', fontsize=10, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(genotypes)
        ax.legend(fontsize=7)
        ax.grid(alpha=0.3, axis='y')
    
    plt.suptitle('Emergence of 1:2:1 Ratio', fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Tab 2: Ratios to Frequencies  
with tab2:
    st.markdown('<h2 class="section-header">🎲 Part 1: Ratios → Frequencies</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="transition-box">
    <h3>Pattern Hunters Question:</h3>
    <p><strong>"When does a RATIO become a FREQUENCY?"</strong></p>
    <p><strong>Answer:</strong> When you have enough samples!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 Interactive: Watch Ratios Become Frequencies!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        n_crosses = st.slider("Number of crosses", 1, 1000, 1)
        
        parent1 = st.selectbox("Parent 1", ['AA', 'Aa', 'aa'], index=1)
        parent2 = st.selectbox("Parent 2", ['AA', 'Aa', 'aa'], index=1)
        
        show_exp = st.checkbox("Show expected", value=True)
        
        run_sim = st.button("🎲 Run!", type="primary")
        
        # Calculate expectations
        def get_probs(p1, p2):
            alleles1 = list(p1)
            alleles2 = list(p2)
            offspring = []
            for a1 in alleles1:
                for a2 in alleles2:
                    offspring.append(''.join(sorted([a1, a2], reverse=True)))
            counts = Counter(offspring)
            total = len(offspring)
            
            # Get probabilities, ensuring all genotypes are included
            probs = {}
            for g in ['AA', 'Aa', 'aa']:
                probs[g] = counts.get(g, 0) / total
            
            # Normalize to ensure sum = 1.0 exactly (fix floating point errors)
            prob_sum = sum(probs.values())
            if prob_sum > 0:
                probs = {g: p/prob_sum for g, p in probs.items()}
            
            return probs
        
        exp_probs = get_probs(parent1, parent2)
        
        st.info(f"**Expected:**\nAA={exp_probs['AA']:.2f}\nAa={exp_probs['Aa']:.2f}\naa={exp_probs['aa']:.2f}")
    
    with col2:
        if run_sim or n_crosses == 1:
            np.random.seed(None)
            probs = [exp_probs['AA'], exp_probs['Aa'], exp_probs['aa']]
            offspring = np.random.choice(['AA', 'Aa', 'aa'], n_crosses, p=probs)
            counts = Counter(offspring)
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
            
            genotypes = ['AA', 'Aa', 'aa']
            obs_counts = [counts.get(g, 0) for g in genotypes]
            obs_freqs = [c/n_crosses for c in obs_counts]
            exp_counts = [n_crosses * exp_probs[g] for g in genotypes]
            exp_freqs = [exp_probs[g] for g in genotypes]
            
            x = np.arange(3)
            width = 0.35
            
            # Counts
            ax1.bar(x - width/2, obs_counts, width, label='Observed',
                   color='#ef4444', alpha=0.7, edgecolor='black', linewidth=2)
            if show_exp:
                ax1.bar(x + width/2, exp_counts, width, label='Expected',
                       color='#3b82f6', alpha=0.7, edgecolor='black', linewidth=2)
            ax1.set_title(f'Counts (n={n_crosses})', fontweight='bold')
            ax1.set_xticks(x)
            ax1.set_xticklabels(genotypes)
            ax1.legend()
            ax1.grid(alpha=0.3, axis='y')
            
            # Frequencies
            ax2.bar(x - width/2, obs_freqs, width, label='Observed',
                   color='#10b981', alpha=0.7, edgecolor='black', linewidth=2)
            if show_exp:
                ax2.bar(x + width/2, exp_freqs, width, label='Expected',
                       color='#f59e0b', alpha=0.7, edgecolor='black', linewidth=2)
            ax2.set_title('Frequencies', fontweight='bold')
            ax2.set_xticks(x)
            ax2.set_xticklabels(genotypes)
            ax2.set_ylim(0, 1)
            ax2.legend()
            ax2.grid(alpha=0.3, axis='y')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
            
            if n_crosses == 1:
                st.warning(f"**n=1:** Pure chance! Got {offspring[0]}")
            elif n_crosses < 100:
                st.info(f"**n={n_crosses}:** Pattern emerging!")
            else:
                st.success(f"**n={n_crosses}:** Frequencies converged! This is population genetics!")

# Tab 3: Hardy-Weinberg
with tab3:
    st.markdown('<h2 class="section-header">🧮 Part 2: Hardy-Weinberg Equilibrium</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="null-model-box">
    <h3>🎯 Pattern Hunters Revelation: HWE is a NULL MODEL!</h3>
    <p>Just like:</p>
    <ul>
    <li><strong>Module 1:</strong> Poisson = null model for crossovers</li>
    <li><strong>Module 5B:</strong> Neutral theory = null model for evolution</li>
    </ul>
    <p><strong>Module 4:</strong> HWE = null model for population genetics!</p>
    <p><strong>Meaning:</strong> If nothing is happening (no selection, drift, migration, mutation), this is what you expect!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## What HWE Actually Means
    
    ### ❌ What Students Think:
    "Some complicated formula I have to memorize"
    
    ### ✅ What It Really Is:
    "The Punnett square written as frequencies!"
    
    ## The Derivation (Simple Version)
    
    **Given:**
    - Allele A has frequency p
    - Allele a has frequency q
    - p + q = 1
    
    **Random mating** = picking alleles randomly
    
    ### Genotype Frequencies:
    
    ```
    P(AA) = p × p = p²
    P(Aa) = 2 × p × q = 2pq  (can get A from mom, a from dad OR vice versa)
    P(aa) = q × q = q²
    
    Sum: p² + 2pq + q² = (p + q)² = 1²  = 1 ✓
    ```
    
    **That's it!** It's just the binomial expansion!
    
    ## The Five Assumptions
    
    HWE holds when:
    1. **No mutation** - allele frequencies don't change by mutation
    2. **No migration** - no gene flow from other populations
    3. **No selection** - all genotypes equally fit
    4. **No drift** - infinite population size
    5. **Random mating** - no inbreeding or assortative mating
    
    **Reality:** These are NEVER all true!
    
    **So why use HWE?**
    
    Because deviations tell us what's happening! (Just like Poisson in Module 1, Neutral theory in Module 5B)
    """)
    
    st.markdown("---")
    
    # Widget 2: HWE Explorer
    st.markdown("### 🎮 Interactive 2: Hardy-Weinberg Population")
    
    st.info("**EDUCATIONAL SIMULATION - Build a population in HWE!**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        p_freq = st.slider(
            "Allele A frequency (p)",
            min_value=0.0,
            max_value=1.0,
            value=0.6,
            step=0.01
        )
        
        q_freq = 1 - p_freq
        
        pop_size = st.slider(
            "Population size (N)",
            min_value=50,
            max_value=10000,
            value=1000,
            step=50
        )
        
        show_punnett = st.checkbox("Show population Punnett square", value=True)
        
        run_pop = st.button("👥 Generate Population!", type="primary")
        
        # HWE expectations
        exp_AA = p_freq ** 2
        exp_Aa = 2 * p_freq * q_freq
        exp_aa = q_freq ** 2
        
        st.code(f"""
Allele Frequencies:
p(A) = {p_freq:.3f}
q(a) = {q_freq:.3f}

HWE Predictions:
AA = p² = {exp_AA:.3f}
Aa = 2pq = {exp_Aa:.3f}
aa = q² = {exp_aa:.3f}

Sum = {exp_AA + exp_Aa + exp_aa:.3f}
        """)
    
    with col2:
        if run_pop or pop_size >= 50:
            # Generate population
            np.random.seed(None)
            
            # Each individual gets 2 alleles randomly
            alleles = np.random.choice(['A', 'a'], size=(pop_size, 2),
                                      p=[p_freq, q_freq])
            
            # Determine genotypes
            genotypes = []
            for ind in alleles:
                geno = ''.join(sorted(ind, reverse=True))
                genotypes.append(geno)
            
            counts = Counter(genotypes)
            
            # Observed frequencies
            obs_AA = counts.get('AA', 0) / pop_size
            obs_Aa = counts.get('Aa', 0) / pop_size
            obs_aa = counts.get('aa', 0) / pop_size
            
            # Plot
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
            
            # Plot 1: Counts
            genotypes_list = ['AA', 'Aa', 'aa']
            obs_counts = [counts.get(g, 0) for g in genotypes_list]
            exp_counts = [pop_size * exp_AA, pop_size * exp_Aa, pop_size * exp_aa]
            
            x = np.arange(3)
            width = 0.35
            
            bars1 = ax1.bar(x - width/2, obs_counts, width, label='Observed',
                           color='#10b981', alpha=0.7, edgecolor='black', linewidth=2)
            bars2 = ax1.bar(x + width/2, exp_counts, width, label='HWE Expected',
                           color='#f59e0b', alpha=0.7, edgecolor='black', linewidth=2)
            
            ax1.set_ylabel('Count', fontsize=12, fontweight='bold')
            ax1.set_title(f'Population Genotypes (N={pop_size})', fontsize=13, fontweight='bold')
            ax1.set_xticks(x)
            ax1.set_xticklabels(genotypes_list)
            ax1.legend(fontsize=10)
            ax1.grid(alpha=0.3, axis='y')
            
            # Plot 2: Frequencies
            obs_freqs = [obs_AA, obs_Aa, obs_aa]
            exp_freqs = [exp_AA, exp_Aa, exp_aa]
            
            bars3 = ax2.bar(x - width/2, obs_freqs, width, label='Observed',
                           color='#3b82f6', alpha=0.7, edgecolor='black', linewidth=2)
            bars4 = ax2.bar(x + width/2, exp_freqs, width, label='HWE Expected',
                           color='#ef4444', alpha=0.7, edgecolor='black', linewidth=2)
            
            ax2.set_ylabel('Frequency', fontsize=12, fontweight='bold')
            ax2.set_title('Genotype Frequencies', fontsize=13, fontweight='bold')
            ax2.set_xticks(x)
            ax2.set_xticklabels(genotypes_list)
            ax2.set_ylim(0, 1.0)
            ax2.legend(fontsize=10)
            ax2.grid(alpha=0.3, axis='y')
            
            # Add value labels
            for bar, val in zip(bars3, obs_freqs):
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'{val:.3f}', ha='center', va='bottom', 
                        fontsize=10, fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
            
            # Chi-square test
            chi_sq = sum([(o - e)**2 / e for o, e in zip(obs_counts, exp_counts)])
            
            if pop_size < 200:
                st.warning(f"""
                ### 📊 Small Population (N={pop_size})
                
                **Chi-square:** {chi_sq:.2f}
                
                Notice variation from HWE. This is **genetic drift** in action!
                
                Small populations deviate from HWE by chance alone.
                """)
            else:
                st.success(f"""
                ### ✅ Large Population (N={pop_size})
                
                **Observed:** AA={obs_AA:.3f}, Aa={obs_Aa:.3f}, aa={obs_aa:.3f}
                **Expected:** AA={exp_AA:.3f}, Aa={exp_Aa:.3f}, aa={exp_aa:.3f}
                
                **Chi-square:** {chi_sq:.2f}
                
                Excellent match to HWE! This is what random mating looks like.
                """)
        
        # Punnett square
        if show_punnett:
            st.markdown("---")
            st.markdown("### 📊 Population Punnett Square:")
            
            st.markdown(f"""
            ```
            Think of this as sampling from a gene pool:
            
            Sperm/Pollen:  A (p={p_freq:.2f})    a (q={q_freq:.2f})
                        +----------------+----------------+
            Eggs:   A   |   AA (p²)      |   Aa (pq)      |
            (p={p_freq:.2f}) |   {exp_AA:.3f}        |   {p_freq*q_freq:.3f}        |
                        +----------------+----------------+
                    a   |   Aa (pq)      |   aa (q²)      |
            (q={q_freq:.2f}) |   {p_freq*q_freq:.3f}        |   {exp_aa:.3f}        |
                        +----------------+----------------+
            
            Sum of Aa cells = 2 × {p_freq*q_freq:.3f} = {exp_Aa:.3f}
            ```
            
            **This IS the same Punnett square from Mendelian genetics!**
            
            Just applied to an entire population instead of one cross!
            """)
    
    # Experiments
    st.markdown("---")
    st.markdown("### 🧪 Experiments to Try:")
    
    with st.expander("🔬 Click to see suggested experiments"):
        st.markdown("""
        1. **Effect of Population Size:**
           - N=50: Notice drift (deviation from HWE)
           - N=1000: Much better match
           - N=10000: Nearly perfect
           - **Lesson:** HWE requires large N!
        
        2. **Different Allele Frequencies:**
           - p=0.5: Maximum heterozygosity (Aa = 0.5)
           - p=0.9: Mostly AA, few aa (Aa = 0.18)
           - p=0.1: Mostly aa, few AA (Aa = 0.18)
           - **Lesson:** p=0.5 gives most genetic diversity
        
        3. **Verify the Math:**
           - Set p=0.6, q=0.4
           - Calculate: p² = 0.36, 2pq = 0.48, q² = 0.16
           - Sum = 1.00 ✓
           - Check if population matches
        
        4. **Connect to Mendel:**
           - Set p=0.5 (like Aa × Aa)
           - Expected: 0.25, 0.50, 0.25
           - **This is 1:2:1 ratio!**
        """)

# Tab 4: Connections
with tab4:
    st.markdown('<h2 class="section-header">🔗 Part 3: Connecting Everything</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The Complete Picture
    
    Now you understand how ALL the modules connect!
    """)
    
    # Connection diagram
    st.markdown("### 🎯 The Module Connection Map:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Mendelian Foundation:
        
        **Module 1: Genetic Mapping**
        - Crossovers follow Poisson
        - Individual crosses
        - Gene mapping
        
        **Module 2: Interference**
        - Reality modifies Poisson
        - COC < 1
        - Real chromosome mechanics
        
        **Module 4 (THIS): Bridge**
        - Ratios → Frequencies
        - Individual → Population
        - **HWE = null model**
        """)
    
    with col2:
        st.markdown("""
        ### Population Genomics:
        
        **Module 5A: FST**
        - Population structure
        - Differentiation
        - HWE within populations
        
        **Module 5B: Selection**
        - Deviations from neutral
        - Tajima's D
        - **Neutral theory = null model**
        
        **Module 5C: Effective Size**
        - Ne determines drift
        - Affects HWE
        - Conservation applications
        """)
    
    st.markdown("---")
    
    # The null model pattern
    st.markdown("""
    <div class="null-model-box">
    <h3>🎓 Pattern Hunters Meta-Pattern: The Null Model Strategy</h3>
    
    <p>Notice the recurring pattern across modules:</p>
    
    <table style="width:100%; background:white; color:#1e3a8a;">
    <tr>
        <th>Module</th>
        <th>Null Model</th>
        <th>What It Assumes</th>
        <th>Deviations Reveal</th>
    </tr>
    <tr>
        <td><strong>Module 1</strong></td>
        <td>Poisson</td>
        <td>Independent crossovers</td>
        <td>Interference (Module 2)</td>
    </tr>
    <tr>
        <td><strong>Module 4</strong></td>
        <td>Hardy-Weinberg</td>
        <td>No evolution happening</td>
        <td>Selection, drift, etc.</td>
    </tr>
    <tr>
        <td><strong>Module 5B</strong></td>
        <td>Neutral Theory</td>
        <td>No selection</td>
        <td>Adaptive evolution</td>
    </tr>
    </table>
    
    <p><strong>The Strategy:</strong> Start with simple null model → Measure deviations → Learn about reality!</p>
    <p><strong>This is how science works!</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Real example connecting all modules
    st.markdown("### 🐟 Complete Example: Labeo rohita Population Study")
    
    st.markdown("""
    Let's see how ALL modules apply to one real research project:
    
    #### Research Question: 
    "Is the Labeo rohita population in Mahanadi River genetically healthy?"
    
    #### Module-by-Module Analysis:
    
    **Module 1 & 2: Genetic Mapping**
    - Map QTL for growth, disease resistance
    - Understand linkage (interference present, COC ~ 0.4)
    - Design breeding programs
    
    **Module 4: HWE Check**
    - Sample 100 fish, genotype at microsatellite locus
    - Test if in HWE:
      - Observed: AA=36, Aa=48, aa=16
      - Expected (p=0.6): AA=36, Aa=48, aa=16
      - ✅ In HWE! (random mating, no selection at this locus)
    
    **Module 5A: Population Structure**
    - Compare upstream vs downstream (separated by dam)
    - Calculate FST = 0.08 (moderate differentiation)
    - Recommendation: Maintain gene flow (fish ladder?)
    
    **Module 5B: Selection Signatures**
    - Test for selection at temperature tolerance locus
    - Tajima's D = -1.8 (recent selection!)
    - Interpretation: Adapting to warmer water (climate change?)
    
    **Module 5C: Effective Size**
    - Census size N = 8000 fish
    - Estimated Ne = 420 (from LD method)
    - Ne/N = 0.05 (typical for fish)
    - Status: Above 50, but below 500 threshold
    - Recommendation: Maintain habitat, prevent further fragmentation
    
    #### Complete Assessment:
    
    ✅ **Genetic diversity:** Adequate (HWE at most loci)  
    ⚠️ **Population structure:** Moderate (FST = 0.08)  
    ✅ **Adaptive potential:** Present (selection detected)  
    ⚠️ **Long-term viability:** Concern (Ne < 500)  
    
    **Management recommendation:**
    - Short-term: Monitor, maintain connectivity
    - Long-term: Increase habitat quality to boost Ne
    - Research: Continue monitoring selection at climate loci
    
    **See how all modules work together?**
    """)

# Tab 5: Summary
with tab5:
    st.markdown('<h2 class="section-header">🎯 Summary & Key Takeaways</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Congratulations! You've Crossed the Bridge! 🌉
    
    You now understand the connection between Mendelian and Population Genetics!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ What You've Learned:
        
        1. **The Transition**
           - Ratios (small n) → Frequencies (large n)
           - Same biology, different scale
           - Statistics emerges from repetition
        
        2. **Hardy-Weinberg**
           - p² + 2pq + q² = 1
           - Just binomial expansion
           - **Null model** for population genetics
        
        3. **The Connection**
           - Punnett square = HWE
           - 1:2:1 ratio = p², 2pq, q²
           - Individual genetics = Population genetics
        
        4. **The Pattern**
           - Null models reveal reality
           - Deviations are informative
           - Same strategy across modules
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Pattern Hunters Principles:
        
        1. **"Statistics emerges from repetition"**
           - One cross = random
           - Many crosses = pattern
        
        2. **"Same biology, different lens"**
           - Mendelian: individuals
           - Population: frequencies
           - **Both valid!**
        
        3. **"Null models are powerful"**
           - HWE like Poisson, Neutral theory
           - Deviations teach us
           - Framework for understanding
        
        4. **"Scale matters"**
           - n=1: Mendelian thinking
           - n=∞: Population thinking
           - Transition is continuous
        """)
    
    st.markdown("---")
    
    # Quick reference
    st.markdown("## 📊 Quick Reference Guide:")
    
    ref_data = {
        'Concept': [
            'Punnett Square',
            'Mendelian Ratio',
            'HWE Equation',
            'Allele Frequency',
            'Genotype Frequency'
        ],
        'Mendelian View': [
            'Predicts offspring',
            '1:2:1, 3:1, etc.',
            'Not used',
            'Not emphasized',
            'Counts of offspring'
        ],
        'Population View': [
            'Models random mating',
            'Same as frequencies!',
            'p² + 2pq + q² = 1',
            'p, q (core concept)',
            'Proportions in population'
        ],
        'Connection': [
            'SAME TOOL!',
            'Ratio = Frequency (large n)',
            'Binomial expansion',
            'Emerges from many crosses',
            'Frequency = ratio/n'
        ]
    }
    
    df_ref = pd.DataFrame(ref_data)
    st.dataframe(df_ref, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # The big picture
    st.markdown("""
    ## 🎓 The Complete Genetics Course:
    
    You now understand:
    
    **Foundation (Modules 1-2):**
    - Crossovers, linkage, mapping
    - Interference and reality
    
    **Bridge (Module 4 - THIS):**
    - Individual → Population transition
    - HWE as null model
    
    **Population Genomics (Modules 5A-5C):**
    - Structure, selection, viability
    - All build on HWE!
    
    **You're ready for:**
    - Advanced population genetics
    - Conservation genetics
    - Evolutionary genomics
    - Research in any organism!
    """)
    
    st.success("""
    ### 🎊 The Bridge is Crossed!
    
    **You can now:**
    - ✅ Connect Mendelian to Population genetics
    - ✅ Understand what HWE really means
    - ✅ See ratios as frequencies
    - ✅ Apply null model thinking
    - ✅ Integrate all 6 modules
    - ✅ Read population genetics papers
    - ✅ Design genetic studies
    - ✅ Teach this connection to others
    
    **This conceptual understanding is MORE valuable than memorizing formulas!**
    """)
    
    st.markdown("---")
    
    # Feedback
    with st.expander("📝 Share your thoughts"):
        st.markdown("""
        Did this module help?
        
        - Did you have an "aha!" moment?
        - Was the bridge concept clear?
        - Which visualization helped most?
        - Will you think differently about HWE now?
        
        **Contact:** susama.kar@kuchindacollege.ac.in
        
        **GitHub:** https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Module 4: From Mendelian to Population Genetics</strong></p>
    <p>The Conceptual Bridge</p>
    <p>Developed by Susama Kar & Dr. Alok Patel</p>
    <p>Department of Zoology, Kuchinda College, Sambalpur University</p>
    <p>Part of the Pattern Hunters Educational Series</p>
    <p>License: CC BY 4.0 | <a href="https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive">GitHub</a></p>
</div>
""", unsafe_allow_html=True)