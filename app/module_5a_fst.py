"""
Module 5A: FST and Population Structure
Interactive FST calculator with real Indian biodiversity examples
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def render_module_5a():
    """Render complete Module 5A content"""
    
    st.title("Module 5A: FST and Population Structure")
    
    st.markdown("""
    ### 🎯 Learning Objectives
    - Understand what FST measures
    - Calculate FST using Wright's formula
    - Interpret FST for conservation decisions
    - Apply drift-migration balance
    """)
    
    tabs = st.tabs(["📖 Concept", "🎮 Interactive 1: Divergence", 
                    "🎮 Interactive 2: FST Calculator", 
                    "🎮 Interactive 3: Migration-FST", 
                    "📝 Practice"])
    
    # TAB 1: CONCEPT
    with tabs[0]:
        st.markdown("""
        ## How Different Are Two Populations?
        
        Imagine you catch fish from two rivers:
        - River A: 80% have allele A, 20% have allele a
        - River B: 50% have allele A, 50% have allele a
        
        **Question:** Are these the SAME population or DIFFERENT populations?
        
        ### Enter FST!
        
        **FST** (F-Statistics) quantifies genetic differentiation between populations.
        
        **Formula (Wright 1951):**
        ```
        FST = (HT - HS) / HT
        
        Where:
        HT = Expected heterozygosity if all were one population
        HS = Observed heterozygosity within subpopulations
        ```
        
        **Interpretation:**
        - FST = 0: No differentiation (same population)
        - FST = 0.05: Little differentiation
        - FST = 0.15: Moderate differentiation
        - FST = 0.25: Great differentiation  
        - FST = 1.0: Complete differentiation (fixed differences)
        """)
        
        # Indian examples
        st.info("""
        ### 🇮🇳 Indian Examples
        
        **Human Populations:**
        - ANI vs ASI: FST ≈ 0.03-0.05 (slight structure)
        - Tribal vs non-tribal: FST ≈ 0.08-0.12 (moderate)
        
        **Labeo rohita (Rohu):**
        - Mahanadi vs Ganga: FST ≈ 0.08-0.15
        - Within river system: FST ≈ 0.02-0.05
        
        **Indian Cattle:**
        - Sahiwal vs Gir: FST ≈ 0.10-0.15
        - Tharparkar vs Red Sindhi: FST ≈ 0.12-0.18
        """)
    
    # TAB 2: DIVERGENCE SIMULATOR
    with tabs[1]:
        st.markdown("## 🎮 Interactive: Population Divergence")
        
        st.markdown("""
        Watch two populations diverge due to **genetic drift** (random changes in allele frequencies).
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            generations = st.slider(
                "Generations",
                min_value=10,
                max_value=200,
                value=100,
                step=10
            )
            
        with col2:
            Ne_input = st.slider(
                "Effective Population Size (Ne)",
                min_value=10,
                max_value=500,
                value=100,
                step=10
            )
        
        # Simulate drift in two populations
        np.random.seed(42)
        
        # Starting frequency
        p0 = 0.5
        
        # Population 1
        freq_pop1 = [p0]
        for _ in range(generations):
            p_current = freq_pop1[-1]
            # Binomial sampling (drift)
            alleles = np.random.binomial(2 * Ne_input, p_current)
            p_new = alleles / (2 * Ne_input)
            freq_pop1.append(p_new)
        
        # Population 2
        freq_pop2 = [p0]
        for _ in range(generations):
            p_current = freq_pop2[-1]
            alleles = np.random.binomial(2 * Ne_input, p_current)
            p_new = alleles / (2 * Ne_input)
            freq_pop2.append(p_new)
        
        # Calculate FST at end
        p_final_1 = freq_pop1[-1]
        p_final_2 = freq_pop2[-1]
        
        # Average frequency
        p_avg = (p_final_1 + p_final_2) / 2
        
        # Variance
        var_p = ((p_final_1 - p_avg)**2 + (p_final_2 - p_avg)**2) / 2
        
        # FST (variance method)
        fst_final = var_p / (p_avg * (1 - p_avg)) if p_avg * (1 - p_avg) > 0 else 0
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(freq_pop1, 'b-', linewidth=2, label='Population 1')
        ax.plot(freq_pop2, 'r-', linewidth=2, label='Population 2')
        ax.axhline(y=p0, color='gray', linestyle='--', alpha=0.5, label='Starting frequency')
        
        ax.set_xlabel('Generation', fontsize=12)
        ax.set_ylabel('Allele Frequency', fontsize=12)
        ax.set_title(f'Genetic Drift in Two Isolated Populations (Ne = {Ne_input})', 
                     fontsize=14)
        ax.legend()
        ax.grid(alpha=0.3)
        ax.set_ylim(0, 1)
        
        st.pyplot(fig)
        
        # Results
        st.success(f"""
        ### 📊 Final Results (Generation {generations}):
        - **Population 1 frequency:** {p_final_1:.3f}
        - **Population 2 frequency:** {p_final_2:.3f}
        - **Difference:** {abs(p_final_1 - p_final_2):.3f}
        - **FST:** {fst_final:.3f}
        
        **Interpretation:** 
        {
        "No differentiation - populations are essentially identical" if fst_final < 0.05 else
        "Little differentiation - populations slightly different" if fst_final < 0.15 else
        "Moderate differentiation - populations clearly distinct" if fst_final < 0.25 else
        "Great differentiation - populations very different"
        }
        
        **Pattern:** Smaller Ne → faster divergence → higher FST
        """)
    
    # TAB 3: FST CALCULATOR
    with tabs[2]:
        st.markdown("## 🎮 Interactive: FST Calculator")
        
        st.markdown("""
        Calculate FST step-by-step using real allele frequency data.
        """)
        
        # Input method
        input_method = st.radio(
            "Choose input method:",
            ["🧬 Enter allele frequencies", "🐟 Use example (Labeo rohita)"]
        )
        
        if input_method == "🧬 Enter allele frequencies":
            col1, col2 = st.columns(2)
            
            with col1:
                p1 = st.number_input(
                    "Population 1: Frequency of allele A",
                    min_value=0.0,
                    max_value=1.0,
                    value=0.8,
                    step=0.05,
                    format="%.2f"
                )
            
            with col2:
                p2 = st.number_input(
                    "Population 2: Frequency of allele A",
                    min_value=0.0,
                    max_value=1.0,
                    value=0.5,
                    step=0.05,
                    format="%.2f"
                )
        else:
            # Labeo rohita example
            st.info("""
            **Example: Labeo rohila microsatellite locus LR-MS1**
            - Mahanadi River population: Allele A frequency = 0.75
            - Ganga River population: Allele A frequency = 0.55
            
            (Hypothetical data for demonstration)
            """)
            p1 = 0.75
            p2 = 0.55
        
        # Calculate step by step
        st.markdown("### 📐 Step-by-Step Calculation")
        
        # Step 1: Average frequency
        p_avg = (p1 + p2) / 2
        
        st.markdown(f"""
        **Step 1:** Calculate average allele frequency across populations
        ```
        p̄ = (p₁ + p₂) / 2
        p̄ = ({p1} + {p2}) / 2 = {p_avg:.3f}
        ```
        """)
        
        # Step 2: Variance
        var_p = ((p1 - p_avg)**2 + (p2 - p_avg)**2) / 2
        
        st.markdown(f"""
        **Step 2:** Calculate variance in allele frequencies
        ```
        Var(p) = [(p₁ - p̄)² + (p₂ - p̄)²] / 2
        Var(p) = [({p1} - {p_avg:.3f})² + ({p2} - {p_avg:.3f})²] / 2
        Var(p) = {var_p:.4f}
        ```
        """)
        
        # Step 3: Expected heterozygosity (total)
        HT = 2 * p_avg * (1 - p_avg)
        
        st.markdown(f"""
        **Step 3:** Calculate total expected heterozygosity (HT)
        ```
        HT = 2 × p̄ × (1 - p̄)
        HT = 2 × {p_avg:.3f} × {1-p_avg:.3f}
        HT = {HT:.4f}
        ```
        """)
        
        # Step 4: Within-population heterozygosity
        H1 = 2 * p1 * (1 - p1)
        H2 = 2 * p2 * (1 - p2)
        HS = (H1 + H2) / 2
        
        st.markdown(f"""
        **Step 4:** Calculate average within-population heterozygosity (HS)
        ```
        H₁ = 2 × p₁ × (1 - p₁) = 2 × {p1} × {1-p1} = {H1:.4f}
        H₂ = 2 × p₂ × (1 - p₂) = 2 × {p2} × {1-p2} = {H2:.4f}
        HS = (H₁ + H₂) / 2 = {HS:.4f}
        ```
        """)
        
        # Step 5: FST
        fst = (HT - HS) / HT if HT > 0 else 0
        
        st.markdown(f"""
        **Step 5:** Calculate FST
        ```
        FST = (HT - HS) / HT
        FST = ({HT:.4f} - {HS:.4f}) / {HT:.4f}
        FST = {fst:.4f}
        ```
        """)
        
        # Alternative formula (variance method)
        fst_var = var_p / (p_avg * (1 - p_avg)) if p_avg * (1 - p_avg) > 0 else 0
        
        st.markdown(f"""
        **Alternative (Variance Method):**
        ```
        FST = Var(p) / [p̄(1 - p̄)]
        FST = {var_p:.4f} / [{p_avg:.3f} × {1-p_avg:.3f}]
        FST = {fst_var:.4f}
        ```
        *(Both methods give same result!)*
        """)
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot 1: Allele frequencies
        pops = ['Population 1', 'Population 2']
        freqs_A = [p1, p2]
        freqs_a = [1-p1, 1-p2]
        
        x = np.arange(len(pops))
        width = 0.35
        
        ax1.bar(x - width/2, freqs_A, width, label='Allele A', color='#3b82f6')
        ax1.bar(x + width/2, freqs_a, width, label='Allele a', color='#f97316')
        
        ax1.set_ylabel('Frequency', fontsize=12)
        ax1.set_title('Allele Frequencies', fontsize=14)
        ax1.set_xticks(x)
        ax1.set_xticks(x)
        ax1.set_xticklabels(pops)
        ax1.legend()
        ax1.set_ylim(0, 1)
        ax1.grid(axis='y', alpha=0.3)
        
        # Plot 2: FST interpretation
        fst_scale = [0, 0.05, 0.15, 0.25, 1.0]
        labels = ['No\nDiff', 'Little', 'Moderate', 'Great', 'Fixed']
        colors_scale = ['#22c55e', '#eab308', '#f97316', '#ef4444', '#7f1d1d']
        
        ax2.barh(range(len(fst_scale)-1), 
                 [fst_scale[i+1] - fst_scale[i] for i in range(len(fst_scale)-1)],
                 left=fst_scale[:-1],
                 color=colors_scale[:-1],
                 alpha=0.6,
                 edgecolor='black')
        
        ax2.axvline(x=fst, color='blue', linewidth=3, label=f'Your FST = {fst:.3f}')
        ax2.set_xlabel('FST Value', fontsize=12)
        ax2.set_title('FST Interpretation Scale', fontsize=14)
        ax2.set_xlim(0, 0.5)
        ax2.legend()
        ax2.grid(axis='x', alpha=0.3)
        
        for i, label in enumerate(labels[:-1]):
            ax2.text((fst_scale[i] + fst_scale[i+1])/2, 0, label,
                    ha='center', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Conservation interpretation
        st.success(f"""
        ### 🦎 Conservation Interpretation:
        
        **FST = {fst:.3f}**
        
        {
        '''
        **No differentiation:** Populations are genetically similar.
        - Management: Can be managed as single unit
        - Conservation: Gene flow likely occurring
        - Action: No special measures needed for genetic distinctiveness
        ''' if fst < 0.05 else
        '''
        **Little differentiation:** Populations slightly different but connected.
        - Management: Consider as single unit with monitoring
        - Conservation: Some gene flow, maintain connectivity
        - Action: Preserve migration corridors
        ''' if fst < 0.15 else
        '''
        **Moderate differentiation:** Populations are clearly distinct.
        - Management: Treat as separate management units
        - Conservation: Limited gene flow, local adaptation possible
        - Action: Maintain both populations, don't mix stocks
        ''' if fst < 0.25 else
        '''
        **Great differentiation:** Populations very different.
        - Management: Separate conservation units essential
        - Conservation: No gene flow, likely locally adapted
        - Action: Preserve each population independently
        '''
        }
        """)
    
    # TAB 4: MIGRATION-FST BALANCE
    with tabs[3]:
        st.markdown("## 🎮 Interactive: Drift-Migration Balance")
        
        st.markdown("""
        ### The One Migrant Rule
        
        **Key insight:** Just ONE migrant per generation is enough to prevent 
        population differentiation due to drift!
        
        **Formula:**
        ```
        FST ≈ 1 / (4Nem + 1)
        
        Where:
        Ne = Effective population size
        m = Migration rate (proportion of migrants per generation)
        ```
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            Ne_balance = st.slider(
                "Effective Population Size (Ne)",
                min_value=50,
                max_value=1000,
                value=200,
                step=50
            )
        
        with col2:
            # Calculate Nem instead of m directly
            Nem = st.slider(
                "Number of Migrants (Nem)",
                min_value=0.0,
                max_value=10.0,
                value=1.0,
                step=0.1,
                help="Nem = Ne × m"
            )
        
        # Calculate FST
        fst_predicted = 1 / (4 * Nem + 1) if Nem > 0 else 1.0
        
        # Calculate actual m
        m = Nem / Ne_balance
        
        # Plot FST vs Nem
        Nem_range = np.linspace(0.1, 10, 100)
        fst_range = 1 / (4 * Nem_range + 1)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(Nem_range, fst_range, 'b-', linewidth=2, label='Predicted FST')
        ax.axvline(x=1, color='r', linestyle='--', linewidth=2, 
                   label='Nem = 1 (One migrant rule)')
        ax.axvline(x=Nem, color='g', linestyle='--', alpha=0.7, 
                   label=f'Current Nem = {Nem}')
        ax.axhline(y=fst_predicted, color='g', linestyle=':', alpha=0.5)
        
        ax.set_xlabel('Number of Migrants per Generation (Nem)', fontsize=12)
        ax.set_ylabel('Expected FST', fontsize=12)
        ax.set_title('Drift-Migration Balance', fontsize=14)
        ax.legend()
        ax.grid(alpha=0.3)
        ax.set_ylim(0, 0.5)
        
        st.pyplot(fig)
        
        st.success(f"""
        ### 📊 Results:
        - **Effective population size (Ne):** {Ne_balance}
        - **Number of migrants (Nem):** {Nem}
        - **Migration rate (m):** {m:.4f} ({m*100:.2f}%)
        - **Expected FST:** {fst_predicted:.4f}
        
        **Interpretation:**
        {
        f"With {Nem} migrant(s) per generation, FST is LOW ({fst_predicted:.3f}). "
        "Populations remain genetically connected!" if Nem >= 1 else
        f"With less than 1 migrant per generation, FST is MODERATE-HIGH ({fst_predicted:.3f}). "
        "Drift dominates, populations diverge!"
        }
        
        **Conservation message:** Even small amounts of gene flow (1 individual per 
        generation) can prevent genetic differentiation!
        """)
    
    # TAB 5: PRACTICE PROBLEMS
    with tabs[4]:
        st.markdown("## 📝 Practice Problems")
        
        st.markdown("""
        ### Problem 1: Basic FST Calculation
        
        Two Labeo rohita populations show these allele frequencies at a microsatellite locus:
        - Population A (Mahanadi): Frequency of allele 1 = 0.65
        - Population B (Ganga): Frequency of allele 1 = 0.45
        
        **Calculate FST.**
        """)
        
        with st.expander("💡 See Solution"):
            st.markdown("""
            **Step 1:** Calculate average frequency  
            p̄ = (0.65 + 0.45) / 2 = 0.55
            
            **Step 2:** Calculate variance  
            Var(p) = [(0.65 - 0.55)² + (0.45 - 0.55)²] / 2  
            Var(p) = [0.01 + 0.01] / 2 = 0.01
            
            **Step 3:** Calculate FST  
            FST = Var(p) / [p̄(1 - p̄)]  
            FST = 0.01 / [0.55 × 0.45]  
            FST = 0.01 / 0.2475  
            **FST ≈ 0.040**
            
            **Interpretation:** Little differentiation (FST < 0.05). Populations are 
            connected by gene flow.
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ### Problem 2: Conservation Application
        
        You're studying three Labeo rohita populations:
        - Population 1 vs 2: FST = 0.08
        - Population 1 vs 3: FST = 0.18
        - Population 2 vs 3: FST = 0.22
        
        **How many conservation units should you designate?**
        """)
        
        with st.expander("💡 See Solution"):
            st.markdown("""
            **Analysis:**
            - Pop 1 vs 2: FST = 0.08 (Little-Moderate differentiation)
            - Pop 1 vs 3: FST = 0.18 (Moderate-Great differentiation)
            - Pop 2 vs 3: FST = 0.22 (Great differentiation)
            
            **Interpretation:**
            - Populations 1 and 2 are somewhat similar (can be grouped)
            - Population 3 is very different from both (separate unit)
            
            **Recommendation:**
            **TWO conservation units:**
            1. Unit A: Populations 1 and 2 combined
            2. Unit B: Population 3 alone
            
            **Management:** Don't transfer fish between these units. Maintain genetic 
            distinctiveness. Population 3 may have local adaptations worth preserving.
            """)

# Add to main app.py file where Module 5A section is called
