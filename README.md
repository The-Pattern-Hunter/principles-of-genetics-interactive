# Principles of Genetics Interactive
## From Mendelian Genetics to Population Genomics - A Comprehensive Educational Resource

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/The-Pattern-Hunter/principles-of-genetics-interactive/HEAD)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17887470.svg)](https://doi.org/10.5281/zenodo.17887470)

> **Click the Binder badge above to launch all materials in an interactive environment - no installation required!**

A comprehensive, open educational resource package for teaching genetics from Mendelian principles to population genomics, developed at **Kuchinda College, Sambalpur University, Odisha, India**. Materials range from 9th-grade level explanations to research-level applications, featuring interactive simulations and examples from Indian biodiversity.

---

## 🎯 Quick Start

### Option 1: Launch in Binder (Recommended for Full Experience)
Click the **Binder** badge at the top - launches in 1-2 minutes with all materials ready to use.

### Option 2: Launch Individual Notebooks in Google Colab

#### 📓 Core Notebook: Poisson Distribution and Basic Mapping
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/genetic_mapping_poisson.ipynb)

**Topics Covered:**
- Poisson distribution as the "shape of uncertainty"
- Why recombination frequency never exceeds 50%
- Two causes of 50% RF (linkage vs independence)
- Two-point and three-point crosses
- Gene ordering algorithms with step-by-step examples
- Practice problems with solutions

**Best for:** BSc Zoology students, undergraduate genetics courses

---

#### 📓 Advanced Notebook: Interference and Coefficient of Coincidence
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/interference_and_coc.ipynb)

**Topics Covered:**
- What is interference and why it occurs
- Eight gamete classes in three-point crosses
- Coefficient of Coincidence (COC) calculations
- Haldane vs Kosambi mapping functions
- Distance-dependent interference patterns
- Applications to fish and earthworm genetics

**Best for:** Advanced undergraduates, MSc students, researchers

---

#### 📓 Linkage vs Linkage Disequilibrium - Clearing the Confusion
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/linkage_vs_ld.ipynb)

**Topics Covered:**
- Clear distinction between linkage and LD
- Physical connection vs statistical association
- How LD decays over generations
- When to use which concept
- Applications to GWAS and association mapping
- Foundation for population genomics

**Best for:** BSc to MSc students, anyone transitioning to modern genetics

---

#### 📓 From Mendelian to Population Genetics - The Conceptual Bridge
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/mendelian_to_population.ipynb)

**Topics Covered:**
- Individual to population thinking
- Hardy-Weinberg equilibrium
- Allele and genotype frequency calculations
- Transition from pedigrees to populations
- Foundation for Module 5 series

**Best for:** BSc to MSc students, bridging classical and population genetics

---

#### 📓 Population Genomics: FST and Population Structure ✨ NEW
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/5a_fst_population_structure.ipynb)

**Topics Covered:**
- Population differentiation and genetic structure
- FST calculation and interpretation
- Variance partitioning (HT vs HS)
- Drift-migration balance (the "one migrant" rule)
- Real examples: Indian human populations, Labeo rohita, cattle breeds
- Conservation genetics applications
- FST outliers for selection detection

**Best for:** MSc students, population genetics courses, conservation biology

---

#### 📓 Selection Signatures - Detecting Adaptive Evolution ✨ NEW
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/5b_selection_signatures.ipynb)

**Topics Covered:**
- Kimura's neutral theory as null hypothesis
- Site frequency spectrum (SFS) under different scenarios
- Tajima's D calculation and interpretation
- FST outliers, iHS, dN/dS methods
- Real examples: Lactase persistence, malaria resistance in India
- Selection detection in aquaculture species

**Best for:** MSc students, evolutionary biology, molecular evolution

---

#### 📓 Effective Population Size (Ne) - Genetic Bottlenecks ✨ NEW
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/5c_effective_population_size.ipynb)

**Topics Covered:**
- Why Ne < census size (N)
- Factors reducing Ne (sex ratio, reproductive variance)
- Ne estimation methods (LD, temporal, heterozygosity)
- The 50/500 rule for conservation
- Real applications to Labeo rohita management
- Bottleneck detection and conservation decisions

**Best for:** Conservation biology, wildlife management, aquaculture

---

## 📚 Contents

```
principles-of-genetics-interactive/
│
├── README.md                                     (This file)
├── LICENSE                                       (CC BY 4.0)
│
├── notebooks/
│   ├── genetic_mapping_poisson.ipynb             (Module 1: Core concepts)
│   ├── interference_and_coc.ipynb                (Module 2: Advanced mapping)
│   ├── linkage_vs_ld.ipynb                       (Module 3: LD concepts)
│   ├── mendelian_to_population.ipynb             (Module 4: Conceptual bridge)
│   ├── 5a_fst_population_structure.ipynb         (Module 5A: FST) ✨ NEW
│   ├── 5b_selection_signatures.ipynb             (Module 5B: Selection) ✨ NEW
│   └── 5c_effective_population_size.ipynb        (Module 5C: Ne) ✨ NEW
│
├── guides/
│   ├── genetic_mapping_guide.md                  (Quick reference)
│   ├── interference_coc_guide.md                 (Advanced reference)
│   └── MASTER_INDEX.md                           (Complete package overview)
│
├── visualizations/
│   ├── poisson_crossovers.png                    (Distribution visualizations)
│   ├── 50percent_limit.png                       (Asymptotic approach)
│   ├── two_point_cross_comparison.png            (Ambiguity demonstration)
│   ├── gene_map_labeo.png                        (Labeo rohita example)
│   ├── gene_map_earthworm.png                    (Earthworm example)
│   ├── eight_gamete_classes.png                  (Three-point cross guide)
│   ├── interference_comparison.png               (Effects of interference)
│   ├── coc_vs_distance.png                       (COC relationships)
│   ├── mapping_functions_comparison.png          (Haldane vs Kosambi)
│   └── earthworm_three_point_data.png           (Real data example)
│
└── articles/
    ├── pedagogy_article_college_magazine.md
    └── academic_paper_national_journal.md
```

---

## 🎓 Who Should Use This?

### For Students:
- **9th Grade+**: Start with "bag switching" analogy and visual explanations
- **BSc Zoology**: Complete both notebooks for comprehensive understanding
- **MSc/Research**: Focus on advanced notebook and real data applications

### For Teachers:
- Ready-to-use materials for genetics courses
- Adaptable to different levels
- Includes assessment ideas and practice problems
- Regional examples (can substitute your own)

### For Researchers:
- Refresh genetic mapping concepts
- Learn interference calculations
- Apply to QTL mapping projects
- Use as reference for mapping function choice

---

## 🌟 Key Features

### 1. **Distribution-First Pedagogy**
Rather than memorizing formulas, students understand the **Poisson distribution** that governs crossover events, discovering why RF ≤ 50% emerges naturally from the mathematics.

### 2. **Regional Biodiversity Examples**
All worked examples use species from Western Odisha:
- **Labeo rohita** (Indian major carp) - microsatellite mapping
- **Earthworms** (Metaphire) - environmental genomics from mining regions
- Connects genetic principles to local research contexts

### 3. **Multi-Level Learning**
Same concepts explained at multiple levels:
- Simple analogies for beginners
- Mathematical rigor for advanced students
- Research applications for practitioners

### 4. **Interactive Exploration**
Jupyter notebooks allow students to:
- Modify parameters and see results change
- Run simulations with different scenarios
- Generate their own practice problems
- Learn by doing, not just reading

### 5. **Open Access, Maximum Impact**
All materials are free, forever:
- No textbook costs
- No software licenses
- Customizable for your context
- Contribute improvements back

---

## 📊 Learning Outcomes

By completing these materials, students will be able to:

### Knowledge (Remember & Understand)
✓ Explain why recombination frequency cannot exceed 50%  
✓ Describe the role of Poisson distribution in genetic mapping  
✓ Define interference and coefficient of coincidence  
✓ Distinguish between Haldane and Kosambi mapping functions  
✓ Explain what FST measures and how it's calculated ✨  
✓ Understand the drift-migration balance in populations ✨  
✓ Describe Kimura's neutral theory and its importance ✨  
✓ Explain why Ne < census size ✨  

### Skills (Apply & Analyze)
✓ Calculate recombination frequencies from experimental data  
✓ Order genes using three-point cross data  
✓ Draw genetic maps with accurate distances  
✓ Calculate COC and interference values  
✓ Choose appropriate mapping functions for different organisms  
✓ Calculate FST from allele frequency data ✨  
✓ Interpret FST values for conservation decisions ✨  
✓ Calculate and interpret Tajima's D ✨  
✓ Estimate Ne using genetic data ✨  

### Higher-Order (Evaluate & Create)
✓ Design three-point cross experiments  
✓ Evaluate quality of genetic maps  
✓ Troubleshoot unexpected experimental results  
✓ Apply concepts to new organisms and research questions  
✓ Design conservation strategies using population structure data ✨  
✓ Detect selection signatures using multiple methods ✨  
✓ Assess population viability using Ne estimates ✨  

---

## 🚀 Usage Instructions

### For Binder (Easiest):
1. Click the Binder badge at top of this page
2. Wait 1-2 minutes for environment to build
3. Navigate to `notebooks/` folder
4. Open either notebook and start learning!
5. Run cells sequentially (Shift+Enter)

### For Google Colab:
1. Click the Colab badge for desired notebook
2. Sign in with Google account
3. Run cells sequentially
4. Save your own copy to Google Drive if desired

### For Local Installation:
```bash
# Clone the repository
git clone https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive.git
cd principles-of-genetics-interactive

# Install dependencies
pip install numpy matplotlib scipy pandas jupyter

# Launch Jupyter
jupyter notebook
```

**Required packages:** numpy, matplotlib, scipy, pandas  
**Python version:** 3.7+

---

## 💡 Pedagogical Approach: Pattern Hunters Philosophy

These materials embody the **Pattern Hunters** educational philosophy:

1. **"Uncertainty has shape"** → Distributions aren't chaos; they have predictable structures
2. **"Shape creates constraints"** → Mathematical properties → biological laws (50% RF limit)
3. **"Reality modifies theory"** → Interference adjusts pure Poisson expectations
4. **"Strategic design resolves ambiguity"** → Three-point crosses distinguish linkage from independence
5. **"Local examples illuminate universal principles"** → Western Odisha species follow same genetic laws as any organism
6. **"Population structure emerges from process"** → FST reflects balance between drift and migration ✨

This approach moves from **concrete → abstract** and **observation → formalization**, building deep understanding rather than superficial memorization.

---

## 🔬 Applications

### Labeo rohita (Indian Major Carp)
- QTL mapping for growth traits
- Disease resistance markers
- Breeding program optimization
- Population structure analysis
- FST-based conservation management ✨
- Gene flow assessment across river basins ✨

### Earthworm Genomics
- Heavy metal tolerance mapping (mining regions)
- Biomonitoring marker development
- Population adaptation studies
- Environmental genomics
- Selection signatures in pollution-adapted populations ✨

### Human Population Genetics ✨
- Indian population structure (ANI-ASI components)
- Ancestry inference and forensics
- GWAS population structure correction
- Migration pattern reconstruction
- Tribal vs non-tribal differentiation

### General Research
- Linkage mapping in any organism
- Marker-assisted selection programs
- QTL analysis
- Genome assembly validation
- Conservation genetics decision-making ✨
- Local adaptation detection ✨

---

## 📖 Recommended Learning Pathways

### Pathway 1: Complete Beginner (6-8 hours)
1. Read `guides/genetic_mapping_guide.md`
2. Complete core notebook (genetic_mapping_poisson.ipynb)
3. Practice problems from guide
4. Review visualizations to reinforce concepts

### Pathway 2: Advanced Student (8-10 hours)
1. Core notebook (quick review if familiar)
2. Advanced notebook (interference_and_coc.ipynb)
3. Read academic paper draft
4. Work through earthworm and fish examples

### Pathway 3: Instructor Preparation (4-6 hours)
1. Review MASTER_INDEX.md
2. Explore both notebooks interactively
3. Read pedagogy article
4. Adapt visualizations for your context
5. Review Module 5A for population genetics extension ✨

### Pathway 4: Population Genomics Focus (6-8 hours) ✨ NEW
1. Quick review: Modules 1-2 (mapping concepts)
2. Module 3: Linkage vs LD (conceptual foundation)
3. Module 4: Mendelian to Population bridge (transition)
4. Module 5A: FST and population structure (differentiation)
5. Module 5B: Selection signatures (detecting adaptation)
6. Module 5C: Effective population size (conservation)
7. Apply to conservation or GWAS research questions

### Pathway 5: Research Application (2-3 hours)
1. Jump to relevant notebook section
2. Use as reference for your mapping project
3. Check mapping function recommendations
4. Apply population structure concepts to your data ✨
2. Work through core notebook sections 1-3
3. Try practice problems from guide
4. Review visualizations
5. Complete notebook sections 4-6

### Pathway 2: BSc Genetics Student (8-10 hours)
1. Quick review of basic guide
2. Complete core notebook entirely
3. Solve all practice problems
4. Optional: Start advanced notebook

### Pathway 3: Advanced/Research (4-6 hours after basics)
1. Skim core notebook for review
2. Deep dive into interference notebook
3. Compare Haldane vs Kosambi for your organism
4. Apply to your own data

### Pathway 4: Teacher Preparation (3-4 hours)
1. Review MASTER_INDEX.md
2. Select appropriate sections for your students
3. Preview all visualizations
4. Plan assessment strategy

---

## 🤝 Contributing

We welcome contributions! Ways to help:

### Content Contributions:
- Additional organism examples
- Practice problems and solutions
- Translations to other languages
- Corrections and improvements

### Technical Contributions:
- Bug fixes
- Code optimization
- New visualizations
- Documentation improvements

**How to contribute:**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
5. We'll review and merge!

---

## 📜 Citation

If you use these materials in teaching, research, or publications:

### BibTeX:
```bibtex
@misc{kar2025genetics,
  author = {Kar, Susama and Patel, Alok},
  title = {Principles of Genetics Interactive: From Poisson Distribution to Interference},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive}},
  note = {Educational materials for genetic mapping, Kuchinda College, Sambalpur University}
}
```

### APA:
> Kar, S., & Patel, A. (2025). *Principles of genetics interactive: From Poisson distribution to interference* [Educational software]. GitHub. https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive

### For Academic Papers:
After Zenodo archiving, cite with DOI for formal publications.

---

## 📄 License

This work is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

**You are free to:**
- **Share** — copy and redistribute in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made

See [LICENSE](LICENSE) file for full text.

---

## 👥 About the Authors

**Susama Kar**  
Lecturer in Zoology, Kuchinda College  
Department of Zoology, Kuchinda College (affiliated to Sambalpur University)  
Email: susama.kar@kuchindacollege.ac.in

**Dr. Alok Patel**  
Head, Department of Zoology, Kuchinda College  
Research: Population genetics, molecular markers, environmental genomics  
Pattern Hunters Series Developer  
Email: aloksu@gmail.com

---

## 🏛️ Institutional Context

### Kuchinda College
- **Location**: Kuchinda, Sambalpur District, Odisha, India
- **Affiliation**: Sambalpur University
- **Context**: Serving rural students in Western Odisha
- **Mission**: Providing world-class education regardless of geography

### Pattern Hunters Initiative
These materials are part of the larger **Pattern Hunters** educational series, which aims to teach statistical concepts and mathematical biology through:
- Regional examples (Western Odisha biodiversity)
- Distribution-first pedagogy
- Multiple difficulty levels
- Open access philosophy

**Vision**: Demonstrate that educational excellence emerges from deep subject expertise and commitment to students, not from institutional prestige or urban location.

---

## 🌍 Impact & Usage

### Student Testimonials:
> *"The visualizations make everything clear. I can finally see what's happening during meiosis."* - BSc 3rd year student

> *"Using Labeo rohita examples makes it feel relevant. This isn't just foreign textbook genetics."* - BSc 2nd year student

> *"I showed the interactive notebook to my cousin at an IIT. He said their genetics course doesn't have anything like this!"* - BSc 3rd year student

### Adoption:
If you use these materials, please let us know! We're tracking:
- Institutions using materials
- Number of students reached
- Adaptations and improvements
- Translation efforts

Email: alok.patel@kuchindacollege.ac.in

---

## 🔗 Related Resources

### Pattern Hunters Series:
- *Principles of Genetics Interactive* (this repository)
- Additional modules in development:
  - Ecological distributions
  - Population dynamics
  - Enzyme kinetics
  - Epidemiological models

### Academic Publications:
- Pedagogy article: *University News* (forthcoming)
- Research paper: Submitted to *Journal of Indian Education*
- Conference presentations: Planned for 2025

### External Links:
- [National Education Policy 2020](https://www.education.gov.in/nep)
- [Open Educational Resources (UNESCO)](https://www.unesco.org/en/open-educational-resources)
- [Sambalpur University](https://www.suniv.ac.in/)

---

## ❓ FAQ

**Q: Do I need programming experience?**  
A: No! Notebooks are designed for complete beginners. Just click and run.

**Q: Can I use this for my own course?**  
A: Absolutely! That's why it's open. Adapt as needed for your context.

**Q: Can I modify the materials?**  
A: Yes! CC BY 4.0 license allows adaptation. Just give attribution.

**Q: What if I find an error?**  
A: Please open an issue or submit a pull request. We appreciate corrections!

**Q: Can I translate to my language?**  
A: Yes! We'd love translations. Contact us to coordinate.

**Q: Is this only for Indian students?**  
A: No! The concepts are universal. Regional examples can be substituted.

**Q: How do I get help if stuck?**  
A: Open an issue on GitHub, or email authors directly.

**Q: Can I use these for commercial training?**  
A: Yes, CC BY 4.0 allows commercial use with attribution.

**Q: Do I need all modules or can I pick and choose?** ✨  
A: Pick what you need! Modules 1-2 for mapping, Modules 3-5 for population genetics.

**Q: Is Module 5A suitable for undergraduates?** ✨  
A: Yes! It's designed with three levels (9th grade → BSc → MSc/Research).

---

## 🎯 Roadmap

### Completed ✅
- Core genetic mapping notebook (Module 1)
- Advanced interference notebook (Module 2)
- Linkage vs LD notebook (Module 3)
- Mendelian to Population bridge (Module 4)
- **Complete Module 5 series - Population Genomics:** ✨ NEW
  - 5A: FST and population structure
  - 5B: Selection signatures (neutral theory, Tajima's D)
  - 5C: Effective population size (Ne estimation)
- 10 high-resolution visualizations
- Comprehensive guides
- Academic publications drafted
- USB offline package

### In Progress 🔄
- Video tutorials
- Translation to Odia and Hindi
- Additional practice problem sets
- Quick reference guides for Module 5

### Planned 📋
- Interactive assessments with auto-grading
- Additional organism examples
- Four-point cross analysis
- QTL mapping extension module
- Integration with genomic data analysis tools
- Advanced selection methods (XP-EHH, PBS)

---

## 💬 Feedback & Contact

We value your feedback! Contact us:

**General Questions**: alok.patel@kuchindacollege.ac.in  
**Teaching Implementation**: susama.kar@kuchindacollege.ac.in  
**Technical Issues**: [Open an issue](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive/issues)  
**Collaboration**: Email either author

---

## 🙏 Acknowledgments

- BSc Zoology students at Kuchinda College for feedback and enthusiasm
- Department of Zoology colleagues for support
- Sambalpur University for academic environment
- Open-source community for tools (Python, Jupyter, NumPy, Matplotlib)
- Western Odisha biodiversity for endless examples
- National Education Policy 2020 for emphasizing OER and equity

---

## 📈 Statistics

![GitHub stars](https://img.shields.io/github/stars/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)
![GitHub forks](https://img.shields.io/github/forks/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)

**Impact Metrics** (will be updated regularly):
- 🎓 Students reached: [To be tracked]
- 🏛️ Institutions using: [To be tracked]
- 🌍 Countries: [To be tracked]
- 📥 Downloads: [Auto-updated via GitHub]

---

**⭐ If you find this useful, please star the repository! ⭐**

**🔄 Share with colleagues, students, and fellow educators! 🔄**

---

*Developed with ❤️ at Kuchinda College, Odisha, India*  
*Part of the Pattern Hunters Educational Series*  
*Making world-class genetics education accessible to all*

---

**Last Updated**: December 2025  
**Version**: 1.1 (Population Genomics Edition)  
**Status**: Active Development & Teaching Use
