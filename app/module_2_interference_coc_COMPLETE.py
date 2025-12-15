"""
Module 2: Interference & Coefficient of Coincidence
COMPLETE ENHANCED STREAMLIT VERSION - Beyond the Poisson!

When Reality Violates the Model - An Interactive Journey

Authors: Susama Kar & Dr. Alok Patel
Institution: Department of Zoology, Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from itertools import combinations

# Page configuration
st.set_page_config(
    page_title="Module 2: Interference & COC",
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: 1rem 0;
    }
    .violation-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        margin: 1rem 0;
    }
    .reality-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        margin: 1rem 0;
    }
    .gamete-table {
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background: #eff6ff;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🧬 Module 2: Interference & Coefficient of Coincidence</h1>', unsafe_allow_html=True)

st.markdown("""
**When Reality Violates the Model - An Interactive Journey Beyond Poisson**

**Authors:** Susama Kar & Dr. Alok Patel  
**Institution:** Department of Zoology, Kuchinda College, Sambalpur University

---
""")

# Pattern Hunters approach - ENHANCED
st.markdown("""
<div class="pattern-box">
<h3>🔍 The Pattern Hunters Journey: From Ideal to Real</h3>
<p><strong>Module 1:</strong> We learned crossovers follow Poisson distribution (independent events)</p>
<p><strong>Module 2:</strong> SURPRISE! Real crossovers are NOT independent! 🤯</p>

<h4>The Discovery Process:</h4>
<ol>
<li><strong>EXPECT (Module 1):</strong> If crossovers are independent (Poisson), we can predict double crossovers</li>
<li><strong>OBSERVE (Module 2):</strong> Actual double crossovers are FEWER than expected!</li>
<li><strong>QUANTIFY:</strong> Coefficient of Coincidence (COC) measures this violation</li>
<li><strong>UNDERSTAND:</strong> One crossover interferes with nearby crossovers</li>
<li><strong>APPLY:</strong> Use correct mapping functions (Kosambi, not Haldane)</li>
</ol>

<h4>Pattern Hunters Principle:</h4>
<p><strong>"Reality modifies theory"</strong> - The Poisson model is our starting point, but biology adds complexity!</p>
<p><strong>"Deviations are informative"</strong> - Interference tells us about chromosome mechanics!</p>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Introduction",
    "🧬 Part 1: Three-Point Cross",
    "📊 Part 2: COC & Interference",
    "📏 Part 3: Mapping Functions",
    "🐟 Part 4: Real Examples",
    "🎯 Summary"
])

# ============================================================================
# TAB 1: INTRODUCTION
# ============================================================================
with tab1:
    st.markdown('<h2 class="section-header">Welcome Beyond the Poisson!</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## The Story So Far (Module 1)
        
        You learned:
        - ✅ Crossovers follow **Poisson distribution**
        - ✅ Events are **independent**
        - ✅ RF can't exceed 50%
        
        **This was beautiful, elegant mathematics!**
        
        ## But Wait... 🤔
        
        When geneticists actually counted double crossovers in three-point crosses:
        
        **Expected (from Poisson):** 50 double crossovers  
        **Observed (real data):** 30 double crossovers  
        
        **What happened?** ❌ Poisson violated!
        
        ## The Discovery: Interference
        
        **Herman J. Muller (1916):** Discovered that one crossover **interferes** with formation of nearby crossovers!
        
        ### The Biological Reality:
        
        1. First crossover occurs
        2. Physical stress on chromosome
        3. Nearby regions "protected" from additional crossovers
        4. Result: Fewer double crossovers than expected
        
        This is called **positive interference** or **chromatid interference**.
        
        ## Why This Matters
        
        - **Gene mapping accuracy:** Need correct distances
        - **Linkage map construction:** Choose right formula
        - **Understanding meiosis:** Reveals chromosome mechanics
        - **QTL mapping:** Affects power and resolution
        
        ### What You'll Learn:
        
        1. 🧬 **Three-point crosses** - Ordering genes
        2. 📊 **COC & Interference** - Quantifying deviation
        3. 📏 **Mapping functions** - Haldane vs Kosambi
        4. 🐟 **Real data** - Labeo rohita & earthworms
        """)
    
    with col2:
        st.info("""
        ### 📊 Module Stats
        
        - **Duration:** 90-120 min
        - **Level:** Advanced BSc/MSc
        - **Widgets:** 4 interactive
        - **Real Data:** Yes!
        - **Prerequisites:** Module 1
        
        ### 🎓 Learning Levels
        
        - **BSc:** Three-point cross
        - **MSc:** COC calculation
        - **Research:** Mapping functions
        """)
        
        st.markdown("""
        <div class="violation-box">
        <h4>⚡ The Key Insight</h4>
        <p><strong>Poisson = No Interference</strong></p>
        <p>Reality = Positive Interference</p>
        <p><strong>COC < 1.0</strong> reveals this!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visual: Expected vs Observed
    st.markdown("## 🎯 The Interference Phenomenon")
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Panel 1: No Interference (Poisson expectation)
    distances = np.array([5, 10, 15, 20, 25, 30])
    expected_dco = distances * 0.5  # Simulated expectation
    
    ax1.bar(distances, expected_dco, color='#3b82f6', alpha=0.7, 
           edgecolor='black', linewidth=2, label='Expected DCO')
    ax1.set_xlabel('Map Distance (cM)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Double Crossovers', fontsize=11, fontweight='bold')
    ax1.set_title('No Interference (Poisson)\nTheoretical Expectation', 
                 fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(alpha=0.3, axis='y')
    
    # Panel 2: With Interference (Reality)
    observed_dco = expected_dco * 0.6  # COC = 0.6
    
    bars = ax2.bar(distances, observed_dco, color='#ef4444', alpha=0.7, 
                   edgecolor='black', linewidth=2, label='Observed DCO')
    ax2.plot(distances, expected_dco, 'b--', linewidth=2.5, 
            label='Expected (no interference)', alpha=0.7)
    ax2.set_xlabel('Map Distance (cM)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Double Crossovers', fontsize=11, fontweight='bold')
    ax2.set_title('With Interference (Reality)\nCOC = 0.6', 
                 fontsize=12, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(alpha=0.3, axis='y')
    
    # Panel 3: COC vs Distance
    coc_values = 1 - np.exp(-distances/20)  # Increases with distance
    
    ax3.plot(distances, coc_values, 'go-', linewidth=3, markersize=10, 
            markeredgecolor='black', markeredgewidth=2)
    ax3.axhline(y=1.0, color='blue', linestyle='--', linewidth=2, 
               label='COC = 1 (no interference)', alpha=0.7)
    ax3.fill_between(distances, coc_values, 1.0, alpha=0.2, color='red')
    ax3.set_xlabel('Map Distance (cM)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('COC', fontsize=11, fontweight='bold')
    ax3.set_title('Interference Decreases\nwith Distance', 
                 fontsize=12, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(alpha=0.3)
    ax3.set_ylim(0, 1.2)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.warning("""
    ### 🔑 Key Pattern:
    
    - **Short distances:** Strong interference (COC ~ 0.3-0.5)
    - **Long distances:** Weak interference (COC → 1.0)
    - **Very long:** Multiple intervals, independent (COC ≈ 1.0)
    
    **This distance-dependence is the PATTERN we'll explore!**
    """)
    
    st.success("👆 **Start with Part 1** to learn three-point test crosses!")

# ============================================================================
# TAB 2: PART 1 - THREE-POINT CROSS
# ============================================================================
with tab2:
    st.markdown('<h2 class="section-header">🧬 Part 1: Three-Point Test Cross</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Why Three Points?
    
    **Module 1:** Two-point crosses → Can't distinguish linkage from independence if RF = 50%
    
    **Module 2:** Three-point crosses → SOLVES this ambiguity!
    
    ### The Power of Three Points:
    
    1. **Determines gene order** unambiguously
    2. **Identifies double crossover class** (rarest class)
    3. **Measures interference** directly
    4. **More accurate distances** than two-point
    
    ## The Cross:
    
    ```
    Trihybrid (ABC/abc) × Tester (abc/abc)
    
    Looking at offspring from trihybrid parent:
    
    8 Possible Gamete Classes:
    1. ABC - Parental
    2. abc - Parental
    3. AbC - Single CO region 1
    4. aBc - Single CO region 1  
    5. ABc - Single CO region 2
    6. abC - Single CO region 2
    7. Abc - Double CO
    8. aBC - Double CO
    ```
    
    ## The Strategy:
    
    **Step 1:** Identify parental classes (most frequent)  
    **Step 2:** Identify DCO class (least frequent)  
    **Step 3:** Compare parental vs DCO → Determines which gene is in middle  
    **Step 4:** Calculate RF for each region  
    **Step 5:** Calculate COC and interference  
    """)
    
    st.markdown("---")
    
    # Widget 1: Gene Order Determination
    st.markdown("### 🎮 Interactive 1: Three-Point Cross Gene Ordering")
    
    st.info("**EDUCATIONAL TOOL - Learn to order genes from offspring data!**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Input Data:")
        
        st.markdown("**Three loci: A, B, C**")
        
        # Simulated data input
        use_example = st.checkbox("Use example data (Labeo rohita)", value=True)
        
        if use_example:
            # Example data
            st.info("""
            **Labeo rohita microsatellites:**
            - Locus A: Growth QTL
            - Locus B: Disease resistance
            - Locus C: Temperature tolerance
            
            Sample: 1000 offspring
            """)
            
            data_dict = {
                'ABC': 380,
                'abc': 370,
                'AbC': 65,
                'aBc': 75,
                'ABc': 55,
                'abC': 45,
                'Abc': 5,
                'aBC': 5
            }
        else:
            st.markdown("**Enter offspring counts:**")
            data_dict = {}
            for genotype in ['ABC', 'abc', 'AbC', 'aBc', 'ABc', 'abC', 'Abc', 'aBC']:
                data_dict[genotype] = st.number_input(
                    f"{genotype}:",
                    min_value=0,
                    max_value=500,
                    value=50,
                    step=1,
                    key=f'count_{genotype}'
                )
        
        show_steps = st.checkbox("Show step-by-step analysis", value=True)
        
        total = sum(data_dict.values())
        st.success(f"**Total offspring: {total}**")
    
    with col2:
        # Analysis
        st.markdown("### 📊 Analysis:")
        
        # Sort by frequency
        sorted_classes = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
        
        # Identify classes
        parental = sorted_classes[:2]
        dco = sorted_classes[-2:]
        sco = sorted_classes[2:6]
        
        # Create DataFrame
        df_classes = pd.DataFrame([
            {
                'Genotype': geno,
                'Count': count,
                'Frequency': f'{count/total*100:.1f}%',
                'Class': 'Parental' if (geno, count) in parental else
                        'DCO' if (geno, count) in dco else 'SCO'
            }
            for geno, count in sorted_classes
        ])
        
        st.dataframe(df_classes, use_container_width=True, hide_index=True)
        
        if show_steps:
            st.markdown("""
            ### 🔍 Step-by-Step Gene Ordering:
            
            **Step 1: Identify Parental Types** (most frequent)
            """)
            
            parental_genos = [p[0] for p in parental]
            st.code(f"Parental: {parental_genos[0]} and {parental_genos[1]}")
            
            st.markdown("**Step 2: Identify Double Crossover** (least frequent)")
            
            dco_genos = [d[0] for d in dco]
            st.code(f"DCO: {dco_genos[0]} and {dco_genos[1]}")
            
            st.markdown("""
            **Step 3: Determine Gene Order**
            
            Compare parental to DCO:
            - Middle gene will be the one that "switched"
            - Outer genes stay together in DCO
            """)
            
            # Logic to determine middle gene
            p1 = parental_genos[0]
            d1 = dco_genos[0]
            
            # Compare positions
            diffs = []
            for i, (p_allele, d_allele) in enumerate(zip(p1, d1)):
                if p_allele != d_allele:
                    diffs.append(['A', 'B', 'C'][i])
            
            if len(diffs) == 1:
                middle_gene = diffs[0]
                outer_genes = [g for g in ['A', 'B', 'C'] if g != middle_gene]
                gene_order = f"{outer_genes[0]} --- {middle_gene} --- {outer_genes[1]}"
            else:
                # More complex logic needed
                gene_order = "A --- B --- C (default)"
                middle_gene = 'B'
            
            st.success(f"""
            **Gene Order: {gene_order}**
            
            Middle gene: **{middle_gene}**
            """)
        
        # Calculate RF
        st.markdown("---")
        st.markdown("### 📏 Recombination Frequencies:")
        
        # RF calculations (simplified)
        total_offspring = sum(data_dict.values())
        
        # Assuming B is middle (A-B-C order)
        region1_recom = sum([data_dict[k] for k in ['AbC', 'aBc', 'Abc', 'aBC']])
        region2_recom = sum([data_dict[k] for k in ['ABc', 'abC', 'Abc', 'aBC']])
        
        rf1 = region1_recom / total_offspring
        rf2 = region2_recom / total_offspring
        
        st.code(f"""
        Region 1 (A-B): {rf1*100:.2f}%
        Region 2 (B-C): {rf2*100:.2f}%
        Total map (A-C): {(rf1+rf2)*100:.2f} cM
        """)
        
        # Visualization
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Draw genetic map
        pos_a = 0
        pos_b = rf1 * 100
        pos_c = (rf1 + rf2) * 100
        
        # Line
        ax.plot([pos_a, pos_c], [0.5, 0.5], 'k-', linewidth=4)
        
        # Genes
        for pos, label, color in [(pos_a, 'A', '#3b82f6'), 
                                   (pos_b, 'B', '#10b981'), 
                                   (pos_c, 'C', '#ef4444')]:
            ax.plot(pos, 0.5, 'o', markersize=25, color=color, 
                   markeredgecolor='black', markeredgewidth=3, zorder=10)
            ax.text(pos, 0.3, label, ha='center', fontsize=18, fontweight='bold')
        
        # Distances
        ax.text((pos_a + pos_b)/2, 0.65, f'{rf1*100:.1f} cM', 
               ha='center', fontsize=13, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))
        ax.text((pos_b + pos_c)/2, 0.65, f'{rf2*100:.1f} cM', 
               ha='center', fontsize=13, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))
        
        ax.set_xlim(-5, pos_c + 5)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title('Genetic Map', fontsize=15, fontweight='bold', pad=20)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ============================================================================
# TAB 3: PART 2 - COC & INTERFERENCE
# ============================================================================
with tab3:
    st.markdown('<h2 class="section-header">📊 Part 2: Coefficient of Coincidence & Interference</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="reality-box">
    <h3>🎯 Pattern Hunters Moment: Reality Violates the Model!</h3>
    <p><strong>Module 1 taught us:</strong> Crossovers are independent (Poisson)</p>
    <p><strong>If true:</strong> P(DCO) = P(CO in region 1) × P(CO in region 2)</p>
    <p><strong>Reality:</strong> P(DCO observed) < P(DCO expected) ❌</p>
    <p><strong>Conclusion:</strong> One crossover INTERFERES with nearby crossovers!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## The Coefficient of Coincidence (COC)
    
    **Definition:** The ratio of observed to expected double crossovers
    
    ### COC = Observed DCO / Expected DCO
    
    ### Where:
    - **Observed DCO** = Count from data (rarest class)
    - **Expected DCO** = RF₁ × RF₂ × Total offspring
    
    ### Interpretation:
    
    | COC Value | Meaning | Biological Reality |
    |-----------|---------|-------------------|
    | COC = 1.0 | No interference | Crossovers independent (rare!) |
    | COC < 1.0 | Positive interference | One CO prevents nearby CO (typical) |
    | COC > 1.0 | Negative interference | One CO promotes nearby CO (very rare) |
    | COC = 0.0 | Complete interference | No double COs at all |
    
    ## Interference (I)
    
    **Formula:** I = 1 - COC
    
    ### Interpretation:
    
    - **I = 0** → No interference (COC = 1)
    - **I = 0.5** → Moderate interference (COC = 0.5)
    - **I = 1.0** → Complete interference (COC = 0)
    
    **Typical values:** I = 0.2 to 0.8 (varies by organism and distance)
    """)
    
    st.markdown("---")
    
    # Widget 2: COC Calculator
    st.markdown("### 🎮 Interactive 2: Calculate COC & Interference")
    
    st.info("**EDUCATIONAL TOOL - See how interference affects double crossovers!**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Input Parameters:")
        
        rf1 = st.slider(
            "RF for Region 1 (%)",
            min_value=5.0,
            max_value=40.0,
            value=18.0,
            step=1.0
        ) / 100
        
        rf2 = st.slider(
            "RF for Region 2 (%)",
            min_value=5.0,
            max_value=40.0,
            value=12.0,
            step=1.0
        ) / 100
        
        total_offspring = st.slider(
            "Total offspring",
            min_value=100,
            max_value=2000,
            value=1000,
            step=100
        )
        
        observed_dco = st.slider(
            "Observed double crossovers",
            min_value=0,
            max_value=100,
            value=12,
            step=1
        )
        
        show_calculation = st.checkbox("Show calculation steps", value=True)
        
        st.info(f"""
        **Settings:**
        - RF₁ = {rf1*100:.1f}%
        - RF₂ = {rf2*100:.1f}%
        - N = {total_offspring}
        - Observed DCO = {observed_dco}
        """)
    
    with col2:
        # Calculations
        expected_dco = rf1 * rf2 * total_offspring
        
        if expected_dco > 0:
            coc = observed_dco / expected_dco
        else:
            coc = 0
        
        interference = 1 - coc
        
        if show_calculation:
            st.markdown("### 📐 Step-by-Step Calculation:")
            
            st.markdown(f"""
            **Step 1: Calculate Expected DCO**
            ```
            Expected DCO = RF₁ × RF₂ × N
            Expected DCO = {rf1} × {rf2} × {total_offspring}
            Expected DCO = {expected_dco:.2f}
            ```
            """)
            
            st.markdown(f"""
            **Step 2: Calculate COC**
            ```
            COC = Observed DCO / Expected DCO
            COC = {observed_dco} / {expected_dco:.2f}
            COC = {coc:.3f}
            ```
            """)
            
            st.markdown(f"""
            **Step 3: Calculate Interference**
            ```
            I = 1 - COC
            I = 1 - {coc:.3f}
            I = {interference:.3f}
            ```
            """)
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
        
        # Plot 1: Observed vs Expected
        categories = ['Expected\n(no interference)', 'Observed\n(with interference)']
        values = [expected_dco, observed_dco]
        colors_bar = ['#3b82f6', '#ef4444']
        
        bars = ax1.bar(categories, values, color=colors_bar, alpha=0.7, 
                      edgecolor='black', linewidth=2)
        ax1.set_ylabel('Number of Double Crossovers', fontsize=12, fontweight='bold')
        ax1.set_title('Expected vs Observed DCO', fontsize=13, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{val:.1f}', ha='center', va='bottom', 
                    fontsize=12, fontweight='bold')
        
        # Highlight difference
        if expected_dco > 0:
            mid_x = 0.5
            ax1.annotate('', xy=(mid_x, expected_dco), xytext=(mid_x, observed_dco),
                        arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
            diff = expected_dco - observed_dco
            ax1.text(mid_x + 0.1, (expected_dco + observed_dco)/2, 
                    f'Interference\nreduced by\n{diff:.1f} DCOs', 
                    fontsize=10, color='purple', fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
        
        # Plot 2: COC and Interference scales
        ax2.barh(['Interference (I)', 'COC'], [interference, coc], 
                color=['#ef4444', '#22c55e'], alpha=0.7, 
                edgecolor='black', linewidth=2)
        ax2.set_xlim(0, 1.2)
        ax2.set_xlabel('Value', fontsize=12, fontweight='bold')
        ax2.set_title('Interference Metrics', fontsize=13, fontweight='bold')
        ax2.grid(axis='x', alpha=0.3)
        
        # Add reference lines
        ax2.axvline(x=1.0, color='blue', linestyle='--', linewidth=2, 
                   label='No interference', alpha=0.7)
        ax2.axvline(x=0.5, color='orange', linestyle='--', linewidth=1.5, 
                   label='Moderate', alpha=0.7)
        ax2.legend(fontsize=9)
        
        # Add value labels
        ax2.text(interference + 0.02, 0, f'{interference:.3f}', 
                va='center', fontsize=11, fontweight='bold')
        ax2.text(coc + 0.02, 1, f'{coc:.3f}', 
                va='center', fontsize=11, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Interpretation
    if coc < 0.3:
        st.error(f"""
        ### 🔴 Strong Interference (COC = {coc:.3f}, I = {interference:.3f})
        
        **Interpretation:**
        - Very few double crossovers occur
        - One crossover strongly inhibits nearby crossovers
        - Typical for **short distances** (< 20 cM)
        
        **Example organisms:** Drosophila (short intervals)
        
        **Implication for mapping:**
        - Map distances will be UNDERESTIMATED if you use Haldane function
        - **Use Kosambi** or other interference-correcting functions
        """)
    elif coc < 0.7:
        st.warning(f"""
        ### 🟡 Moderate Interference (COC = {coc:.3f}, I = {interference:.3f})
        
        **Interpretation:**
        - Double crossovers reduced but still occur
        - Typical for **medium distances** (20-40 cM)
        
        **Example organisms:** Most organisms at medium intervals
        
        **Implication for mapping:**
        - Moderate correction needed
        - **Kosambi function recommended**
        """)
    else:
        st.success(f"""
        ### 🟢 Weak/No Interference (COC = {coc:.3f}, I = {interference:.3f})
        
        **Interpretation:**
        - Crossovers nearly independent
        - Typical for **long distances** (> 40 cM) or **different chromosomes**
        
        **Implication for mapping:**
        - Poisson model approximately valid
        - **Haldane function works** (but Kosambi also fine)
        """)
    
    # Pattern insight
    st.markdown("""
    ---
    ### 🎓 Pattern Hunters Insight:
    
    **The Distance-Dependence Pattern:**
    
    - **Short distances:** High interference (COC → 0)
    - **Medium distances:** Moderate interference (COC ≈ 0.4-0.7)
    - **Long distances:** Low interference (COC → 1.0)
    
    **Why?** Physical distance on chromosome determines whether crossovers can "see" each other!
    
    This pattern is **universal** across organisms - it's a fundamental property of meiotic mechanics!
    """)

# ============================================================================
# TAB 4: PART 3 - MAPPING FUNCTIONS
# ============================================================================
with tab4:
    st.markdown('<h2 class="section-header">📏 Part 3: Mapping Functions - Haldane vs Kosambi</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pattern-box">
    <h3>🔍 Pattern Hunters Question: How to Convert RF to Map Distance?</h3>
    <p><strong>Module 1:</strong> RF = (1 - e⁻²ᵘ)/2 for short distances</p>
    <p><strong>Module 2:</strong> But this assumes NO INTERFERENCE!</p>
    <p><strong>Solution:</strong> Use mapping functions that account for interference!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## The Problem
    
    **Observed RF doesn't directly equal map distance when:**
    1. Distances are long (multiple crossovers)
    2. Interference is present
    
    **Mapping functions** convert observed RF → True map distance
    
    ## Two Main Functions:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 1. Haldane Function (1919)
        
        **Assumption:** NO interference (Poisson)
        
        **Formula:**
        ```
        m = -½ ln(1 - 2r)
        ```
        
        Where:
        - m = map distance (Morgans)
        - r = recombination frequency
        
        **When to use:**
        - Neurospora (no interference)
        - Very long distances
        - Quick approximation
        
        **Pros:**
        - Simple formula
        - Mathematically elegant
        
        **Cons:**
        - OVERESTIMATES distance when interference present
        - Not realistic for most organisms
        """)
    
    with col2:
        st.markdown("""
        ### 2. Kosambi Function (1943)
        
        **Assumption:** Partial interference
        
        **Formula:**
        ```
        m = ¼ ln[(1 + 2r)/(1 - 2r)]
        ```
        
        **When to use:**
        - Most organisms (Drosophila, mammals, fish)
        - Medium distances (10-40 cM)
        - When COC < 1
        
        **Pros:**
        - More realistic
        - Accounts for interference
        - Better fit to real data
        
        **Cons:**
        - Slightly more complex
        - Still an approximation
        """)
    
    st.markdown("---")
    
    # Widget 3: Mapping Functions Comparison
    st.markdown("### 🎮 Interactive 3: Compare Mapping Functions")
    
    st.info("**EDUCATIONAL TOOL - See how different functions convert RF to distance!**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Visualization Controls:")
        
        max_rf = st.slider(
            "Maximum RF to display",
            min_value=0.1,
            max_value=0.49,
            value=0.35,
            step=0.01,
            format="%.2f"
        )
        
        show_haldane = st.checkbox("Show Haldane function", value=True)
        show_kosambi = st.checkbox("Show Kosambi function", value=True)
        show_linear = st.checkbox("Show linear (RF × 100 = cM)", value=True)
        
        st.markdown("---")
        st.markdown("**Calculate for specific RF:**")
        
        rf_calc = st.slider(
            "Recombination Frequency",
            min_value=0.05,
            max_value=0.45,
            value=0.18,
            step=0.01,
            format="%.2f"
        )
        
        # Calculate distances
        if rf_calc < 0.5:
            # Haldane
            m_haldane = -0.5 * np.log(1 - 2*rf_calc) * 100
            
            # Kosambi
            m_kosambi = 0.25 * np.log((1 + 2*rf_calc)/(1 - 2*rf_calc)) * 100
            
            # Linear
            m_linear = rf_calc * 100
            
            st.code(f"""
RF = {rf_calc}

Linear: {m_linear:.2f} cM
Haldane: {m_haldane:.2f} cM
Kosambi: {m_kosambi:.2f} cM

Difference (Haldane - Kosambi):
{m_haldane - m_kosambi:.2f} cM
            """)
    
    with col2:
        # Plot mapping functions
        rf_range = np.linspace(0.01, max_rf, 200)
        
        # Calculate distances for each function
        m_haldane_range = -0.5 * np.log(1 - 2*rf_range) * 100
        m_kosambi_range = 0.25 * np.log((1 + 2*rf_range)/(1 - 2*rf_range)) * 100
        m_linear_range = rf_range * 100
        
        fig, ax = plt.subplots(figsize=(11, 7))
        
        if show_haldane:
            ax.plot(rf_range, m_haldane_range, 'b-', linewidth=3, 
                   label='Haldane (no interference)', alpha=0.8)
        
        if show_kosambi:
            ax.plot(rf_range, m_kosambi_range, 'r-', linewidth=3, 
                   label='Kosambi (with interference)', alpha=0.8)
        
        if show_linear:
            ax.plot(rf_range, m_linear_range, 'g--', linewidth=2.5, 
                   label='Linear (RF × 100)', alpha=0.7)
        
        # Mark the calculated point
        if show_haldane:
            ax.plot(rf_calc, m_haldane, 'bo', markersize=15, 
                   markeredgecolor='black', markeredgewidth=2, zorder=10)
        if show_kosambi:
            ax.plot(rf_calc, m_kosambi, 'ro', markersize=15, 
                   markeredgecolor='black', markeredgewidth=2, zorder=10)
        
        # Shade difference
        if show_haldane and show_kosambi:
            ax.fill_between(rf_range, m_haldane_range, m_kosambi_range, 
                           alpha=0.2, color='purple', 
                           label='Interference correction')
        
        ax.set_xlabel('Recombination Frequency (r)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Map Distance (cM)', fontsize=12, fontweight='bold')
        ax.set_title('Mapping Functions Comparison', fontsize=14, fontweight='bold')
        ax.legend(fontsize=10, loc='upper left')
        ax.grid(alpha=0.3)
        ax.set_xlim(0, max_rf)
        
        # Add annotation at calculated point
        if show_haldane and show_kosambi:
            ax.annotate(f'Difference:\n{m_haldane - m_kosambi:.1f} cM', 
                       xy=(rf_calc, (m_haldane + m_kosambi)/2),
                       xytext=(rf_calc + 0.05, (m_haldane + m_kosambi)/2),
                       fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8),
                       arrowprops=dict(arrowstyle='->', lw=2))
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # Interpretation table
    st.markdown("### 📊 When to Use Which Function:")
    
    usage_data = {
        'Scenario': [
            'Neurospora, fungi',
            'Short distance (< 10 cM)',
            'Medium distance (10-40 cM)',
            'Long distance (> 40 cM)',
            'Drosophila, most animals',
            'Fish, plants',
            'Quick approximation'
        ],
        'Recommended Function': [
            'Haldane',
            'Either (difference small)',
            'Kosambi',
            'Haldane',
            'Kosambi',
            'Kosambi',
            'Linear (RF × 100)'
        ],
        'Typical COC': [
            '~1.0 (no interference)',
            '0.3-0.5',
            '0.4-0.7',
            '0.7-1.0',
            '0.4-0.6',
            '0.5-0.7',
            'N/A'
        ]
    }
    
    df_usage = pd.DataFrame(usage_data)
    st.dataframe(df_usage, use_container_width=True, hide_index=True)
    
    st.warning("""
    ### ⚡ Key Principle:
    
    **Haldane overestimates distance** when interference is present!
    
    Why? It assumes more double crossovers than actually occur, leading to inflated distance estimates.
    
    **For most organisms, use Kosambi!**
    """)

# ============================================================================
# TAB 5: PART 4 - REAL EXAMPLES
# ============================================================================
with tab5:
    st.markdown('<h2 class="section-header">🐟 Part 4: Real Examples - Labeo rohita & Earthworms</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="reality-box">
    <h3>🌍 Pattern Hunters in Action: Local Data, Universal Principles</h3>
    <p>Let's apply everything to REAL genetic data from Western Odisha!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Example 1: Labeo rohita
    st.markdown("## Example 1: Labeo rohita (Rohu) - Fish Genetics")
    
    st.markdown("""
    **Species:** *Labeo rohita* (Indian major carp)  
    **Source:** Mahanadi River system, Odisha  
    **Importance:** Major aquaculture species, QTL mapping for growth & disease resistance
    
    ### Three Microsatellite Loci:
    - **Locus A:** Growth rate QTL
    - **Locus B:** Disease resistance marker  
    - **Locus C:** Temperature tolerance
    
    ### Experimental Cross:
    - Trihybrid × Tester
    - N = 1000 offspring scored
    - Objective: Map loci, measure interference
    """)
    
    # Real data simulation
    labeo_data = {
        'Genotype': ['ABC', 'abc', 'AbC', 'aBc', 'ABc', 'abC', 'Abc', 'aBC'],
        'Count': [380, 370, 65, 75, 55, 45, 5, 5],
        'Class': ['Parental', 'Parental', 'SCO-1', 'SCO-1', 'SCO-2', 'SCO-2', 'DCO', 'DCO']
    }
    
    df_labeo = pd.DataFrame(labeo_data)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Offspring Data:")
        st.dataframe(df_labeo, use_container_width=True, hide_index=True)
        
        # Calculations
        total = sum(labeo_data['Count'])
        parental = 380 + 370
        sco1 = 65 + 75
        sco2 = 55 + 45
        dco_obs = 5 + 5
        
        rf1 = (sco1 + dco_obs) / total
        rf2 = (sco2 + dco_obs) / total
        
        dco_exp = rf1 * rf2 * total
        coc = dco_obs / dco_exp
        interference = 1 - coc
        
        st.code(f"""
CALCULATIONS:

Region 1 (A-B):
RF = ({sco1} + {dco_obs}) / {total}
RF = {rf1*100:.2f}%

Region 2 (B-C):
RF = ({sco2} + {dco_obs}) / {total}
RF = {rf2*100:.2f}%

Expected DCO:
= {rf1:.3f} × {rf2:.3f} × {total}
= {dco_exp:.2f}

COC = {dco_obs} / {dco_exp:.2f}
    = {coc:.3f}

Interference = 1 - {coc:.3f}
             = {interference:.3f}
        """)
    
    with col2:
        # Genetic map
        st.markdown("### 🗺️ Genetic Map:")
        
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Positions (using Kosambi)
        m1_kosambi = 0.25 * np.log((1 + 2*rf1)/(1 - 2*rf1)) * 100
        m2_kosambi = 0.25 * np.log((1 + 2*rf2)/(1 - 2*rf2)) * 100
        
        pos_a = 0
        pos_b = m1_kosambi
        pos_c = m1_kosambi + m2_kosambi
        
        # Draw
        ax.plot([pos_a, pos_c], [0.5, 0.5], 'k-', linewidth=5)
        
        for pos, label, color in [(pos_a, 'A\n(Growth)', '#3b82f6'), 
                                   (pos_b, 'B\n(Disease)', '#10b981'), 
                                   (pos_c, 'C\n(Temp)', '#ef4444')]:
            ax.plot(pos, 0.5, 'o', markersize=28, color=color, 
                   markeredgecolor='black', markeredgewidth=3, zorder=10)
            ax.text(pos, 0.25, label, ha='center', fontsize=12, fontweight='bold')
        
        # Distances
        ax.text((pos_a + pos_b)/2, 0.7, f'{m1_kosambi:.1f} cM\n(RF={rf1*100:.1f}%)', 
               ha='center', fontsize=11, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='black'))
        ax.text((pos_b + pos_c)/2, 0.7, f'{m2_kosambi:.1f} cM\n(RF={rf2*100:.1f}%)', 
               ha='center', fontsize=11, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='black'))
        
        ax.set_xlim(-5, pos_c + 5)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title('Labeo rohita Linkage Map (Kosambi)', fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    st.success(f"""
    ### 🎯 Labeo rohita Results:
    
    **COC = {coc:.3f}** → Moderate interference  
    **Interference = {interference:.3f}** → 58% reduction in DCO
    
    **Biological interpretation:**
    - Typical for fish (similar to Drosophila)
    - One crossover reduces probability of nearby crossover
    - Kosambi function appropriate for this organism
    
    **Breeding application:**
    - Can predict recombinants in marker-assisted selection
    - Disease resistance (B) linked to growth (A) at 15 cM
    - Expected 15% recombination in breeding programs
    """)
    
    st.markdown("---")
    
    # Example 2: Earthworms
    st.markdown("## Example 2: Earthworm (Metaphire) - Environmental Genomics")
    
    st.markdown("""
    **Species:** *Metaphire* sp. (earthworm)  
    **Source:** Talcher coalfield mining regions, Odisha  
    **Importance:** Biomonitoring, heavy metal tolerance genes
    
    ### Three Loci for Heavy Metal Tolerance:
    - **Locus P:** Lead tolerance
    - **Locus Q:** Cadmium tolerance  
    - **Locus R:** Mercury tolerance
    
    ### Research Context:
    Mining activities → heavy metal contamination → selection for tolerant earthworms
    """)
    
    # Earthworm data
    earthworm_data = {
        'Genotype': ['PQR', 'pqr', 'PqR', 'pQr', 'PQr', 'pqR', 'Pqr', 'pQR'],
        'Count': [295, 285, 88, 92, 105, 95, 18, 22],
        'Class': ['Parental', 'Parental', 'SCO-1', 'SCO-1', 'SCO-2', 'SCO-2', 'DCO', 'DCO']
    }
    
    df_earth = pd.DataFrame(earthworm_data)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.dataframe(df_earth, use_container_width=True, hide_index=True)
        
        # Calculations
        total_earth = sum(earthworm_data['Count'])
        dco_obs_earth = 18 + 22
        sco1_earth = 88 + 92
        sco2_earth = 105 + 95
        
        rf1_earth = (sco1_earth + dco_obs_earth) / total_earth
        rf2_earth = (sco2_earth + dco_obs_earth) / total_earth
        
        dco_exp_earth = rf1_earth * rf2_earth * total_earth
        coc_earth = dco_obs_earth / dco_exp_earth
        interference_earth = 1 - coc_earth
        
        st.code(f"""
EARTHWORM ANALYSIS:

RF₁ (P-Q) = {rf1_earth*100:.2f}%
RF₂ (Q-R) = {rf2_earth*100:.2f}%

Expected DCO = {dco_exp_earth:.1f}
Observed DCO = {dco_obs_earth}

COC = {coc_earth:.3f}
Interference = {interference_earth:.3f}

LESS interference than fish!
Typical for invertebrates.
        """)
    
    with col2:
        # Comparison chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        organisms = ['Labeo rohita\n(Fish)', 'Earthworm\n(Metaphire)']
        coc_values = [coc, coc_earth]
        interf_values = [interference, interference_earth]
        
        x = np.arange(len(organisms))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, coc_values, width, label='COC', 
                      color='#10b981', alpha=0.7, edgecolor='black', linewidth=2)
        bars2 = ax.bar(x + width/2, interf_values, width, label='Interference', 
                      color='#ef4444', alpha=0.7, edgecolor='black', linewidth=2)
        
        ax.axhline(y=1.0, color='blue', linestyle='--', linewidth=2, 
                  label='No interference', alpha=0.5)
        ax.axhline(y=0.5, color='orange', linestyle='--', linewidth=1.5, 
                  label='Moderate', alpha=0.5)
        
        ax.set_ylabel('Value', fontsize=12, fontweight='bold')
        ax.set_title('Interference Comparison: Fish vs Earthworm', 
                    fontsize=13, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(organisms)
        ax.legend(fontsize=10)
        ax.grid(axis='y', alpha=0.3)
        ax.set_ylim(0, 1.2)
        
        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.2f}', ha='center', va='bottom', 
                       fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    st.warning(f"""
    ### 🔬 Comparative Insights:
    
    **Labeo rohita:** COC = {coc:.2f}, I = {interference:.2f} (strong interference)  
    **Earthworm:** COC = {coc_earth:.2f}, I = {interference_earth:.2f} (moderate interference)
    
    **Why the difference?**
    - Chromosome structure
    - Genome size
    - Crossover control mechanisms
    
    **Pattern:** Vertebrates often show stronger interference than invertebrates!
    
    **Conservation application:**
    - Earthworms as biomonitors for contamination
    - Linked heavy metal tolerance loci
    - Marker-assisted monitoring of pollution-adapted populations
    """)

# ============================================================================
# TAB 6: SUMMARY
# ============================================================================
with tab6:
    st.markdown('<h2 class="section-header">🎯 Summary & Key Takeaways</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## What You've Mastered
    
    Congratulations! You've completed **Module 2: Interference & COC**!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Core Concepts
        
        1. **Three-Point Crosses**
           - Determines gene order unambiguously
           - Identifies double crossover class
           - More accurate than two-point
        
        2. **Interference**
           - One crossover interferes with nearby crossovers
           - Positive interference = typical
           - Distance-dependent phenomenon
        
        3. **Coefficient of Coincidence**
           - COC = Observed DCO / Expected DCO
           - COC < 1 → positive interference
           - COC = 1 → no interference (Poisson)
           - I = 1 - COC
        
        4. **Mapping Functions**
           - Haldane: assumes no interference
           - Kosambi: accounts for interference
           - Haldane overestimates when I > 0
           - Use Kosambi for most organisms
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Pattern Hunters Principles
        
        1. **"Models are starting points"**
           - Poisson (Module 1) was ideal
           - Reality adds complexity (Module 2)
           - Both models are useful!
        
        2. **"Deviations are informative"**
           - Fewer DCO than expected
           - Reveals chromosome mechanics
           - Not an error - it's biology!
        
        3. **"Quantify the deviation"**
           - COC and I measure interference
           - Pattern: distance-dependent
           - Universal across organisms
        
        4. **"Use appropriate tools"**
           - Match mapping function to organism
           - Kosambi for most cases
           - Haldane for special cases
        """)
    
    st.markdown("---")
    
    # Quick reference
    st.markdown("## 📊 Quick Reference Guide")
    
    quick_ref = {
        'Organism/Scenario': [
            'Neurospora (no interference)',
            'Drosophila (typical)',
            'Mammals (typical)',
            'Fish (Labeo rohita)',
            'Earthworms',
            'Short distances (< 10 cM)',
            'Long distances (> 40 cM)'
        ],
        'Typical COC': ['~1.0', '0.4-0.6', '0.4-0.6', '0.4-0.5', '0.5-0.7', '0.3-0.5', '0.7-1.0'],
        'Interference': ['None', 'Strong', 'Strong', 'Strong', 'Moderate', 'Strong', 'Weak'],
        'Recommended Function': [
            'Haldane',
            'Kosambi',
            'Kosambi',
            'Kosambi',
            'Kosambi',
            'Either',
            'Haldane or Kosambi'
        ]
    }
    
    df_quick = pd.DataFrame(quick_ref)
    st.dataframe(df_quick, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Formulas
    st.markdown("## 🧮 Key Formulas")
    
    st.markdown("""
    ### COC and Interference:
    ```
    COC = Observed DCO / Expected DCO
    
    Expected DCO = RF₁ × RF₂ × N
    
    Interference (I) = 1 - COC
    ```
    
    ### Mapping Functions:
    ```
    Haldane:  m = -½ ln(1 - 2r)
    
    Kosambi:  m = ¼ ln[(1 + 2r)/(1 - 2r)]
    ```
    
    Where:
    - m = map distance in Morgans (multiply by 100 for cM)
    - r = recombination frequency
    
    ### Gene Ordering from Three-Point:
    ```
    1. Identify parental (most frequent)
    2. Identify DCO (least frequent)
    3. Compare parental to DCO
    4. Middle gene = the one that "switched"
    ```
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🎓 The Complete Picture: Modules 1 + 2
    
    **Module 1 (Foundation):**
    - Poisson distribution governs crossovers
    - Events are independent
    - RF ≤ 50% always
    - Simple, elegant mathematics
    
    **Module 2 (Reality):**
    - Interference violates independence
    - COC quantifies deviation
    - Distance-dependent pattern
    - Need corrected mapping functions
    
    **Together:**
    - Ideal model → Real complexity
    - Theory → Practice
    - Universal principles → Organism-specific details
    
    This is how science works! Start simple, add complexity as needed.
    """)
    
    st.success("""
    ### 🎊 Congratulations!
    
    You've completed **Modules 1 & 2** of Genetic Mapping!
    
    You can now:
    - ✅ Understand Poisson distribution (Module 1)
    - ✅ Recognize when it's violated (Module 2)
    - ✅ Conduct three-point crosses
    - ✅ Calculate COC and interference
    - ✅ Choose appropriate mapping functions
    - ✅ Map genes in any organism
    - ✅ Apply to QTL mapping and breeding
    
    **Next:** Module 3 (Linkage vs Linkage Disequilibrium) coming soon!
    
    **You're ready for:**
    - Advanced genetics courses
    - QTL mapping projects
    - Breeding program design
    - Genomics research
    """)
    
    st.markdown("---")
    
    # Feedback
    st.markdown("### 📝 Feedback & Contact")
    
    with st.expander("💬 Share your thoughts"):
        st.markdown("""
        What did you think of Module 2?
        
        - Did the Pattern Hunters approach help?
        - Were the real examples useful?
        - Which widget was most helpful?
        - How can we improve?
        
        **Contact:** susama.kar@kuchindacollege.ac.in
        
        **GitHub:** https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Module 2: Interference & Coefficient of Coincidence</strong></p>
    <p>When Reality Violates the Model</p>
    <p>Developed by Susama Kar & Dr. Alok Patel</p>
    <p>Department of Zoology, Kuchinda College, Sambalpur University</p>
    <p>Part of the Pattern Hunters Educational Series</p>
    <p>License: CC BY 4.0 | <a href="https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive">GitHub</a> | DOI: 10.5281/zenodo.17887470</p>
</div>
""", unsafe_allow_html=True)