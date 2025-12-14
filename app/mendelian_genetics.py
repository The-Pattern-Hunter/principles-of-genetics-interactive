"""
Mendelian Genetics Interactive Explorer
========================================

A comprehensive Streamlit app covering:
- Part 1: Monohybrid crosses and 3:1 ratio
- Part 2: Probability foundations and dihybrid crosses
- Part 3: Chi-square test and gene interactions

Authors: Susama Kar & Dr. Alok Patel
Institution: Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.stats import binom, chi2
import pandas as pd
from collections import Counter

# Page configuration
st.set_page_config(
    page_title="Mendelian Genetics Explorer",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E7D32;
        text-align: center;
        padding: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #1976D2;
        padding: 0.5rem;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1976D2;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #2E7D32;
    }
    .warning-box {
        background-color: #FFF3E0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #F57C00;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🧬 Navigation")
st.sidebar.markdown("### Pattern Hunters Series")

module = st.sidebar.radio(
    "Select Module:",
    ["🏠 Home",
     "Part 1: Monohybrid Cross",
     "Part 2: Probability & Dihybrid",
     "Part 3: Chi-Square & Interactions"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**About Pattern Hunters**

Philosophy: Observe → Discover → Understand → Formalize

You'll SEE the patterns BEFORE learning the formulas!
""")

###################
# HOME PAGE
###################

if module == "🏠 Home":
    st.markdown('<h1 class="main-header">🧬 Mendelian Genetics Interactive Explorer</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    ## Welcome to Pattern Hunters Biology!
    
    ### 🎯 Our Core Philosophy
    
    **"In biology, uncertainty has predictable shapes through probability distributions"**
    
    Instead of memorizing Mendel's ratios, you'll **DISCOVER** them by:
    1. **Observing** patterns through simulation
    2. **Asking** "Why this ratio and not another?"
    3. **Understanding** the probability foundation
    4. **Formalizing** with mathematics
    
    ### Why This Approach Works:
    
    - ✅ You understand WHY 3:1 (not just WHAT is 3:1)
    - ✅ You recognize the binomial distribution at play
    - ✅ You can predict new situations (not just memorize)
    - ✅ Knowledge lasts beyond the exam!
    
    ---
    
    This interactive app covers complete Mendelian genetics for BSc 5th Semester Zoology students.
    
    ### 📚 What You'll Learn:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>Part 1: Monohybrid Cross</h3>
        <ul>
        <li>3:1 ratio discovery</li>
        <li>Punnett squares</li>
        <li>Law of Segregation</li>
        <li>Binomial distribution</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h3>Part 2: Probability & Dihybrid</h3>
        <ul>
        <li>Product and sum rules</li>
        <li>Probability trees</li>
        <li>9:3:3:1 ratio</li>
        <li>Independent assortment</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-box">
        <h3>Part 3: Chi-Square & Interactions</h3>
        <ul>
        <li>Statistical validation</li>
        <li>Incomplete dominance</li>
        <li>Codominance</li>
        <li>Epistasis types</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.success("👈 **Select a module from the sidebar to begin your discovery journey!**")
    
    st.markdown("""
    ### 🌾 Regional Focus: Odisha Examples
    
    Throughout the modules, you'll see examples from:
    - Rice plant breeding (traditional Odisha varieties)
    - Labeo rohita (Mahanadi River fish)
    - Indigenous cattle breeds
    - Local crop genetics
    
    ### 👥 Developed By:
    - **Susama Kar** - Lecturer in Zoology
    - **Dr. Alok Patel** - Head, Department of Zoology
    
    **Institution:** Kuchinda College, Sambalpur University, Odisha, India
    """)

###################
# PART 1: MONOHYBRID CROSS
###################

elif module == "Part 1: Monohybrid Cross":
    st.markdown('<h1 class="main-header">Part 1: Monohybrid Cross</h1>', unsafe_allow_html=True)
    
    # Pattern Hunters Philosophy Box
    st.markdown("""
    <div class="info-box">
    <h3>🎯 Pattern Hunters Philosophy</h3>
    <p><strong>Core Insight:</strong> "In biology, uncertainty has predictable shapes through probability distributions"</p>
    <p><strong>Your Mission:</strong> DON'T memorize "Mendel's 3:1 ratio" - instead, DISCOVER why it's 3:1 and not 2:1 or 4:1!</p>
    <p><strong>Approach:</strong> Observe data → Recognize the pattern → Understand the mechanism → Formalize with math</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("""
    ## 🔍 The Discovery Challenge
    
    **Scenario:** You're breeding rice plants in Odisha.
    - Cross two heterozygous tall plants: **Tt × Tt**
    - What offspring ratio emerges?
    
    **⚠️ IMPORTANT:** Run the simulation FIRST, observe the pattern, THEN read the explanation below!
    """)
    
    st.markdown("---")
    st.markdown('<h2 class="sub-header">🎯 Interactive Simulator</h2>', unsafe_allow_html=True)
    
    # Controls
    col1, col2 = st.columns([1, 2])
    
    with col1:
        sample_size = st.slider("Number of Offspring:", 10, 1000, 100, 10)
        show_punnett = st.checkbox("Show Punnett Square", value=True)
        show_expected = st.checkbox("Show Expected 3:1 Line", value=True)
        
        if st.button("🎲 Run Simulation", type="primary"):
            st.session_state.run_mono = True
    
    if 'run_mono' in st.session_state or sample_size:
        # Simulate
        np.random.seed(42)
        offspring = []
        for _ in range(sample_size):
            allele1 = np.random.choice(['T', 't'])
            allele2 = np.random.choice(['T', 't'])
            genotype = ''.join(sorted([allele1, allele2], reverse=True))
            offspring.append(genotype)
        
        # Count
        tall = sum(1 for g in offspring if 'T' in g)
        short = sample_size - tall
        ratio = tall / short if short > 0 else tall
        
        # Visualize
        if show_punnett:
            fig, axes = plt.subplots(1, 3, figsize=(16, 5))
        else:
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))
            axes = [None] + list(axes)
        
        # Punnett square
        if show_punnett:
            ax = axes[0]
            ax.set_xlim(0, 4)
            ax.set_ylim(0, 4)
            ax.axis('off')
            
            # Grid
            for i in range(3):
                ax.plot([1, 3], [3-i, 3-i], 'k-', linewidth=2)
                ax.plot([1+i, 1+i], [1, 3], 'k-', linewidth=2)
            
            # Headers
            ax.add_patch(Rectangle((1, 3), 2, 0.7, facecolor='lightblue', edgecolor='black', linewidth=2))
            ax.add_patch(Rectangle((0.3, 1), 0.7, 2, facecolor='lightblue', edgecolor='black', linewidth=2))
            ax.text(2, 3.35, 'Tt ♂', ha='center', fontsize=16, fontweight='bold')
            ax.text(0.65, 2, 'Tt\n♀', ha='center', fontsize=16, fontweight='bold')
            
            # Gametes
            for i, g in enumerate(['T', 't']):
                ax.text(1.5 + i, 3.35, g, fontsize=14, fontweight='bold')
                ax.text(0.65, 2.5 - i, g, fontsize=14, fontweight='bold')
            
            # Cells
            cells_data = [['TT', 'Tt'], ['Tt', 'tt']]
            for i in range(2):
                for j in range(2):
                    color = 'lightgreen' if 'T' in cells_data[i][j] else 'lightcoral'
                    ax.add_patch(Rectangle((1+j, 2-i), 1, 1, 
                                          facecolor=color, edgecolor='black', linewidth=2, alpha=0.6))
                    ax.text(1.5+j, 2.5-i, cells_data[i][j], ha='center', fontsize=16, fontweight='bold')
            
            ax.set_title('Punnett Square: Tt × Tt', fontsize=14, fontweight='bold', pad=10)
        
        # Bar chart
        ax_idx = 1 if show_punnett else 0
        ax = axes[ax_idx]
        
        categories = ['Tall\n(T_)', 'Short\n(tt)']
        counts = [tall, short]
        colors = ['lightgreen', 'lightcoral']
        
        bars = ax.bar(categories, counts, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
        
        if show_expected:
            expected = [sample_size * 0.75, sample_size * 0.25]
            ax.plot([0, 1], expected, 'r--', linewidth=3, marker='o', markersize=10, label='Expected 3:1')
        
        ax.set_ylabel('Count', fontsize=13, fontweight='bold')
        ax.set_title(f'Phenotype Distribution (n={sample_size})', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        if show_expected:
            ax.legend(fontsize=11)
        
        for bar, val in zip(bars, counts):
            ax.text(bar.get_x() + bar.get_width()/2., val + max(counts)*0.02,
                   f'{val}\n({val/sample_size*100:.1f}%)', ha='center', fontweight='bold')
        
        # Pie chart
        ax_idx2 = 2 if show_punnett else 1
        ax2 = axes[ax_idx2]
        
        ax2.pie(counts, labels=categories, autopct='%1.1f%%',
                colors=colors, explode=(0.05, 0.05), startangle=90,
                textprops={'fontweight': 'bold', 'fontsize': 11})
        ax2.set_title(f'Ratio: {ratio:.2f}:1\n(Expected: 3:1)', fontsize=13, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Results
        st.markdown("---")
        st.markdown('<h3 class="sub-header">📊 Results</h3>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Sample Size", f"{sample_size}")
        with col2:
            st.metric("Tall Plants", f"{tall} ({tall/sample_size*100:.1f}%)")
        with col3:
            st.metric("Short Plants", f"{short} ({short/sample_size*100:.1f}%)")
        with col4:
            st.metric("Observed Ratio", f"{ratio:.2f}:1")
        
        if abs(ratio - 3) < 0.3:
            st.success("✅ Excellent match to expected 3:1 ratio!")
        elif abs(ratio - 3) < 0.7:
            st.info("✓ Good match to expected 3:1 ratio")
        else:
            st.warning("⚠️ Try increasing sample size for better ratio convergence")
    
    # Explanation
    st.markdown("---")
    st.markdown('<h2 class="sub-header">🔬 Pattern Hunters: Why 3:1 Specifically?</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🤔 The Big Question
    
    You observed approximately **3:1 ratio**. But WHY this specific ratio? Why not 2:1 or 4:1?
    
    **This is where Pattern Hunters thinking begins!** 🎯
    """)
    
    with st.expander("🎲 REASON 1: The Probability Foundation (Click to discover!)"):
        st.markdown("""
        ### Independent Coin Flips in Disguise!
        
        **Key Insight:** Each gamete is like a coin flip!
        
        #### The Mechanism:
        
        **1. Gamete Formation (Meiosis)**
        - Tt parent produces gametes
        - **Probability = 0.5** for T allele (like heads)
        - **Probability = 0.5** for t allele (like tails)
        
        **2. Random Fertilization = Two Independent Flips**
        
        | Sperm (flip 1) | Egg (flip 2) | Offspring | Probability | Phenotype |
        |----------------|--------------|-----------|-------------|-----------|
        | T (0.5) | T (0.5) | TT | 0.5 × 0.5 = **0.25** | Tall |
        | T (0.5) | t (0.5) | Tt | 0.5 × 0.5 = **0.25** | Tall |
        | t (0.5) | T (0.5) | Tt | 0.5 × 0.5 = **0.25** | Tall |
        | t (0.5) | t (0.5) | tt | 0.5 × 0.5 = **0.25** | Short |
        
        **3. Sum the Probabilities (SUM RULE)**
        - P(Tall) = P(TT) + P(Tt) + P(tT) = 0.25 + 0.25 + 0.25 = **0.75**
        - P(Short) = P(tt) = **0.25**
        
        **4. Calculate the Ratio**
        - Ratio = 0.75 / 0.25 = **3:1** ✓
        
        ### 💡 Pattern Discovery:
        **The 3:1 ratio comes from the BINOMIAL DISTRIBUTION with p = 0.5!**
        
        It's NOT arbitrary - it's mathematical!
        """)
    
    with st.expander("📊 REASON 2: The Binomial Distribution Shape (Click to see the math!)"):
        st.markdown("""
        ### The Shape of Uncertainty
        
        **Core Pattern Hunters Insight:** "Uncertainty has predictable shapes through probability distributions"
        
        #### The Mathematics:
        
        For **n offspring**, each with **probability p = 0.75** of being tall:
        
        $$P(k \\text{ tall}) = \\binom{n}{k} (0.75)^k (0.25)^{n-k}$$
        
        **This is the BINOMIAL DISTRIBUTION!**
        
        #### Why 0.75 specifically?
        
        Because dominance means:
        - TT → Tall ✓
        - Tt → Tall ✓  (this is KEY!)
        - tt → Short
        
        So 3 out of 4 genotypes produce tall phenotype = 0.75
        
        #### Why NOT Other Ratios?
        
        - **2:1?** Would require p = 0.67 → Not possible with 0.5 gamete probabilities
        - **4:1?** Would require p = 0.80 → Not possible with Mendelian segregation
        - **1:1?** Would require p = 0.50 → Only happens in TEST CROSS (Tt × tt)
        
        **The 3:1 ratio is INEVITABLE given:**
        1. Equal gamete probabilities (0.5 each)
        2. Complete dominance
        3. Random fertilization
        
        ### 🎯 This is why Pattern Hunters emphasizes:
        **"See the DISTRIBUTION before memorizing the RATIO"**
        """)
    
    with st.expander("🧬 REASON 3: The Biological Mechanism (Click for complete picture!)"):
        st.markdown("""
        ### From Biology to Mathematics
        
        **Step 1: Meiosis (Cell Division)**
        - Homologous chromosomes separate
        - Each gamete gets ONE allele
        - Physical mechanism → Equal probabilities
        
        **Step 2: Random Fertilization**
        - Sperm meets egg randomly
        - No preference for T or t
        - Random process → Binomial distribution
        
        **Step 3: Dominance**
        - One functional copy is enough
        - T allele produces functional protein
        - Result: TT and Tt both tall
        
        **Step 4: The Math Emerges**
        - Biology → Probabilities
        - Probabilities → Distribution
        - Distribution → Predictable ratio
        
        ### 🌟 Pattern Hunters Principle:
        
        **"The ratio is not a rule to memorize - it's a CONSEQUENCE of the mechanism!"**
        
        When you understand:
        - Equal segregation (meiosis)
        - Random fertilization
        - Complete dominance
        
        The 3:1 ratio is **inevitable**, not arbitrary!
        """)
    
    with st.expander("📖 Traditional vs Pattern Hunters Approach"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="warning-box">
            <h4>❌ Traditional Teaching</h4>
            <ol>
            <li>Memorize: "Mendel's 3:1 ratio"</li>
            <li>Learn the Punnett square</li>
            <li>Apply to problems</li>
            <li>Forget after exam</li>
            </ol>
            <p><strong>Problem:</strong> Students don't know WHY it's 3:1!</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Pattern Hunters Way</h4>
            <ol>
            <li>Simulate crosses → See pattern emerge</li>
            <li>Ask "Why 3:1 and not 2:1?"</li>
            <li>Discover probability foundation</li>
            <li>Understand binomial distribution</li>
            <li>Formalize as Mendel's Law</li>
            </ol>
            <p><strong>Result:</strong> Deep understanding that lasts!</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    with st.expander("📝 Quick Reference: Step-by-Step Mechanism"):
        st.markdown("""
        ### Summary of the Mechanism
        
        **1. Gamete Formation (Meiosis)**
        - Tt parent produces gametes
        - 50% carry T allele
        - 50% carry t allele
        
        **2. Random Fertilization**
        - T sperm × T egg → TT (tall)
        - T sperm × t egg → Tt (tall)
        - t sperm × T egg → Tt (tall)
        - t sperm × t egg → tt (short)
        
        **3. Probabilities**
        - P(TT) = 0.5 × 0.5 = 0.25 (25%)
        - P(Tt) = 2 × 0.5 × 0.5 = 0.50 (50%)
        - P(tt) = 0.5 × 0.5 = 0.25 (25%)
        
        **4. Phenotypic Ratio**
        - Tall (TT + Tt) = 75%
        - Short (tt) = 25%
        - **Ratio = 3:1** ✓
        
        ### This is Mendel's Law of Segregation!
        
        **Law:** Paired alleles separate during gamete formation and randomly reunite at fertilization.
        
        **Mathematical basis:** Binomial distribution with p = 0.75
        """)
    
    st.markdown("---")
    
    with st.expander("🌾 Odisha Example: Rice Plant Breeding"):
        st.markdown("""
        ### Traditional Rice Variety Breeding
        
        **Scenario:**
        - T = Tall stems (dominant) - preferred for traditional farming
        - t = Dwarf stems (recessive) - better for modern intensive farming
        
        **Breeding Program:**
        - Cross: Tt × Tt
        - Expect: 3 tall : 1 dwarf
        
        **Agricultural Application:**
        - Farmers can predict offspring ratios
        - Plan field space accordingly
        - Select desired phenotypes efficiently
        
        **Real Impact:** This knowledge helps Odisha farmers maintain traditional varieties while improving yield!
        """)

###################
# PART 2: PROBABILITY & DIHYBRID
###################

elif module == "Part 2: Probability & Dihybrid":
    st.markdown('<h1 class="main-header">Part 2: Probability & Dihybrid Cross</h1>', 
                unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🎲 Probability Explorer", "📊 Dihybrid Cross"])
    
    # TAB 1: Probability
    with tab1:
        st.markdown("""
        ## Understanding Probability in Genetics
        
        Two fundamental rules:
        
        ### 1. Product Rule (AND)
        Probability of independent events occurring together:
        
        **P(A AND B) = P(A) × P(B)**
        
        ### 2. Sum Rule (OR)
        Probability of mutually exclusive events:
        
        **P(A OR B) = P(A) + P(B)**
        """)
        
        st.markdown("---")
        st.markdown('<h3 class="sub-header">🎯 Interactive Probability Calculator</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            p_A = st.slider("P(Dominant allele):", 0.1, 0.9, 0.5, 0.05)
            show_tree = st.checkbox("Show probability tree", value=True)
            show_calc = st.checkbox("Show calculations", value=True)
        
        p_a = 1 - p_A
        
        # Calculate
        p_AA = p_A * p_A
        p_Aa = 2 * p_A * p_a
        p_aa = p_a * p_a
        
        # Visualize
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Tree (simplified for Streamlit)
        if show_tree:
            ax = axes[0]
            ax.text(0.5, 0.9, 'Probability Tree Diagram', ha='center', fontsize=14, fontweight='bold',
                   transform=ax.transAxes)
            ax.text(0.5, 0.7, f'P(A) = {p_A:.2f}', ha='center', fontsize=12, transform=ax.transAxes)
            ax.text(0.5, 0.6, f'P(a) = {p_a:.2f}', ha='center', fontsize=12, transform=ax.transAxes)
            ax.text(0.5, 0.4, f'P(AA) = {p_A:.2f} × {p_A:.2f} = {p_AA:.3f}', 
                   ha='center', fontsize=11, transform=ax.transAxes)
            ax.text(0.5, 0.3, f'P(Aa) = 2 × {p_A:.2f} × {p_a:.2f} = {p_Aa:.3f}', 
                   ha='center', fontsize=11, transform=ax.transAxes)
            ax.text(0.5, 0.2, f'P(aa) = {p_a:.2f} × {p_a:.2f} = {p_aa:.3f}', 
                   ha='center', fontsize=11, transform=ax.transAxes)
            ax.axis('off')
        else:
            axes[0].text(0.5, 0.5, 'Enable tree to see visualization', 
                        ha='center', va='center', transform=axes[0].transAxes)
            axes[0].axis('off')
        
        # Bar chart
        ax2 = axes[1]
        genotypes = ['AA', 'Aa', 'aa']
        probs = [p_AA, p_Aa, p_aa]
        colors = ['green', 'orange', 'red']
        
        bars = ax2.bar(genotypes, probs, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
        ax2.set_ylabel('Probability', fontsize=13, fontweight='bold')
        ax2.set_title('Genotype Probabilities', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.set_ylim(0, max(probs) * 1.2)
        
        for bar, prob in zip(bars, probs):
            ax2.text(bar.get_x() + bar.get_width()/2., prob + 0.02,
                    f'{prob:.3f}\n({prob*100:.1f}%)', ha='center', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        if show_calc:
            st.markdown("---")
            st.markdown("### 📝 Detailed Calculations")
            
            st.code(f"""
Allele frequencies:
   P(A) = {p_A:.3f}
   P(a) = {p_a:.3f}

PRODUCT RULE:
   P(AA) = P(A) × P(A) = {p_A:.3f} × {p_A:.3f} = {p_AA:.4f}
   P(Aa) = 2 × P(A) × P(a) = 2 × {p_A:.3f} × {p_a:.3f} = {p_Aa:.4f}
   P(aa) = P(a) × P(a) = {p_a:.3f} × {p_a:.3f} = {p_aa:.4f}

Check (should equal 1.0): {p_AA + p_Aa + p_aa:.4f} ✓

SUM RULE:
   P(Dominant phenotype) = P(AA) + P(Aa) = {p_AA + p_Aa:.4f}
   P(Recessive phenotype) = P(aa) = {p_aa:.4f}
            """)
    
    # TAB 2: Dihybrid
    with tab2:
        st.markdown("""
        ## Dihybrid Cross - Two Genes!
        
        **Scenario:** Two genes segregating simultaneously
        - Gene 1: Seed shape (R = round, r = wrinkled)
        - Gene 2: Seed color (Y = yellow, y = green)
        
        **Cross:** RrYy × RrYy
        
        **Question:** What ratio emerges?
        """)
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            n_dihy = st.slider("Number of Offspring:", 16, 1600, 160, 16)
            show_exp_dihy = st.checkbox("Show expected 9:3:3:1", value=True, key="dihy_exp")
            
            if st.button("🎲 Run Dihybrid Cross", type="primary"):
                st.session_state.run_dihy = True
        
        if 'run_dihy' in st.session_state or n_dihy:
            # Simulate
            phenotypes = []
            for _ in range(n_dihy):
                r_alleles = np.random.choice(['R', 'r'], size=2)
                gene1 = 'R_' if 'R' in r_alleles else 'rr'
                
                y_alleles = np.random.choice(['Y', 'y'], size=2)
                gene2 = 'Y_' if 'Y' in y_alleles else 'yy'
                
                phenotypes.append(gene1 + gene2)
            
            # Count
            counts = Counter(phenotypes)
            order = ['R_Y_', 'R_yy', 'rrY_', 'rryy']
            observed = [counts.get(p, 0) for p in order]
            expected = [n_dihy * r for r in [9/16, 3/16, 3/16, 1/16]]
            
            # Plot
            fig, ax = plt.subplots(figsize=(12, 6))
            
            labels = ['Round\nYellow', 'Round\nGreen', 'Wrinkled\nYellow', 'Wrinkled\nGreen']
            colors = ['lightgreen', 'lightyellow', 'lightcoral', 'lightgray']
            
            x = np.arange(len(labels))
            width = 0.35
            
            ax.bar(x - width/2, observed, width, label='Observed', 
                   color=colors, alpha=0.8, edgecolor='black', linewidth=2)
            
            if show_exp_dihy:
                ax.bar(x + width/2, expected, width, label='Expected 9:3:3:1', 
                       color='steelblue', alpha=0.5, edgecolor='black', linewidth=2)
            
            ax.set_ylabel('Count', fontsize=13, fontweight='bold')
            ax.set_title(f'Dihybrid Cross (n={n_dihy})', fontsize=14, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(labels, fontsize=11)
            ax.legend(fontsize=11)
            ax.grid(True, alpha=0.3, axis='y')
            
            for i, val in enumerate(observed):
                ax.text(i - width/2, val + max(observed)*0.02, f'{val}', 
                       ha='center', fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Summary
            st.markdown("---")
            
            if observed[3] > 0:
                ratio = [round(obs / observed[3], 1) for obs in observed]
            else:
                ratio = [0, 0, 0, 0]
            
            st.markdown(f"""
            ### 📊 Results
            
            **Observed ratio:** {ratio[0]}:{ratio[1]}:{ratio[2]}:{ratio[3]}  
            **Expected ratio:** 9:3:3:1
            """)
            
            st.markdown("""
            ---
            
            ### 🎯 Pattern Hunters Question: Why 9:3:3:1?
            
            **Not 8:4:2:2 or 10:3:2:1?** Why THIS specific pattern?
            """)
            
            with st.expander("🔍 Click to discover WHY 9:3:3:1 is inevitable!"):
                st.markdown("""
                ### The Pattern Behind the Pattern
                
                **Key Insight:** TWO independent 3:1 crosses happening simultaneously!
                
                #### The Mathematics:
                
                **Gene 1 (R/r):** 3 Round : 1 wrinkled = (3:1)  
                **Gene 2 (Y/y):** 3 Yellow : 1 green = (3:1)
                
                **Multiply them together (PRODUCT RULE):**
                
                | Gene 1 | × | Gene 2 | = | Combined | Calculation | Ratio |
                |--------|---|--------|---|----------|-------------|-------|
                | 3 Round | × | 3 Yellow | = | 9 Round Yellow | 3×3 | 9/16 |
                | 3 Round | × | 1 green | = | 3 Round green | 3×1 | 3/16 |
                | 1 wrinkled | × | 3 Yellow | = | 3 wrinkled Yellow | 1×3 | 3/16 |
                | 1 wrinkled | × | 1 green | = | 1 wrinkled green | 1×1 | 1/16 |
                
                **Total: 9:3:3:1** ✓
                
                ### Why NOT Other Ratios?
                
                - **12:3:1?** Would need different gene interaction (epistasis)
                - **15:1?** Would need complementary genes
                - **1:1:1:1?** Would need testcross (RrYy × rryy)
                
                **The 9:3:3:1 is INEVITABLE when:**
                1. Two genes segregate independently
                2. Both show complete dominance
                3. No gene interaction (epistasis)
                
                ### 🌟 Pattern Hunters Principle:
                
                **(3:1) × (3:1) = 9:3:3:1**
                
                It's NOT a separate law to memorize - it's the **PRODUCT** of two monohybrid ratios!
                
                ### 📈 The Distribution View:
                
                Each offspring has:
                - P(Round) = 0.75, P(Yellow) = 0.75
                - P(Round AND Yellow) = 0.75 × 0.75 = **0.5625** (9/16)
                
                This is the **BINOMIAL DISTRIBUTION** applied to TWO traits independently!
                """)
            
            st.markdown("💡 **This is Mendel's Law of Independent Assortment in action!**")
        
        with st.expander("🌾 Odisha Example: Rice Grain Traits"):
            st.markdown("""
            ### Traditional Rice Variety
            
            **Two traits:**
            - Grain length: L = long (dominant), l = short
            - Aroma: A = aromatic (dominant), a = non-aromatic
            
            **Cross:** LlAa × LlAa
            
            **Expected:**
            - 9 long, aromatic (premium variety)
            - 3 long, non-aromatic
            - 3 short, aromatic
            - 1 short, non-aromatic
            
            **Value:** Farmers can predict which combination will appear and plan accordingly!
            """)

###################
# PART 3: CHI-SQUARE & INTERACTIONS
###################

elif module == "Part 3: Chi-Square & Interactions":
    st.markdown('<h1 class="main-header">Part 3: Chi-Square & Gene Interactions</h1>', 
                unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🎯 Chi-Square Test", "🔄 Gene Interactions"])
    
    # TAB 1: Chi-Square
    with tab1:
        st.markdown("""
        ## Chi-Square Goodness of Fit Test
        
        **Question:** Is your observed data close enough to the expected ratio?
        
        ### Formula:
        
        $$\\chi^2 = \\sum \\frac{(O - E)^2}{E}$$
        
        Where:
        - O = Observed count
        - E = Expected count
        """)
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            obs_dom = st.slider("Observed Dominant:", 50, 150, 95)
            obs_rec = st.slider("Observed Recessive:", 10, 50, 25)
            alpha = st.selectbox("Significance level (α):", [0.05, 0.01])
            
            if st.button("🧮 Calculate Chi-Square", type="primary"):
                st.session_state.run_chi = True
        
        if 'run_chi' in st.session_state or obs_dom:
            total = obs_dom + obs_rec
            
            # Expected for 3:1
            exp_dom = total * 0.75
            exp_rec = total * 0.25
            
            observed = [obs_dom, obs_rec]
            expected = [exp_dom, exp_rec]
            
            # Calculate chi-square
            chi_sq = sum((o - e)**2 / e for o, e in zip(observed, expected))
            
            # Critical value (df=1)
            critical = chi2.ppf(1 - alpha, 1)
            p_value = 1 - chi2.cdf(chi_sq, 1)
            reject = chi_sq > critical
            
            # Visualize
            fig, axes = plt.subplots(1, 3, figsize=(16, 5))
            
            # Bar chart
            ax = axes[0]
            x = [0, 1]
            width = 0.35
            
            ax.bar([i-width/2 for i in x], observed, width, label='Observed', 
                   color='steelblue', alpha=0.8, edgecolor='black', linewidth=2)
            ax.bar([i+width/2 for i in x], expected, width, label='Expected', 
                   color='coral', alpha=0.8, edgecolor='black', linewidth=2)
            
            ax.set_ylabel('Count', fontsize=13, fontweight='bold')
            ax.set_title('Observed vs Expected', fontsize=14, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(['Dominant', 'Recessive'])
            ax.legend()
            ax.grid(True, alpha=0.3, axis='y')
            
            # Chi-square distribution
            ax2 = axes[1]
            x_range = np.linspace(0, max(critical*2, chi_sq*1.5), 200)
            y_range = chi2.pdf(x_range, 1)
            
            ax2.plot(x_range, y_range, 'b-', linewidth=2, label='χ² dist (df=1)')
            ax2.fill_between(x_range[x_range >= critical], 0, 
                             chi2.pdf(x_range[x_range >= critical], 1),
                             color='red', alpha=0.3, label=f'Reject region (α={alpha})')
            
            ax2.axvline(chi_sq, color='green', linewidth=3, linestyle='--', 
                       label=f'χ² = {chi_sq:.3f}')
            ax2.axvline(critical, color='red', linewidth=2, linestyle=':', 
                       label=f'Critical = {critical:.3f}')
            
            ax2.set_xlabel('χ²', fontsize=12, fontweight='bold')
            ax2.set_title('Chi-Square Distribution', fontsize=14, fontweight='bold')
            ax2.legend(fontsize=9)
            ax2.grid(True, alpha=0.3)
            
            # Decision box
            ax3 = axes[2]
            ax3.axis('off')
            
            decision_text = f"""Chi-Square Test

χ² = {chi_sq:.3f}
Critical = {critical:.3f}
p-value = {p_value:.4f}

Decision: {'REJECT' if reject else 'ACCEPT'} H₀

{"Data does NOT fit 3:1" if reject else "Data fits 3:1 ratio"}
"""
            
            color = 'red' if reject else 'green'
            ax3.text(0.5, 0.5, decision_text, ha='center', va='center', 
                    transform=ax3.transAxes, fontsize=12, fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor=color, alpha=0.3, linewidth=3),
                    family='monospace')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Summary
            st.markdown("---")
            
            if reject:
                st.error(f"""
                ### ❌ REJECT the hypothesis
                
                - χ² = {chi_sq:.4f} > Critical value = {critical:.4f}
                - p-value = {p_value:.4f} < α = {alpha}
                - Data does NOT fit 3:1 ratio
                
                **Possible reasons:**
                - Non-Mendelian inheritance
                - Lethal alleles
                - Sampling error
                - Experimental error
                """)
            else:
                st.success(f"""
                ### ✅ ACCEPT the hypothesis
                
                - χ² = {chi_sq:.4f} ≤ Critical value = {critical:.4f}
                - p-value = {p_value:.4f} ≥ α = {alpha}
                - Data fits 3:1 ratio
                - Consistent with Mendelian inheritance
                """)
    
    # TAB 2: Gene Interactions
    with tab2:
        st.markdown("""
        ## Gene Interactions - Beyond Simple Dominance
        
        Not all genes follow 3:1 or 9:3:3:1 ratios!
        
        ### Types:
        1. **Incomplete Dominance** - Heterozygote shows intermediate phenotype (1:2:1)
        2. **Codominance** - Both alleles fully expressed (1:2:1)
        3. **Epistasis** - One gene masks another (modified ratios)
        """)
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            interaction_type = st.selectbox(
                "Select Interaction Type:",
                ['Complete Dominance (3:1)',
                 'Incomplete Dominance (1:2:1)',
                 'Epistasis 9:3:4']
            )
            
            n_inter = st.slider("Sample Size:", 100, 1000, 400, 100, key="inter_n")
            
            if st.button("🧬 Simulate", type="primary"):
                st.session_state.run_inter = True
        
        if 'run_inter' in st.session_state or n_inter:
            # Define based on type
            if 'Complete' in interaction_type:
                phenotypes = ['Dominant', 'Recessive']
                props = [0.75, 0.25]
                colors = ['purple', 'white']
                info = """**Complete Dominance:**
AA and Aa → dominant
aa → recessive
3:1 ratio"""
            
            elif 'Incomplete' in interaction_type:
                phenotypes = ['Red', 'Pink', 'White']
                props = [0.25, 0.50, 0.25]
                colors = ['red', 'pink', 'white']
                info = """**Incomplete Dominance:**
RR = red
Rr = pink (intermediate)
rr = white
1:2:1 ratio"""
            
            else:  # Epistasis
                phenotypes = ['Black', 'Brown', 'Yellow']
                props = [9/16, 3/16, 4/16]
                colors = ['black', 'brown', 'yellow']
                info = """**Recessive Epistasis (9:3:4):**
E_B_ = black (9/16)
E_bb = brown (3/16)
ee__ = yellow (4/16)
Example: Labrador coat color"""
            
            # Simulate
            observed = np.random.multinomial(n_inter, props)
            expected = [n_inter * p for p in props]
            
            # Plot
            fig, axes = plt.subplots(1, 2, figsize=(14, 6))
            
            ax = axes[0]
            x = np.arange(len(phenotypes))
            width = 0.35
            
            ax.bar(x - width/2, observed, width, label='Observed', 
                   color=colors, alpha=0.7, edgecolor='black', linewidth=2)
            ax.bar(x + width/2, expected, width, label='Expected', 
                   color='gray', alpha=0.5, edgecolor='black', linewidth=2)
            
            ax.set_ylabel('Count', fontsize=13, fontweight='bold')
            ax.set_title(f'{interaction_type}\n(n={n_inter})', fontsize=14, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(phenotypes, fontsize=11)
            ax.legend()
            ax.grid(True, alpha=0.3, axis='y')
            
            for i, val in enumerate(observed):
                ax.text(i - width/2, val + max(observed)*0.02, f'{val}', 
                       ha='center', fontweight='bold')
            
            # Info box
            ax2 = axes[1]
            ax2.axis('off')
            ax2.text(0.1, 0.5, info, transform=ax2.transAxes, 
                    fontsize=12, verticalalignment='center',
                    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                    family='monospace')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            st.markdown(f"""
            ---
            ### 📊 Results
            
            **Expected ratio:** {':'.join([str(int(p*16)) for p in props])}
            
            💡 **Key Insight:** Different interactions → Different ratios!
            """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p><strong>Developed by:</strong> Susama Kar & Dr. Alok Patel</p>
    <p><strong>Institution:</strong> Kuchinda College, Sambalpur University, Odisha</p>
    <p><strong>Philosophy:</strong> Pattern Hunters - "Uncertainty has predictable shapes"</p>
    <p><strong>License:</strong> CC BY 4.0</p>
</div>
""", unsafe_allow_html=True)
