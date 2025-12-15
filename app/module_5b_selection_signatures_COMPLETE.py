"""
Module 5B: Selection Signatures - Detecting Adaptive Evolution
COMPLETE STREAMLIT VERSION - Enhanced Interactive Experience

An Interactive Journey from Neutral Expectation to Selection Detection

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
    page_title="Module 5B: Selection Signatures",
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
    .pattern-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        margin: 1rem 0;
    }
    .neutral-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        margin: 1rem 0;
    }
    .selection-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: #1e3a8a;
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
st.markdown('<h1 class="main-header">🧬 Module 5B: Selection Signatures</h1>', unsafe_allow_html=True)

st.markdown("""
**Detecting Adaptive Evolution - An Interactive Journey from Neutral Expectation to Selection Detection**

**Authors:** Susama Kar & Dr. Alok Patel  
**Institution:** Department of Zoology, Kuchinda College, Sambalpur University

---
""")

# Pattern Hunters approach box
st.markdown("""
<div class="pattern-box">
<h3>🔍 The Pattern Hunters Approach</h3>
<p><strong>Traditional approach:</strong> "D = (π - θ) / √Var" → Memorize formula</p>
<p><strong>Pattern Hunters approach:</strong></p>
<ol>
<li><strong>UNDERSTAND NEUTRAL:</strong> What does evolution look like WITHOUT selection?</li>
<li><strong>OBSERVE DEVIATION:</strong> How does selection change the pattern?</li>
<li><strong>QUANTIFY DIFFERENCE:</strong> Calculate Tajima's D and other statistics</li>
<li><strong>INTERPRET:</strong> What does this tell us about adaptation?</li>
</ol>
<p><strong>Key insight:</strong> Neutral theory isn't about "nothing happens" - it's our <strong>null hypothesis</strong> that makes selection detectable!</p>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Introduction",
    "⚛️ Part 1: Neutral Theory",
    "📊 Part 2: Site Frequency Spectrum",
    "📐 Part 3: Tajima's D",
    "🔬 Part 4: Multiple Methods",
    "🎯 Summary"
])

# ============================================================================
# TAB 1: INTRODUCTION
# ============================================================================
with tab1:
    st.markdown('<h2 class="section-header">Welcome to Selection Detection!</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## What You'll Learn
        
        This module teaches you **how to detect natural selection** in DNA sequences using:
        
        ### The Journey:
        
        1. ⚛️ **Neutral Theory** - Kimura's revolutionary null hypothesis
        2. 📊 **Site Frequency Spectrum** - The "shape" of genetic variation
        3. 📐 **Tajima's D** - A powerful selection detection statistic
        4. 🔬 **Multiple Methods** - FST outliers, iHS, XP-EHH, and more
        
        ## Why This Matters
        
        Selection detection helps us:
        - Identify genes under positive selection (adaptation)
        - Find disease resistance alleles
        - Understand human evolution (lactase, malaria)
        - Improve crops and livestock (breeding)
        - Detect balancing vs directional selection
        
        ## The Revolutionary Idea
        
        **Motoo Kimura (1968):** "Most mutations are neutral"
        
        This wasn't pessimistic - it was **brilliant**!
        - Neutral = our baseline expectation
        - Deviations from neutral = SELECTION!
        - Made selection mathematically detectable
        """)
    
    with col2:
        st.info("""
        ### 📊 Module Stats
        
        - **Duration:** 90-120 min
        - **Level:** MSc/Research
        - **Widgets:** 4 interactive
        - **Real Data:** 3 examples
        - **Prerequisites:** Module 5A helpful
        
        ### 🎓 Learning Levels
        
        - **BSc:** Neutral vs selection concepts
        - **MSc:** Calculate Tajima's D
        - **Research:** Multiple detection methods
        - **Advanced:** Interpret real genomic scans
        """)
    
    st.markdown("---")
    
    # Visual: Selection vs Neutral
    st.markdown("## 🎯 Selection vs Neutral - Visual Comparison")
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
    
    # Neutral
    x_neutral = np.linspace(0, 1, 100)
    y_neutral = 1/x_neutral[1:] * 0.1  # 1/frequency shape
    ax1.plot(x_neutral[1:], y_neutral, 'b-', linewidth=3)
    ax1.fill_between(x_neutral[1:], y_neutral, alpha=0.3, color='blue')
    ax1.set_title('Neutral Evolution\n(Tajima\'s D ≈ 0)', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Allele Frequency')
    ax1.set_ylabel('Number of Sites')
    ax1.text(0.5, max(y_neutral)*0.7, 'Many rare\nvariants', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Positive Selection (Sweep)
    x_sweep = np.linspace(0, 1, 100)
    y_sweep = np.exp(-((x_sweep - 0.8)**2) / 0.02) * 5
    ax2.bar(x_sweep, y_sweep, width=0.01, color='red', alpha=0.7)
    ax2.set_title('Positive Selection\n(Tajima\'s D < 0)', fontsize=13, fontweight='bold', color='red')
    ax2.set_xlabel('Allele Frequency')
    ax2.text(0.5, max(y_sweep)*0.7, 'Excess low &\nhigh frequency', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Balancing Selection
    x_balance = np.linspace(0, 1, 100)
    y_balance = np.exp(-((x_balance - 0.5)**2) / 0.02) * 8
    ax3.bar(x_balance, y_balance, width=0.01, color='green', alpha=0.7)
    ax3.set_title('Balancing Selection\n(Tajima\'s D > 0)', fontsize=13, fontweight='bold', color='green')
    ax3.set_xlabel('Allele Frequency')
    ax3.text(0.5, max(y_balance)*0.7, 'Excess\nintermediate', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.success("👆 **Start with Part 1: Neutral Theory** to understand the baseline!")

# ============================================================================
# TAB 2: PART 1 - NEUTRAL THEORY
# ============================================================================
with tab2:
    st.markdown('<h2 class="section-header">⚛️ Part 1: The Neutral Baseline - Kimura\'s Revolution</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The Question That Changed Population Genetics
    
    **1968:** Motoo Kimura asks a radical question:
    
    > "What if MOST genetic variation is **selectively neutral**?"
    
    ### The Neutral Theory of Molecular Evolution
    
    **Key claims:**
    1. Most mutations are either **deleterious** (removed) or **neutral** (drift)
    2. Advantageous mutations are **rare**
    3. Most polymorphism is neutral, maintained by drift
    4. Molecular evolution occurs mostly by **random fixation** of neutral alleles
    
    ### Why This Was Revolutionary
    
    Not because "selection doesn't matter" - but because it gave us:
    - A **null hypothesis** to test
    - Mathematical predictions to compare against
    - A way to DETECT selection by seeing deviations
    
    ### The Key Prediction
    
    If neutral theory is correct:
    - **Synonymous mutations** (don't change amino acid) should be common
    - **Nonsynonymous mutations** (change amino acid) should be rare (selected against)
    - Ratio dN/dS should be < 1
    """)
    
    st.markdown("---")
    
    # Widget 1: Synonymous vs Nonsynonymous
    st.markdown("### 🎮 Interactive 1: Observe Synonymous vs Nonsynonymous Variation")
    
    st.info("**EDUCATIONAL SIMULATION - Based on real genomic patterns**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Simulation Parameters:")
        
        generations_w1 = st.slider(
            "Generations",
            min_value=100,
            max_value=2000,
            value=1000,
            step=100,
            key='gen_w1'
        )
        
        pop_size_w1 = st.slider(
            "Population Size",
            min_value=50,
            max_value=500,
            value=100,
            step=50,
            key='pop_w1'
        )
        
        syn_rate = st.slider(
            "Synonymous mutation rate",
            min_value=0.0001,
            max_value=0.01,
            value=0.001,
            step=0.0001,
            format="%.4f",
            key='syn_rate'
        )
        
        nonsyn_rate = st.slider(
            "Nonsynonymous mutation rate",
            min_value=0.0001,
            max_value=0.01,
            value=0.001,
            step=0.0001,
            format="%.4f",
            key='nonsyn_rate'
        )
        
        selection_coef = st.slider(
            "Selection coefficient (s) against nonsyn",
            min_value=-0.05,
            max_value=0.0,
            value=-0.01,
            step=0.001,
            format="%.3f",
            help="Negative = deleterious"
        )
        
        st.info(f"""
        **Settings:**
        - Time: {generations_w1} generations
        - N = {pop_size_w1}
        - μ_syn = {syn_rate}
        - μ_nonsyn = {nonsyn_rate}
        - s = {selection_coef}
        """)
    
    with col2:
        # Simulate mutation accumulation
        np.random.seed(42)
        
        # Synonymous mutations (neutral)
        syn_mutations = []
        for gen in range(generations_w1):
            if np.random.random() < syn_rate:
                # New mutation appears
                freq = 1 / (2 * pop_size_w1)
                # Drift
                while freq > 0 and freq < 1:
                    freq += np.random.normal(0, np.sqrt(freq * (1-freq) / (2*pop_size_w1)))
                    freq = max(0, min(1, freq))
                    if freq > 0 and freq < 1:
                        break
                if freq > 0:
                    syn_mutations.append(freq)
        
        # Nonsynonymous mutations (selected against)
        nonsyn_mutations = []
        for gen in range(generations_w1):
            if np.random.random() < nonsyn_rate:
                freq = 1 / (2 * pop_size_w1)
                # Selection + drift
                while freq > 0 and freq < 1:
                    # Selection reduces frequency
                    freq_after_selection = freq * (1 + selection_coef) / (1 + freq * selection_coef)
                    # Then drift
                    freq_after_selection += np.random.normal(0, np.sqrt(freq_after_selection * (1-freq_after_selection) / (2*pop_size_w1)))
                    freq = max(0, min(1, freq_after_selection))
                    if freq > 0 and freq < 1:
                        break
                if freq > 0:
                    nonsyn_mutations.append(freq)
        
        # Plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
        
        # Histogram comparison
        bins = np.linspace(0, 1, 20)
        ax1.hist(syn_mutations, bins=bins, alpha=0.7, label='Synonymous (neutral)',
                color='blue', edgecolor='black')
        ax1.hist(nonsyn_mutations, bins=bins, alpha=0.7, label='Nonsynonymous (selected)',
                color='red', edgecolor='black')
        ax1.set_xlabel('Allele Frequency', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Number of Mutations', fontsize=12, fontweight='bold')
        ax1.set_title('Mutation Frequency Distribution', fontsize=13, fontweight='bold')
        ax1.legend(fontsize=10)
        ax1.grid(alpha=0.3)
        
        # Bar chart of counts
        counts = [len(syn_mutations), len(nonsyn_mutations)]
        colors_bar = ['blue', 'red']
        labels_bar = ['Synonymous', 'Nonsynonymous']
        
        bars = ax2.bar(labels_bar, counts, color=colors_bar, alpha=0.7, edgecolor='black', linewidth=2)
        ax2.set_ylabel('Total Number of Segregating Mutations', fontsize=12, fontweight='bold')
        ax2.set_title('Total Variation Comparison', fontsize=13, fontweight='bold')
        ax2.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{count}', ha='center', va='bottom', fontsize=13, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Results
    dN_dS_ratio = len(nonsyn_mutations) / max(len(syn_mutations), 1)
    
    st.markdown(f"""
    <div class="neutral-box">
    <h3>📊 Results - Neutral Theory Prediction:</h3>
    <p><strong>Synonymous mutations (neutral):</strong> {len(syn_mutations)}</p>
    <p><strong>Nonsynonymous mutations (selected):</strong> {len(nonsyn_mutations)}</p>
    <p><strong>dN/dS ratio:</strong> {dN_dS_ratio:.3f}</p>
    <h4>✅ Interpretation:</h4>
    <p>{"dN/dS < 1 confirms <strong>purifying selection</strong> against amino acid changes!" if dN_dS_ratio < 1 else "dN/dS ≥ 1 suggests <strong>positive selection</strong> or relaxed constraint!"}</p>
    <p><strong>Neutral Theory Prediction:</strong> Most nonsynonymous mutations are deleterious and removed by selection, while synonymous mutations drift freely.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Why this matters
    st.markdown("---")
    st.markdown("### 💡 Why This Matters: The Neutral Theory as Null Hypothesis")
    
    with st.expander("📖 Click to understand Kimura's genius"):
        st.markdown("""
        **Kimura's genius:** He gave us a **null hypothesis** for evolution!
        
        ### Without Neutral Theory:
        ❌ See variation → "Is this selection?" → ??? (no baseline to compare)
        
        ### With Neutral Theory:
        ✅ See variation → Compare to neutral expectation → Deviation = SELECTION!
        
        ### The Power of a Null Hypothesis
        
        1. **Neutral Theory predicts:**
           - dN/dS ≈ 1 if NO selection
           - dN/dS < 1 if purifying selection
           - dN/dS > 1 if positive selection
        
        2. **Site Frequency Spectrum:**
           - 1/i distribution under neutrality
           - Deviations indicate selection
        
        3. **Tajima's D:**
           - D ≈ 0 under neutrality
           - D < 0 → positive selection (sweep)
           - D > 0 → balancing selection
        
        ### Real Example: Lactase Persistence
        
        **Gene:** LCT (lactase)  
        **Neutral prediction:** dN/dS < 1 (most amino acid changes bad)  
        **Observation:** Regulatory region shows D < 0, high FST  
        **Conclusion:** POSITIVE SELECTION for lactose digestion in dairy farmers!
        
        This wouldn't be detectable without neutral baseline!
        """)

# ============================================================================
# TAB 3: PART 2 - SITE FREQUENCY SPECTRUM
# ============================================================================
with tab3:
    st.markdown('<h2 class="section-header">📊 Part 2: Site Frequency Spectrum - The Shape of Variation</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What Is the Site Frequency Spectrum (SFS)?
    
    **Simple definition:** A histogram showing how many mutations exist at each frequency in a population.
    
    ### Example:
    - You sequence 20 individuals (40 chromosomes)
    - Find a SNP present in 3 copies → frequency = 3/40 = 0.075
    - Count how many SNPs at each frequency (1/40, 2/40, 3/40, ...)
    - Plot histogram → That's the SFS!
    
    ### The Neutral Expectation
    
    Under neutrality, the SFS follows a **1/i distribution**:
    
    **E[ξᵢ] = θ/i**
    
    Where:
    - ξᵢ = number of mutations at frequency i
    - θ = 4Nμ (population mutation rate)
    - i = frequency class (1, 2, 3, ...)
    
    **Key insight:** Many rare variants, few common variants!
    
    ### How Selection Changes the SFS
    
    1. **Positive Selection (Selective Sweep):**
       - Excess of rare variants (new mutations after sweep)
       - Deficit of intermediate frequencies
       - Maybe one high-frequency variant (selected allele)
       - **Tajima's D < 0**
    
    2. **Balancing Selection:**
       - Excess of intermediate frequencies
       - Deficit of rare and common variants
       - **Tajima's D > 0**
    
    3. **Population Expansion:**
       - Excess of rare variants (like sweep)
       - All loci affected (not just selected gene)
       - **Tajima's D < 0 genome-wide**
    """)
    
    st.markdown("---")
    
    # Widget 2: SFS Explorer
    st.markdown("### 🎮 Interactive 2: Explore the Site Frequency Spectrum")
    
    st.info("**EDUCATIONAL SIMULATION**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Scenario Selection:")
        
        scenario = st.selectbox(
            "Choose evolutionary scenario",
            options=[
                'Neutral',
                'Positive Selection (Sweep)',
                'Balancing Selection',
                'Population Expansion',
                'Bottleneck'
            ],
            key='scenario_sfs'
        )
        
        sample_size = st.slider(
            "Sample size (individuals)",
            min_value=10,
            max_value=50,
            value=20,
            step=2
        )
        
        theta = st.slider(
            "θ (population mutation rate)",
            min_value=5.0,
            max_value=50.0,
            value=10.0,
            step=5.0
        )
        
        st.info(f"""
        **Settings:**
        - Scenario: {scenario}
        - Sample: {sample_size} individuals
        - θ = {theta}
        - Chromosomes: {2*sample_size}
        """)
        
        # Explanation box
        if scenario == 'Neutral':
            st.success("**Neutral:** Classic 1/i distribution - many rare, few common variants")
        elif scenario == 'Positive Selection (Sweep)':
            st.warning("**Sweep:** Excess rare variants + possible high-frequency selected allele")
        elif scenario == 'Balancing Selection':
            st.success("**Balancing:** Excess intermediate frequency variants")
        elif scenario == 'Population Expansion':
            st.info("**Expansion:** Like sweep but genome-wide - population grew recently")
        else:
            st.warning("**Bottleneck:** Loss of rare variants, excess intermediate")
    
    with col2:
        # Generate SFS based on scenario
        n_chromosomes = 2 * sample_size
        frequencies = np.arange(1, n_chromosomes)
        
        if scenario == 'Neutral':
            # Classic 1/i distribution
            sfs = theta / frequencies
            tajima_d = 0.0
            
        elif scenario == 'Positive Selection (Sweep)':
            # Excess rare + deficit intermediate + maybe one high
            sfs = theta / frequencies * 2  # More rare variants
            sfs[5:15] *= 0.3  # Deficit intermediate
            if len(sfs) > 30:
                sfs[30] += theta * 3  # High-frequency selected allele
            tajima_d = -1.5
            
        elif scenario == 'Balancing Selection':
            # Excess intermediate
            mid = len(frequencies) // 2
            sfs = theta / frequencies
            sfs[mid-5:mid+5] *= 3  # Excess intermediate
            sfs[:5] *= 0.5  # Fewer rare
            tajima_d = 2.0
            
        elif scenario == 'Population Expansion':
            # Recent expansion - excess rare
            sfs = theta / frequencies * 2.5
            sfs[10:] *= 0.5
            tajima_d = -1.8
            
        else:  # Bottleneck
            # Loss of rare variants
            sfs = theta / frequencies * 0.5
            sfs[:5] *= 0.2
            sfs[10:20] *= 2
            tajima_d = 0.8
        
        # Add noise
        np.random.seed(42)
        sfs = sfs + np.random.normal(0, sfs * 0.2)
        sfs = np.maximum(sfs, 0)
        
        # Plot SFS
        fig, ax = plt.subplots(figsize=(11, 6))
        
        # Bar plot
        colors_sfs = ['#3b82f6' if scenario == 'Neutral' else 
                     '#ef4444' if 'Selection' in scenario else '#10b981' for _ in frequencies]
        
        ax.bar(frequencies, sfs, color=colors_sfs, alpha=0.7, edgecolor='black', linewidth=1)
        
        # Add neutral expectation line if not neutral
        if scenario != 'Neutral':
            neutral_sfs = theta / frequencies
            ax.plot(frequencies, neutral_sfs, 'k--', linewidth=2.5, 
                   label='Neutral expectation (1/i)', alpha=0.7)
        
        ax.set_xlabel('Allele Frequency (number of copies)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Segregating Sites', fontsize=12, fontweight='bold')
        ax.set_title(f'Site Frequency Spectrum - {scenario}', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3, axis='y')
        
        if scenario != 'Neutral':
            ax.legend(fontsize=11)
        
        # Add Tajima's D annotation
        ax.text(0.98, 0.95, f"Tajima's D ≈ {tajima_d:.2f}", 
               transform=ax.transAxes, ha='right', va='top',
               fontsize=13, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Interpretation
    st.markdown(f"""
    <div class="selection-box">
    <h3>🔍 What You're Seeing:</h3>
    <h4>{scenario} Scenario</h4>
    <p><strong>Tajima's D ≈ {tajima_d:.2f}</strong></p>
    <ul>
    <li>{"<strong>D ≈ 0:</strong> Consistent with neutral evolution" if abs(tajima_d) < 0.5 else ""}</li>
    <li>{"<strong>D < 0:</strong> Excess of rare variants - suggests recent positive selection or population expansion" if tajima_d < -0.5 else ""}</li>
    <li>{"<strong>D > 0:</strong> Excess of intermediate frequencies - suggests balancing selection or bottleneck" if tajima_d > 0.5 else ""}</li>
    </ul>
    <p><strong>Pattern:</strong> {
        "Classic 1/i shape - many rare variants, progressively fewer as frequency increases" if scenario == 'Neutral' else
        "Excess rare variants + deficit intermediate = signature of recent selective sweep!" if scenario == 'Positive Selection (Sweep)' else
        "Excess intermediate frequencies = signature of balancing selection maintaining variation!" if scenario == 'Balancing Selection' else
        "Excess rare variants across genome = recent population growth, not locus-specific selection" if scenario == 'Population Expansion' else
        "Loss of rare variants + excess intermediate = population bottleneck reduced diversity"
    }</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Experiments to try
    st.markdown("---")
    st.markdown("### 🔍 What You Discovered")
    
    with st.expander("❓ Try these experiments:"):
        st.markdown("""
        1. **Neutral scenario:**
           - See the characteristic 1/i shape
           - Many singletons, few high-frequency variants
           - D ≈ 0
        
        2. **Positive Selection:**
           - Even MORE rare variants than neutral
           - "Hole" in intermediate frequencies
           - Maybe one high-frequency variant (selected allele)
           - D < 0 (often D < -1)
        
        3. **Balancing Selection:**
           - Fewer rare variants
           - Excess INTERMEDIATE frequencies
           - Classic example: MHC genes, sickle cell
           - D > 0 (often D > 1)
        
        4. **Compare θ values:**
           - Higher θ → More variants at ALL frequencies
           - But SHAPE stays the same!
           - This is why we use Tajima's D (shape-based) not raw counts
        
        5. **Sample size effect:**
           - Larger samples → more frequency classes
           - More power to detect selection
           - Real studies use 100s-1000s of individuals
        """)

# ============================================================================
# TAB 4: PART 3 - TAJIMA'S D
# ============================================================================
with tab4:
    st.markdown('<h2 class="section-header">📐 Part 3: Tajima\'s D - Detecting Deviations</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What Is Tajima's D?
    
    **Simple explanation:** A test statistic that compares two different ways of measuring genetic diversity.
    
    ### The Formula:
    
    **D = (π - θ) / √Var**
    
    Where:
    - **π** = Average pairwise differences (nucleotide diversity)
    - **θ** = Watterson's estimator (based on number of segregating sites)
    - **Var** = Variance of the difference
    
    ### Why Two Estimators?
    
    Both π and θ estimate the same thing (4Nμ) but use different information:
    
    1. **π (pi):** Counts all pairwise differences
       - More sensitive to intermediate-frequency variants
       - Formula: π = Σ(pairwise differences) / (n choose 2)
    
    2. **θ (theta, Watterson's):** Counts segregating sites
       - More sensitive to rare variants
       - Formula: θ = S / Σ(1/i) where S = number of segregating sites
    
    ### Under Neutrality:
    - **π ≈ θ** (both estimate 4Nμ correctly)
    - **D ≈ 0**
    
    ### Under Selection:
    - **Positive selection:** π < θ → **D < 0**
      - Why? Sweep removes variation, new mutations create rare variants
      - θ high (many singletons), π low (few pairwise differences)
    
    - **Balancing selection:** π > θ → **D > 0**
      - Why? Maintains intermediate-frequency variants
      - π high (many differences), θ normal
    
    ## Interpretation Guidelines:
    
    | Tajima's D | Interpretation | Biological Scenario |
    |-----------|----------------|---------------------|
    | D ≈ 0 | Neutral | Mutation-drift equilibrium |
    | D < -2 | Strong signal | Recent positive selection (sweep) |
    | -2 < D < 0 | Weak signal | Possible selection or population expansion |
    | 0 < D < 2 | Weak signal | Possible balancing selection or bottleneck |
    | D > 2 | Strong signal | Balancing selection |
    
    **Critical p-value:** |D| > 2 typically significant (p < 0.05)
    """)
    
    st.markdown("---")
    
    # Widget 3: Tajima's D Calculator
    st.markdown("### 🎮 Interactive 3: Calculate Tajima's D")
    
    st.info("**EDUCATIONAL TOOL - Input sequence data and calculate Tajima's D step-by-step!**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Input Parameters:")
        
        num_sequences = st.slider(
            "Number of sequences",
            min_value=5,
            max_value=50,
            value=10,
            step=5
        )
        
        num_seg_sites = st.slider(
            "Number of segregating sites (S)",
            min_value=5,
            max_value=100,
            value=20,
            step=5,
            help="Total number of polymorphic sites"
        )
        
        avg_pairwise = st.slider(
            "Average pairwise differences (π)",
            min_value=5.0,
            max_value=50.0,
            value=15.0,
            step=1.0,
            help="Average number of differences between sequences"
        )
        
        show_calculation = st.checkbox("Show detailed calculation steps", value=True)
        
        st.info(f"""
        **Current data:**
        - n = {num_sequences} sequences
        - S = {num_seg_sites} segregating sites
        - π = {avg_pairwise} pairwise diffs
        """)
    
    with col2:
        n = num_sequences
        S = num_seg_sites
        pi = avg_pairwise
        
        # Calculate Watterson's estimator (θ)
        a1 = sum(1/i for i in range(1, n))
        theta_w = S / a1
        
        # Calculate variance components
        a2 = sum(1/(i**2) for i in range(1, n))
        b1 = (n + 1) / (3 * (n - 1))
        b2 = 2 * (n**2 + n + 3) / (9 * n * (n - 1))
        c1 = b1 - (1 / a1)
        c2 = b2 - ((n + 2) / (a1 * n)) + (a2 / (a1**2))
        e1 = c1 / a1
        e2 = c2 / (a1**2 + a2)
        
        # Variance of D
        var_D = e1 * S + e2 * S * (S - 1)
        
        # Tajima's D
        if var_D > 0:
            D = (pi - theta_w) / np.sqrt(var_D)
        else:
            D = 0
        
        if show_calculation:
            st.markdown("### 📐 Step-by-Step Calculation:")
            
            st.markdown(f"""
            **Step 1:** Calculate Watterson's estimator (θ)
            ```
            a₁ = Σ(1/i) for i=1 to n-1
            a₁ = {a1:.4f}
            
            θ = S / a₁
            θ = {S} / {a1:.4f}
            θ = {theta_w:.4f}
            ```
            """)
            
            st.markdown(f"""
            **Step 2:** Calculate variance components
            ```
            a₂ = Σ(1/i²) = {a2:.4f}
            b₁ = (n+1)/(3(n-1)) = {b1:.4f}
            b₂ = 2(n²+n+3)/(9n(n-1)) = {b2:.4f}
            c₁ = b₁ - 1/a₁ = {c1:.4f}
            c₂ = b₂ - (n+2)/(a₁n) + a₂/a₁² = {c2:.4f}
            e₁ = c₁/a₁ = {e1:.4f}
            e₂ = c₂/(a₁²+a₂) = {e2:.4f}
            ```
            """)
            
            st.markdown(f"""
            **Step 3:** Calculate variance of D
            ```
            Var(D) = e₁·S + e₂·S·(S-1)
            Var(D) = {e1:.4f}·{S} + {e2:.4f}·{S}·{S-1}
            Var(D) = {var_D:.4f}
            ```
            """)
            
            st.markdown(f"""
            **Step 4:** Calculate Tajima's D
            ```
            D = (π - θ) / √Var(D)
            D = ({pi} - {theta_w:.4f}) / √{var_D:.4f}
            D = {pi - theta_w:.4f} / {np.sqrt(var_D):.4f}
            D = {D:.4f}
            ```
            """)
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
        
        # Plot 1: π vs θ comparison
        values = [pi, theta_w]
        labels = ['π\n(Pairwise)', 'θ\n(Watterson)']
        colors_comp = ['#3b82f6', '#10b981']
        
        bars = ax1.bar(labels, values, color=colors_comp, alpha=0.7, edgecolor='black', linewidth=2)
        ax1.set_ylabel('Diversity Estimate', fontsize=12, fontweight='bold')
        ax1.set_title('Comparing Two Diversity Estimators', fontsize=13, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{val:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        # Highlight difference
        if pi > theta_w:
            ax1.annotate('', xy=(0.5, pi), xytext=(0.5, theta_w),
                        arrowprops=dict(arrowstyle='<->', lw=3, color='red'))
            ax1.text(0.5, (pi+theta_w)/2, f'π > θ\nD > 0', ha='right', 
                    fontsize=11, color='red', fontweight='bold')
        elif pi < theta_w:
            ax1.annotate('', xy=(0.5, theta_w), xytext=(0.5, pi),
                        arrowprops=dict(arrowstyle='<->', lw=3, color='blue'))
            ax1.text(0.5, (pi+theta_w)/2, f'π < θ\nD < 0', ha='right', 
                    fontsize=11, color='blue', fontweight='bold')
        
        # Plot 2: D on interpretation scale
        ax2.axhline(y=0, color='gray', linestyle='-', linewidth=2, alpha=0.5)
        ax2.axhline(y=-2, color='red', linestyle='--', linewidth=1.5, alpha=0.5, label='Significance threshold')
        ax2.axhline(y=2, color='green', linestyle='--', linewidth=1.5, alpha=0.5)
        
        # Color regions
        ax2.fill_between([-3, 3], -2, 0, alpha=0.2, color='red', label='Positive selection')
        ax2.fill_between([-3, 3], 0, 2, alpha=0.2, color='green', label='Balancing selection')
        
        # Plot D value
        color_d = 'red' if D < 0 else 'green'
        ax2.plot([0], [D], 'o', markersize=25, color=color_d, 
                markeredgecolor='black', markeredgewidth=3, label=f'Your D = {D:.2f}', zorder=10)
        
        ax2.set_xlim(-1, 1)
        ax2.set_ylim(-3, 3)
        ax2.set_ylabel("Tajima's D", fontsize=12, fontweight='bold')
        ax2.set_title("Tajima's D Interpretation Scale", fontsize=13, fontweight='bold')
        ax2.legend(loc='upper left', fontsize=9)
        ax2.grid(alpha=0.3, axis='y')
        ax2.set_xticks([])
        
        # Add interpretation text
        if D < -2:
            interp = "Strong evidence of\npositive selection"
        elif D < 0:
            interp = "Weak evidence of\nselection/expansion"
        elif D > 2:
            interp = "Strong evidence of\nbalancing selection"
        elif D > 0:
            interp = "Weak evidence of\nbalancing/bottleneck"
        else:
            interp = "Neutral\nevolution"
        
        ax2.text(0, D + 0.3, interp, ha='center', fontsize=11, 
                fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Final interpretation
    if abs(D) > 2:
        st.error(f"""
        ### 🚨 **Significant Result: D = {D:.3f}**
        
        **Statistical significance:** |D| > 2 (p < 0.05)
        
        **Biological interpretation:**
        {
        f"**POSITIVE SELECTION** - Strong signal of recent selective sweep! The locus shows excess rare variants and deficit of intermediate frequencies, consistent with hitchhiking effect of beneficial mutation." if D < -2 else
        f"**BALANCING SELECTION** - Strong signal of maintaining variation! The locus shows excess intermediate-frequency variants, consistent with heterozygote advantage or frequency-dependent selection."
        }
        
        **Next steps for research:**
        - Scan flanking regions for extent of selection
        - Look for candidate genes
        - Test for functional effects
        - Compare across populations
        """)
    else:
        st.success(f"""
        ### ✅ **Non-significant Result: D = {D:.3f}**
        
        **Statistical significance:** |D| < 2 (not significant at p < 0.05)
        
        **Biological interpretation:**
        Data consistent with neutral evolution. No strong evidence for selection at this locus.
        
        **Note:** Weak signals (-2 < D < 0 or 0 < D < 2) might still be real but require:
        - Larger sample sizes
        - Additional evidence from other methods
        - Replication in independent populations
        """)

# ============================================================================
# TAB 5: PART 4 - MULTIPLE METHODS
# ============================================================================
with tab5:
    st.markdown('<h2 class="section-header">🔬 Part 4: Selection Signatures - Multiple Methods</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Beyond Tajima's D
    
    Tajima's D is just **one** method! Let's explore others:
    """)
    
    # Methods comparison table
    st.markdown("### 📊 Selection Detection Methods - Comparison")
    
    methods_data = {
        'Method': [
            'Tajima\'s D',
            'FST Outliers',
            'dN/dS Ratio',
            'iHS (Integrated Haplotype Score)',
            'XP-EHH (Cross-pop EHH)',
            'Fay & Wu\'s H'
        ],
        'What it Detects': [
            'Deviation from neutral SFS',
            'Local adaptation between populations',
            'Protein evolution',
            'Recent positive selection (within pop)',
            'Selection differences between pops',
            'High-frequency derived alleles'
        ],
        'Best For': [
            'General selection detection',
            'Population differentiation',
            'Coding sequence evolution',
            'Recent sweeps (<10k years)',
            'Comparing populations',
            'Distinguishing sweep types'
        ],
        'Time Scale': [
            'Recent-intermediate',
            'Any',
            'Long-term',
            'Very recent',
            'Recent',
            'Recent-intermediate'
        ],
        'Data Required': [
            'Sequence polymorphism',
            'Multiple populations',
            'Coding sequences',
            'Phased haplotypes',
            'Two populations, phased',
            'Sequence + outgroup'
        ]
    }
    
    df_methods = pd.DataFrame(methods_data)
    st.dataframe(df_methods, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Method details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 1. **FST Outliers**
        
        **Principle:** Loci under local adaptation show higher FST than neutral expectation
        
        **How it works:**
        1. Calculate FST for thousands of SNPs
        2. Plot FST vs heterozygosity
        3. Identify outliers (much higher FST)
        4. Outliers = candidate selected loci
        
        **Example:** High FST at altitude-adaptation genes in Tibetan vs lowland populations
        
        **Advantages:**
        - Doesn't require phasing
        - Works with any number of populations
        - Identifies population-specific adaptation
        
        **Limitations:**
        - Requires multiple populations
        - Can't detect balancing selection
        - Demographic history affects baseline
        """)
        
        st.markdown("""
        ### 2. **dN/dS Ratio**
        
        **Principle:** Compare rates of nonsynonymous vs synonymous substitutions
        
        **Formula:** ω = dN/dS
        
        **Interpretation:**
        - ω < 1: Purifying selection (most genes)
        - ω = 1: Neutral evolution
        - ω > 1: Positive selection
        
        **Example:** Immune genes often show ω > 1 at antigen-binding sites
        
        **Advantages:**
        - Clear biological interpretation
        - Works on divergence data
        - Can pinpoint specific codons
        
        **Limitations:**
        - Only for coding sequences
        - Requires outgroup
        - Long-term signal (misses recent selection)
        """)
        
        st.markdown("""
        ### 3. **Integrated Haplotype Score (iHS)**
        
        **Principle:** Recent sweeps create long haplotypes around selected allele
        
        **How it works:**
        1. Measure haplotype homozygosity extending from SNP
        2. Compare derived vs ancestral allele
        3. Strong signal if one allele has long haplotypes
        
        **Example:** Lactase persistence shows extreme iHS signal
        
        **Advantages:**
        - Very sensitive to recent selection
        - Works within single population
        - Doesn't need outgroup
        
        **Limitations:**
        - Requires phased haplotypes
        - Only recent selection (<50k years)
        - Computationally intensive
        """)
    
    with col2:
        # Visualization: FST outlier plot
        st.markdown("#### FST Outlier Detection - Example")
        
        np.random.seed(42)
        n_snps = 500
        
        # Neutral SNPs
        het = np.random.beta(2, 2, n_snps)
        fst_neutral = np.random.beta(2, 8, n_snps) * 0.3
        
        # Add some outliers (selected loci)
        n_outliers = 15
        outlier_idx = np.random.choice(n_snps, n_outliers, replace=False)
        het[outlier_idx] = np.random.beta(3, 3, n_outliers)
        fst_neutral[outlier_idx] = np.random.beta(8, 2, n_outliers) * 0.7 + 0.3
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot neutral
        ax.scatter(het, fst_neutral, alpha=0.5, s=30, color='gray', label='Neutral SNPs')
        
        # Highlight outliers
        ax.scatter(het[outlier_idx], fst_neutral[outlier_idx], 
                  s=100, color='red', edgecolor='black', linewidth=2, 
                  label='FST outliers (candidate selected loci)', zorder=10)
        
        # Add threshold line
        fst_threshold = np.percentile(fst_neutral, 95)
        ax.axhline(y=fst_threshold, color='red', linestyle='--', 
                  linewidth=2, label=f'95th percentile ({fst_threshold:.3f})', alpha=0.7)
        
        ax.set_xlabel('Heterozygosity (He)', fontsize=12, fontweight='bold')
        ax.set_ylabel('FST', fontsize=12, fontweight='bold')
        ax.set_title('FST Outlier Method - Genome Scan', fontsize=13, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        st.info("""
        **Red points** = Candidate loci under selection
        - Much higher FST than expected
        - Indicates local adaptation
        - Needs validation with other methods
        """)
    
    st.markdown("---")
    
    # Real examples
    st.markdown("### 🌍 Real Examples from Indian Populations")
    
    st.markdown("""
    #### Example 1: Lactase Persistence (LCT gene)
    
    **Background:** Ability to digest lactose in adulthood
    
    **Selection signatures detected:**
    - ✅ Tajima's D < -2 in dairy-farming populations
    - ✅ FST outlier between North (dairy) vs South India
    - ✅ iHS signal extremely strong
    - ✅ Long haplotypes around -13910*T allele
    
    **Interpretation:** Strong positive selection in populations with dairy farming history
    
    **Timeline:** Selection began ~10,000 years ago with animal domestication
    """)
    
    st.markdown("""
    #### Example 2: Malaria Resistance (G6PD, HBB)
    
    **Background:** Protection against malaria in endemic regions
    
    **G6PD deficiency:**
    - Tajima's D > 0 (balancing selection)
    - Maintained at intermediate frequency
    - Trade-off: protection vs hemolytic anemia
    
    **Sickle cell (HBB):**
    - Classic balancing selection
    - Heterozygote advantage
    - High frequency in tribal populations in endemic regions
    
    **FST pattern:** High differentiation between endemic vs non-endemic regions
    """)
    
    st.markdown("""
    #### Example 3: Altitude Adaptation (EGLN1, EPAS1)
    
    **Background:** Tibetan plateau populations (~4000m elevation)
    
    **Selection signatures:**
    - Extreme FST outliers vs lowland populations
    - iHS signals in Tibetan populations
    - Different alleles from Andean populations (convergent evolution)
    
    **Function:** Regulate oxygen sensing and red blood cell production
    
    **Indian relevance:** Ladakhi and Sherpa populations show similar signatures
    """)
    
    st.markdown("---")
    
    # Recommendations
    st.markdown("### 💡 Which Method Should You Use?")
    
    decision_tree = """
    ```
    START: What's your question?
    │
    ├─ Recent selection within population?
    │  └─ Use: iHS or Tajima's D
    │
    ├─ Selection difference between populations?
    │  └─ Use: FST outliers or XP-EHH
    │
    ├─ Protein evolution / coding sequences?
    │  └─ Use: dN/dS ratio
    │
    ├─ Balancing selection?
    │  └─ Use: Tajima's D (look for D > 0)
    │
    └─ Comprehensive scan?
       └─ Use: Multiple methods + integrate results
    ```
    """
    
    st.code(decision_tree, language='text')
    
    st.warning("""
    ### ⚠️ Important Caveats
    
    1. **Demography mimics selection:**
       - Population expansion → D < 0 (like selection)
       - Bottleneck → D > 0 (like balancing selection)
       - Solution: Genome-wide analysis + demographic modeling
    
    2. **Multiple testing:**
       - Testing thousands of SNPs → many false positives
       - Solution: Correct for multiple testing (FDR, Bonferroni)
    
    3. **Confirmation needed:**
       - One method alone is not enough
       - Use multiple methods
       - Validate in independent populations
       - Test functional predictions
    
    4. **Sample size matters:**
       - Small samples = low power
       - Need 20+ individuals for reasonable power
       - 100+ for recent selection detection
    """)

# ============================================================================
# TAB 6: SUMMARY
# ============================================================================
with tab6:
    st.markdown('<h2 class="section-header">🎯 Summary & Key Takeaways</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What You've Mastered
    
    Congratulations! You've completed Module 5B - Selection Signatures!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Core Concepts
        
        1. **Neutral Theory**
           - Kimura's revolutionary null hypothesis
           - Most mutations neutral or deleterious
           - dN/dS < 1 for most genes
           - Basis for all selection detection
        
        2. **Site Frequency Spectrum**
           - 1/i distribution under neutrality
           - Positive selection → excess rare variants
           - Balancing selection → excess intermediate
           - Shape reveals evolutionary process
        
        3. **Tajima's D**
           - Compares π vs θ
           - D ≈ 0 → neutral
           - D < 0 → positive selection
           - D > 0 → balancing selection
           - |D| > 2 typically significant
        
        4. **Multiple Methods**
           - FST outliers for local adaptation
           - iHS for recent sweeps
           - dN/dS for protein evolution
           - Integration increases power
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Skills Acquired
        
        1. **Analytical Skills**
           - Calculate Tajima's D
           - Interpret SFS patterns
           - Identify FST outliers
           - Evaluate dN/dS ratios
        
        2. **Critical Thinking**
           - Distinguish selection from demography
           - Choose appropriate methods
           - Integrate multiple lines of evidence
           - Understand method limitations
        
        3. **Real Applications**
           - Detect adaptation in populations
           - Identify disease resistance
           - Breeding program optimization
           - Conservation genetics
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🎓 Pattern Hunters Principles Demonstrated
    
    1. ✅ **"Understand the null first"**
       - Neutral theory = our baseline
       - Deviations reveal selection
       - Can't detect signal without knowing noise
    
    2. ✅ **"Patterns have shapes"**
       - SFS shape reveals evolutionary process
       - 1/i = neutral
       - Different shapes = different forces
    
    3. ✅ **"Multiple perspectives strengthen conclusions"**
       - Don't rely on single method
       - Tajima's D + FST + iHS = stronger evidence
       - Cross-validate findings
    
    4. ✅ **"Local examples, universal principles"**
       - Lactase in India = same as Europe
       - Malaria resistance = classic balancing selection
       - Principles work everywhere
    """)
    
    st.markdown("---")
    
    # Quick reference
    st.markdown("## 📊 Quick Reference Guide")
    
    reference_data = {
        'Signal': ['D < -2', '-2 < D < 0', 'D ≈ 0', '0 < D < 2', 'D > 2'],
        'Primary Interpretation': [
            'Positive selection (sweep)',
            'Weak selection / expansion',
            'Neutral evolution',
            'Weak balancing / bottleneck',
            'Balancing selection'
        ],
        'SFS Pattern': [
            'Excess rare + high frequency',
            'More rare variants',
            'Classic 1/i shape',
            'More intermediate',
            'Excess intermediate frequency'
        ],
        'Example': [
            'Lactase persistence',
            'Recent population growth',
            'Most of genome',
            'Demographic bottleneck',
            'MHC genes, sickle cell'
        ]
    }
    
    df_ref = pd.DataFrame(reference_data)
    st.dataframe(df_ref, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🚀 Next Steps & Applications
    
    ### Module 5C: Effective Population Size (Coming Next!)
    
    You'll learn:
    - Why Ne < census size
    - Estimating Ne from genetic data
    - The 50/500 rule for conservation
    - Bottleneck detection
    
    ### Apply Your Knowledge:
    
    1. **Research Project:**
       - Download genomic data (1000 Genomes, etc.)
       - Calculate Tajima's D across genome
       - Identify selection candidates
       - Compare populations
    
    2. **Conservation Application:**
       - Assess adaptive potential
       - Identify locally adapted populations
       - Guide translocation decisions
       - Preserve genetic diversity
    
    3. **Breeding Programs:**
       - Detect selection signatures in domestication
       - Identify targets for improvement
       - Avoid inbreeding
       - Maintain adaptive variation
    """)
    
    st.success("""
    ### 🎊 Congratulations!
    
    You've mastered **Selection Signatures**!
    
    You can now:
    - ✅ Understand neutral theory as null hypothesis
    - ✅ Interpret site frequency spectra
    - ✅ Calculate and interpret Tajima's D
    - ✅ Choose appropriate selection detection methods
    - ✅ Apply to real genomic data
    - ✅ Detect adaptation in natural populations
    
    **This skill is crucial for:**
    - Population genomics research
    - Conservation genetics
    - Understanding human evolution
    - Crop and livestock improvement
    - Disease resistance identification
    
    **Ready for Module 5C?** → Learn about effective population size!
    """)
    
    st.markdown("---")
    
    # Feedback
    st.markdown("### 📝 Feedback & Contact")
    
    with st.expander("💬 Share your thoughts"):
        st.markdown("""
        What did you think of Module 5B?
        
        - Was Tajima's D calculation clear?
        - Which examples were most helpful?
        - What was confusing?
        - How will you use selection detection?
        
        **Contact:** susama.kar@kuchindacollege.ac.in
        
        **GitHub:** https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Module 5B: Selection Signatures - Detecting Adaptive Evolution</strong></p>
    <p>Developed by Susama Kar & Dr. Alok Patel</p>
    <p>Department of Zoology, Kuchinda College, Sambalpur University</p>
    <p>Part of the Pattern Hunters Educational Series</p>
    <p>License: CC BY 4.0 | <a href="https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive">GitHub</a> | DOI: 10.5281/zenodo.17887470</p>
</div>
""", unsafe_allow_html=True)
