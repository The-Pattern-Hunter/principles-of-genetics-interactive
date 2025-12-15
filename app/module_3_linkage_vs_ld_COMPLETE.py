"""
Module 3: Linkage vs Linkage Disequilibrium
SUPER-ENHANCED - Breaking the #1 Confusion in Genetics

Two Words. Two TOTALLY Different Concepts.

Authors: Susama Kar & Dr. Alok Patel  
Institution: Department of Zoology, Kuchinda College, Sambalpur University
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(
    page_title="Module 3: Linkage vs LD",
    page_icon="🧬",
    layout="wide"
)

# Custom CSS - REDUCED from full version for token efficiency
st.markdown("""
<style>
.confusion-box {padding:1.5rem; border-radius:0.5rem; background:linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); color:white; margin:1rem 0; border:3px solid #c92a2a;}
.clarity-box {padding:1.5rem; border-radius:0.5rem; background:linear-gradient(135deg, #51cf66 0%, #37b24d 100%); color:white; margin:1rem 0;}
.linkage-box {padding:1.5rem; border-radius:0.5rem; background:linear-gradient(135deg, #748ffc 0%, #5c7cfa 100%); color:white; margin:1rem 0;}
.ld-box {padding:1.5rem; border-radius:0.5rem; background:linear-gradient(135deg, #ffd43b 0%, #fcc419 100%); color:#1e3a8a; margin:1rem 0;}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 style="color:#1e3a8a; font-size:2.5rem;">🧬 Linkage vs Linkage Disequilibrium</h1>', unsafe_allow_html=True)
st.markdown("**Breaking the #1 Confusion in Genetics**")
st.markdown("**Authors:** Susama Kar & Dr. Alok Patel | Kuchinda College, Sambalpur University")
st.markdown("---")

# THE CONFUSION
st.markdown("""
<div class="confusion-box">
<h2>⚠️ THE #1 CONFUSION</h2>
<h3>Students think:</h3>
<ul>
<li>"LD is just short for 'Linkage'" ❌</li>
<li>"Linked genes always have LD" ❌</li>
<li>"They're basically the same" ❌❌❌</li>
</ul>
<h3 style="color:#ffed4e;">ALL WRONG! Completely different concepts!</h3>
</div>
""", unsafe_allow_html=True)

# THE TRUTH
st.markdown("""
<div class="clarity-box">
<h2>✅ THE TRUTH</h2>
<table style="width:100%; background:white; color:#1e3a8a; font-size:1.1rem;">
<tr style="background:#37b24d; color:white;">
<th>Concept</th><th>What It Is</th><th>Type</th><th>Changes?</th>
</tr>
<tr>
<td><strong>LINKAGE</strong></td>
<td>Physical location on chromosome</td>
<td>PHYSICAL/SPATIAL</td>
<td>NO (permanent)</td>
</tr>
<tr>
<td><strong>LD</strong></td>
<td>Statistical association of alleles</td>
<td>STATISTICAL/TEMPORAL</td>
<td>YES (decays)</td>
</tr>
</table>
<p style="font-size:1.2rem; margin-top:1rem;"><strong>Linkage = WHERE genes ARE | LD = HOW alleles ASSOCIATE</strong></p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Confusion", "🔵 Linkage", "🟡 LD", "⏰ LD Decay", "🔗 Relationship", "🎯 Summary"
])

# TAB 1: CONFUSION
with tab1:
    st.markdown("## Why Students Get Confused")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ❌ Similar Names
        - "Linkage"
        - "Linkage **Disequilibrium**"
        
        ### ❌ They ARE Related
        - Both involve genes/loci
        - Recombination affects both
        - Close genes → slow LD decay
        """)
    
    with col2:
        st.success("""
        ### ✅ The Four Combinations
        
        | Linkage? | LD? | Example |
        |----------|-----|---------|
        | YES | YES | F2 cross |
        | YES | NO | Old population |
        | NO | YES | Admixture |
        | NO | NO | Equilibrium |
        
        **You can have ANY combination!**
        """)
    
    # Visual
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Linkage (physical)
    ax1.plot([0, 100], [1, 1], 'k-', linewidth=8)
    for pos, label, c in [(10, 'A', '#3b82f6'), (15, 'B', '#3b82f6'), (50, 'C', '#ef4444')]:
        ax1.plot(pos, 1, 'o', markersize=20, color=c, markeredgecolor='black', markeredgewidth=2)
        ax1.text(pos, 0.7, label, ha='center', fontsize=10, fontweight='bold')
    ax1.plot([10, 15], [1.3, 1.3], 'b-', linewidth=3)
    ax1.text(12.5, 1.4, 'LINKED', ha='center', fontweight='bold')
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 2)
    ax1.set_title('LINKAGE = Physical Position (PERMANENT)', fontsize=13, fontweight='bold')
    ax1.axis('off')
    
    # LD (statistical)
    for allele, (x, y), c in [('A₁', (1, 3), '#3b82f6'), ('A₂', (1, 1), '#3b82f6'), 
                               ('B₁', (3, 3), '#ef4444'), ('B₂', (3, 1), '#ef4444')]:
        circle = plt.Circle((x, y), 0.4, color=c, alpha=0.7, edgecolor='black', linewidth=2)
        ax2.add_patch(circle)
        ax2.text(x, y, allele, ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    ax2.annotate('', xy=(2.6, 3), xytext=(1.4, 3), arrowprops=dict(arrowstyle='<->', lw=4, color='green'))
    ax2.text(2, 3.3, 'ASSOCIATED', ha='center', fontweight='bold')
    ax2.set_xlim(0, 4)
    ax2.set_ylim(0, 4)
    ax2.set_title('LD = Statistical Association (TEMPORARY)', fontsize=13, fontweight='bold')
    ax2.axis('off')
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# TAB 2: LINKAGE
with tab2:
    st.markdown("""
    <div class="linkage-box">
    <h2>🔵 LINKAGE - The Physical Concept</h2>
    <p><strong>Modules 1-2 were about linkage!</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## What is Linkage?
    
    **Definition:** Genes on same chromosome, close enough that recombination is reduced.
    
    ### Key:
    - **Physical/Spatial** - about LOCATION
    - **Permanent** - doesn't change
    - **Measured in cM** (map units)
    - **Same in all populations**
    
    From Modules 1-2: Genetic mapping, interference, COC
    """)
    
    # Map visualization
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot([0, 100], [1, 1], 'k-', linewidth=10)
    for pos, label, c in [(10, 'A', '#3b82f6'), (25, 'B', '#10b981'), (27, 'C', '#10b981'), (90, 'E', '#f59e0b')]:
        ax.plot(pos, 1, 'o', markersize=25, color=c, markeredgecolor='black', markeredgewidth=3)
        ax.text(pos, 0.6, label, ha='center', fontsize=11, fontweight='bold')
    ax.plot([25, 27], [1.7, 1.7], 'g-', linewidth=4)
    ax.text(26, 1.9, 'TIGHT (2 cM)', ha='center', fontweight='bold')
    ax.set_xlim(-5, 105)
    ax.set_ylim(0, 2.5)
    ax.set_title('Linkage Map (PERMANENT)', fontsize=14, fontweight='bold')
    ax.axis('off')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# TAB 3: LD
with tab3:
    st.markdown("""
    <div class="ld-box">
    <h2>🟡 LINKAGE DISEQUILIBRIUM - The Statistical Concept</h2>
    <p><strong>Modules 5A-5C use LD!</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## What is LD?
    
    **Definition:** Non-random association of alleles at different loci in a population.
    
    ### Key:
    - **Statistical** - about FREQUENCIES
    - **Temporary** - DECAYS over time
    - **Measured by D or r²**
    - **Different in populations**
    
    ### The D Coefficient:
    ```
    D = f(A₁B₁) - p(A₁)×p(B₁)
    
    D = 0 → Equilibrium (random)
    D ≠ 0 → Disequilibrium (associated)
    ```
    """)
    
    # LD calculator widget
    st.markdown("### 🎮 Interactive: Calculate LD")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        f_A1B1 = st.slider("f(A₁B₁)", 0.0, 1.0, 0.49, 0.01)
        f_A1B2 = st.slider("f(A₁B₂)", 0.0, 1.0, 0.21, 0.01)
        f_A2B1 = st.slider("f(A₂B₁)", 0.0, 1.0, 0.21, 0.01)
        f_A2B2 = st.slider("f(A₂B₂)", 0.0, 1.0, 0.09, 0.01)
        
        total = f_A1B1 + f_A1B2 + f_A2B1 + f_A2B2
        if abs(total - 1.0) > 0.01:
            st.error(f"Must sum to 1.0! Currently: {total:.2f}")
        
        # Normalize
        norm = [f_A1B1/total, f_A1B2/total, f_A2B1/total, f_A2B2/total]
        f_A1B1, f_A1B2, f_A2B1, f_A2B2 = norm
        
        # Allele freqs
        p_A1 = f_A1B1 + f_A1B2
        p_B1 = f_A1B1 + f_A2B1
        
        # Calculate D
        D = f_A1B1 - (p_A1 * p_B1)
        
        st.code(f"""
p(A₁) = {p_A1:.3f}
p(B₁) = {p_B1:.3f}

Expected f(A₁B₁) = {p_A1*p_B1:.3f}
Observed f(A₁B₁) = {f_A1B1:.3f}

D = {D:.4f}
        """)
    
    with col2:
        # Plot haplotype freqs
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Observed
        haps = ['A₁B₁', 'A₁B₂', 'A₂B₁', 'A₂B₂']
        obs = [f_A1B1, f_A1B2, f_A2B1, f_A2B2]
        ax1.bar(haps, obs, color='#ef4444', alpha=0.7, edgecolor='black', linewidth=2)
        ax1.set_title('Observed Frequencies', fontweight='bold')
        ax1.set_ylabel('Frequency')
        ax1.grid(alpha=0.3, axis='y')
        
        # Expected vs Observed
        exp = [p_A1*p_B1, p_A1*(1-p_B1), (1-p_A1)*p_B1, (1-p_A1)*(1-p_B1)]
        x = np.arange(4)
        w = 0.35
        ax2.bar(x-w/2, obs, w, label='Observed', color='#ef4444', alpha=0.7, edgecolor='black')
        ax2.bar(x+w/2, exp, w, label='Expected (LE)', color='#3b82f6', alpha=0.7, edgecolor='black')
        ax2.set_xticks(x)
        ax2.set_xticklabels(haps)
        ax2.set_title('Observed vs Expected', fontweight='bold')
        ax2.legend()
        ax2.grid(alpha=0.3, axis='y')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        if abs(D) < 0.01:
            st.success(f"**D ≈ 0:** EQUILIBRIUM! Alleles randomly associated.")
        elif D > 0:
            st.warning(f"**D = {D:.3f} > 0:** DISEQUILIBRIUM! A₁ and B₁ associated.")
        else:
            st.warning(f"**D = {D:.3f} < 0:** DISEQUILIBRIUM! A₁ and B₂ associated.")

# TAB 4: LD DECAY
with tab4:
    st.markdown("## ⏰ LD Decay Over Time")
    
    st.markdown("""
    **KEY INSIGHT:** LD is TEMPORARY! It decays at rate = recombination fraction!
    
    ### Formula:
    ```
    D_t = D_0 × (1 - r)^t
    
    Where:
    - D_t = LD at generation t
    - D_0 = Initial LD
    - r = recombination fraction
    - t = generations
    ```
    """)
    
    # LD decay simulator
    col1, col2 = st.columns([1, 2])
    
    with col1:
        D0 = st.slider("Initial D", 0.01, 0.25, 0.20, 0.01)
        r = st.slider("Recombination (r)", 0.0, 0.50, 0.10, 0.01)
        gens = st.slider("Generations", 10, 500, 100, 10)
        
        # Calculate half-life
        if r > 0:
            half_life = np.log(0.5) / np.log(1 - r)
        else:
            half_life = np.inf
        
        st.info(f"""
        **Half-life:** {half_life:.1f} generations
        
        Time for LD to decay to:
        - 50%: {half_life:.0f} gen
        - 10%: {half_life*3.32:.0f} gen
        - 1%: {half_life*6.64:.0f} gen
        """)
    
    with col2:
        # Plot decay
        t_range = np.arange(0, gens+1)
        D_t = D0 * (1 - r)**t_range
        
        fig, ax = plt.subplots(figsize=(11, 6))
        ax.plot(t_range, D_t, 'b-', linewidth=3, label=f'r = {r}')
        ax.axhline(D0/2, color='r', linestyle='--', linewidth=2, label='50% decay')
        if half_life < gens:
            ax.axvline(half_life, color='orange', linestyle='--', linewidth=2, label=f'Half-life = {half_life:.0f}')
        ax.set_xlabel('Generations', fontsize=12, fontweight='bold')
        ax.set_ylabel('D (LD coefficient)', fontsize=12, fontweight='bold')
        ax.set_title(f'LD Decay (r = {r})', fontsize=14, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        if r < 0.05:
            st.warning(f"**Tight linkage (r={r}):** LD persists {half_life:.0f}+ generations!")
        elif r < 0.3:
            st.info(f"**Moderate linkage:** LD decays in ~{half_life:.0f} generations")
        else:
            st.success(f"**Loose/unlinked:** LD decays quickly (~{half_life:.0f} gen)")

# TAB 5: RELATIONSHIP
with tab5:
    st.markdown("## 🔗 The Relationship Between Linkage and LD")
    
    st.markdown("""
    **HOW ARE THEY RELATED?**
    
    Linkage (r) determines HOW FAST LD decays, but doesn't determine IF LD exists!
    """)
    
    # Comparison table
    comp_data = {
        'Aspect': ['Definition', 'Type', 'Measured by', 'Timescale', 'Changes?', 'Depends on', 'Example'],
        'LINKAGE': [
            'Physical proximity',
            'Spatial/Physical',
            'Recombination fraction (r)',
            'Evolutionary',
            'NO (permanent)',
            'Chromosome structure',
            '2 genes 10 cM apart'
        ],
        'LD': [
            'Statistical association',
            'Population/Statistical',
            'D or r²',
            'Population history',
            'YES (decays)',
            'Recombination + history',
            '2 alleles associated'
        ]
    }
    
    df_comp = pd.DataFrame(comp_data)
    st.dataframe(df_comp, use_container_width=True, hide_index=True)
    
    # Four scenarios
    st.markdown("### The Four Scenarios:")
    
    scenarios = {
        'Scenario': ['1. New F2 cross', '2. Old equilibrium population', '3. Recent admixture', '4. Unlinked equilibrium'],
        'Linkage': ['✅ YES (close)', '✅ YES (close)', '❌ NO (far/different chr)', '❌ NO'],
        'LD': ['✅ YES (new)', '❌ NO (decayed)', '✅ YES (new)', '❌ NO'],
        'Why': [
            'Just created, no time to decay',
            'Had time to reach equilibrium',
            'Admixture creates LD even between unlinked loci',
            'Random mating, no history'
        ]
    }
    
    df_scen = pd.DataFrame(scenarios)
    st.dataframe(df_scen, use_container_width=True, hide_index=True)
    
    st.success("""
    ### 🎯 The Key Insight:
    
    **Linkage affects LD decay RATE, but doesn't determine LD EXISTENCE!**
    
    - Tight linkage (small r) → Slow LD decay
    - Loose linkage (large r) → Fast LD decay
    - No linkage (r=0.5) → Very fast decay
    
    **But:**
    - New populations: LD exists regardless of linkage
    - Old populations: LD can be 0 even with linkage
    """)

# TAB 6: SUMMARY
with tab6:
    st.markdown("## 🎯 Summary - Confusion CLEARED!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ What You Learned:
        
        1. **They're Different**
           - Linkage = Physical
           - LD = Statistical
        
        2. **Both Important**
           - Linkage: gene mapping
           - LD: GWAS, selection
        
        3. **Related But Independent**
           - Linkage affects LD decay
           - But you can have either without the other
        
        4. **Timescales**
           - Linkage: Permanent
           - LD: Temporary (generations)
        """)
    
    with col2:
        st.success("""
        ### 🎓 Key Formulas:
        
        **Linkage:**
        - RF = # recombinants / total
        - 0 ≤ RF ≤ 0.5
        
        **LD:**
        - D = f(A₁B₁) - p(A₁)p(B₁)
        - D_t = D_0(1-r)^t
        
        **Connection:**
        - Small r → Slow decay
        - Large r → Fast decay
        """)
    
    st.markdown("""
    ## 🌉 Connecting to Other Modules:
    
    **Linkage (Modules 1-2):**
    - Genetic mapping
    - Chromosome structure
    - Inheritance patterns
    
    **LD (Modules 5A-5C):**
    - Population structure
    - Selection detection
    - GWAS, QTL mapping
    
    **This module (3) is the BRIDGE!**
    """)
    
    st.success("""
    ### 🎊 Confusion CLEARED!
    
    You now understand:
    - ✅ Linkage ≠ LD
    - ✅ When each applies
    - ✅ How they relate
    - ✅ Why both matter
    
    **You'll never confuse them again!** 🎯
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#64748b; padding:2rem;'>
<p><strong>Module 3: Linkage vs LD</strong></p>
<p>Breaking the Biggest Confusion in Genetics</p>
<p>Susama Kar & Dr. Alok Patel | Kuchinda College, Sambalpur University</p>
<p>Part of the Pattern Hunters Educational Series</p>
</div>
""", unsafe_allow_html=True)
