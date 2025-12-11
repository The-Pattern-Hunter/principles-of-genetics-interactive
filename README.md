# Principles of Genetics Interactive
## From Poisson Distribution to Linkage Disequilibrium - A Comprehensive Educational Resource

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/The-Pattern-Hunter/principles-of-genetics-interactive/HEAD)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17887470.svg)](https://doi.org/10.5281/zenodo.17887470)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **Click the Binder badge above to launch all materials in an interactive environment - no installation required!**

A comprehensive, open educational resource package for teaching genetic mapping and linkage disequilibrium, developed at **Kuchinda College, Sambalpur University, Odisha, India**. Materials range from 9th-grade level explanations to research-level applications, featuring examples from Western Odisha biodiversity.

---

## 🎯 Quick Start

### Option 1: Launch in Binder (Recommended for Full Experience)
Click the **Binder** badge at the top - launches in 1-2 minutes with all materials ready to use.

### Option 2: Launch Individual Notebooks in Google Colab

| Notebook | Topics | Level | Launch |
|----------|--------|-------|--------|
| **1. Poisson & RF Limit** | Distribution patterns, crossovers, 50% limit | Foundational | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/genetic_mapping_poisson.ipynb) |
| **2. Three-Point & Interference** | Gene ordering, COC, mapping functions | Advanced | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/interference_and_coc.ipynb) |
| **3. Linkage vs LD** ✨ NEW | LD concepts, decay, GWAS applications | Advanced+ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/linkage_vs_linkage_disequilibrium.ipynb) |
| **4. Mendelian → Population** ✨ | Statistical bridge, HW equilibrium | Foundational | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/mendelian_to_population_genetics.ipynb) |

---

## 📚 Learning Modules

### Module 1: Poisson Distribution & 50% Recombination Limit
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/genetic_mapping_poisson.ipynb)

**Topics Covered:**
- Poisson distribution as the "shape of uncertainty"
- Why recombination frequency never exceeds 50%
- Two causes of 50% RF (linkage vs independence)
- Interactive crossover simulator
- Gene ordering with Labeo rohita examples
- Practice problems with solutions

**Interactive Features:**
- 🎚️ 5 interactive widgets with sliders
- 📊 Real-time parameter manipulation
- 🎲 Crossover simulation with adjustable sample sizes
- 🐟 Regional species examples

**Duration:** 60-90 minutes  
**Best for:** BSc Zoology students, undergraduate genetics courses

---

### Module 2: Three-Point Crosses & Interference
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/interference_and_coc.ipynb)

**Topics Covered:**
- What is interference and why it occurs
- Eight gamete classes in three-point crosses
- Gene ordering algorithms with step-by-step guidance
- Coefficient of Coincidence (COC) calculations
- Haldane vs Kosambi mapping functions
- Distance-dependent interference patterns

**Interactive Features:**
- 🎚️ 3 interactive sections with real-time calculations
- 🧮 Automatic COC and interference computation
- 📏 Visual comparison of mapping functions
- 🪱 Earthworm and fish genetics applications

**Duration:** 60-90 minutes  
**Best for:** Advanced undergraduates, MSc students, researchers

---

### Module 3: Linkage vs Linkage Disequilibrium ✨ NEW!
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/linkage_vs_linkage_disequilibrium.ipynb)

**Topics Covered:**
- Critical distinction between linkage and linkage disequilibrium
- LD measures: D, D', and r²
- LD decay over generations (with simulator)
- Population genetics scenarios (admixture, selection, drift)
- GWAS applications and SNP proxies
- Haplotype block formation

**Interactive Features:**
- 🎚️ 3 major interactive sections with multiple sliders
- ⏰ LD decay simulator with customizable parameters
- 🧬 Create your own LD scenarios
- 📊 Real-time haplotype frequency calculations
- 🌍 Population genetics scenario explorer

**Why This Matters:**  
Clarifies one of the most confusing concepts in genetics! Students often mix up linkage (physical proximity) with LD (statistical association). This module makes the distinction crystal clear through hands-on exploration.

**Duration:** 60-90 minutes  
**Best for:** Advanced undergraduates, MSc students, population genetics, GWAS researchers

**🎯 Recommended:** Complete Modules 1 & 2 before exploring LD concepts.

---
### Module 4: Mendelian to Population Genetics Bridge ✨ NEW!
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/mendelian_to_population_genetics.ipynb)

**Topics Covered:**
- Transition from individual to population thinking
- How ratios become frequencies
- Hardy-Weinberg equilibrium from first principles
- Population Punnett squares (visual connection!)
- Random mating simulations
- Chi-square goodness of fit testing
- Understanding sampling variation

**Interactive Features:**
- 🎚️ Watch n=1 cross transform into n=1000 population
- 🎲 Simulate random mating in real-time
- 📊 Population Punnett square visualization
- 🧮 Automatic HW predictions and chi-square tests

**Why This Matters:**  
Bridges the conceptual gap that confuses most genetics students! Shows that population genetics is just scaled-up Mendelian genetics with statistical thinking.

**Duration:** 60-90 minutes  
**Best for:** BSc transitioning to population genetics, MSc foundation

**🎯 Recommended:** Complete BEFORE Module 3 (Linkage vs LD) for best understanding.
## 📁 Repository Contents
```
principles-of-genetics-interactive/
│
├── README.md                              (This file)
├── LICENSE                                (CC BY 4.0)
├── requirements.txt                       (Python dependencies)
│
├── notebooks/
│   ├── genetic_mapping_poisson.ipynb      (Module 1: Core concepts)
│   ├── interference_and_coc.ipynb         (Module 2: Advanced topics)
│   └── linkage_vs_linkage_disequilibrium.ipynb  (Module 3: LD concepts) ✨ NEW!
│   └── mendelian_to_population_genetics.ipynb  (Module 4: individual to population thinking) ✨ NEW!
│
├── guides/
│   ├── genetic_mapping_guide.md           (Quick reference)
│   ├── interference_coc_guide.md          (Advanced reference)
│   └── MASTER_INDEX.md                    (Complete package overview)
│
├── visualizations/
│   ├── poisson_crossovers.png             (Distribution visualizations)
│   ├── 50percent_limit.png                (Asymptotic approach)
│   ├── two_point_cross_comparison.png     (Ambiguity demonstration)
│   ├── gene_map_labeo.png                 (Labeo rohita example)
│   ├── gene_map_earthworm.png             (Earthworm example)
│   ├── eight_gamete_classes.png           (Three-point cross guide)
│   ├── interference_comparison.png        (Effects of interference)
│   ├── coc_vs_distance.png               (COC relationships)
│   ├── mapping_functions_comparison.png   (Haldane vs Kosambi)
│   └── earthworm_three_point_data.png    (Real data example)
│
└── articles/
    ├── pedagogy_article_college_magazine.md
    └── academic_paper_national_journal.md
```

---

## 🎓 Who Should Use This?

### For Students:
- **9th Grade+**: Start with "bag switching" analogy and visual explanations
- **BSc Zoology**: Complete Modules 1-2 (required), Module 3 (optional/advanced)
- **MSc/Research**: All three modules for comprehensive understanding
- **Population Genetics**: Focus on Module 3 for LD concepts

### For Teachers:
- Ready-to-use materials for genetics courses
- Adaptable to different levels
- Includes assessment ideas and practice problems
- Regional examples (can substitute your own)

### For Researchers:
- Refresh genetic mapping concepts
- Learn interference calculations
- Understand LD for GWAS interpretation
- Apply to QTL mapping projects
- Use as reference for mapping function choice

---

## 🌟 Key Features

### 1. **Distribution-First Pedagogy**
Rather than memorizing formulas, students understand the **Poisson distribution** that governs crossover events, discovering why RF ≤ 50% emerges naturally from the mathematics.

### 2. **Fully Interactive with Real-Time Manipulation**
All three notebooks feature interactive sliders and widgets:
- Change parameters instantly
- Watch visualizations update in real-time
- Explore "what if" scenarios
- Learn through direct manipulation, not passive reading

### 3. **Regional Biodiversity Examples**
All worked examples use species from Western Odisha:
- **Labeo rohita** (Indian major carp) - microsatellite mapping
- **Earthworms** (Metaphire) - environmental genomics from mining regions
- Connects genetic principles to local research contexts

### 4. **Clarifies Difficult Concepts**
Module 3 specifically addresses the **linkage vs LD confusion** that trips up students worldwide:
- Side-by-side comparisons
- Interactive demonstrations
- Population genetics scenarios
- Shows LD can exist between unlinked genes!

### 5. **Multi-Level Learning**
Same concepts explained at multiple levels:
- Simple analogies for beginners
- Mathematical rigor for advanced students
- Research applications for practitioners

### 6. **Open Access, Maximum Impact**
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
✓ **Differentiate linkage from linkage disequilibrium** ✨  
✓ **Explain how and why LD decays over generations** ✨  

### Skills (Apply & Analyze)
✓ Calculate recombination frequencies from experimental data  
✓ Order genes using three-point cross data  
✓ Draw genetic maps with accurate distances  
✓ Calculate COC and interference values  
✓ Choose appropriate mapping functions for different organisms  
✓ **Measure LD using D, D', and r²** ✨  
✓ **Predict LD decay patterns** ✨  
✓ **Interpret r² values for GWAS** ✨  

### Higher-Order (Evaluate & Create)
✓ Design three-point cross experiments  
✓ Evaluate quality of genetic maps  
✓ Troubleshoot unexpected experimental results  
✓ Apply concepts to new organisms and research questions  
✓ **Distinguish population history from linkage effects** ✨  
✓ **Design GWAS studies with appropriate LD considerations** ✨  

---

## 🚀 Usage Instructions

### For Binder (Easiest):
1. Click the Binder badge at top of this page
2. Wait 1-2 minutes for environment to build
3. Navigate to `notebooks/` folder
4. Open any notebook and start learning!
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
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

**Required packages:** numpy, matplotlib, scipy, pandas, seaborn, ipywidgets  
**Python version:** 3.7+

---

## 💡 Pedagogical Approach: Pattern Hunters Philosophy

These materials embody the **Pattern Hunters** educational philosophy:

1. **"Uncertainty has shape"** → Distributions aren't chaos; they have predictable structures
2. **"Shape creates constraints"** → Mathematical properties → biological laws (50% RF limit)
3. **"Reality modifies theory"** → Interference adjusts pure Poisson expectations
4. **"Strategic design resolves ambiguity"** → Three-point crosses distinguish linkage from independence
5. **"Physical vs Statistical"** → Linkage is location, LD is association (Module 3) ✨
6. **"Local examples illuminate universal principles"** → Western Odisha species follow same genetic laws as any organism

This approach moves from **concrete → abstract** and **observation → formalization**, building deep understanding rather than superficial memorization.

---

## 🔬 Applications

### Labeo rohita (Indian Major Carp)
- QTL mapping for growth traits
- Disease resistance markers
- Breeding program optimization
- Population structure analysis

### Earthworm Genomics
- Heavy metal tolerance mapping (mining regions)
- Biomonitoring marker development
- Population adaptation studies
- Environmental genomics

### Linkage Disequilibrium Applications ✨
- GWAS study design and interpretation
- Haplotype block identification
- Population admixture detection
- Selection signature identification
- Imputation accuracy prediction
- Fine-mapping of causal variants

### General Research
- Linkage mapping in any organism
- Marker-assisted selection programs
- QTL analysis
- Genome assembly validation

---

## 📖 Recommended Learning Pathways

### Pathway 1: Complete Beginner (8-10 hours)
1. Read `guides/genetic_mapping_guide.md`
2. Work through Module 1 (Poisson)
3. Try practice problems
4. Complete Module 2 (Interference)
5. Optional: Explore Module 3 (LD)

### Pathway 2: BSc Genetics Student (10-12 hours)
1. Quick review of basic guide
2. Complete Modules 1-2 entirely
3. Solve all practice problems
4. Explore Module 3 basics
5. Focus on interactive features

### Pathway 3: Advanced/MSc (6-8 hours after basics)
1. Quick review of Modules 1-2
2. Deep dive into Module 2 (Interference)
3. Complete Module 3 (LD) thoroughly
4. Compare Haldane vs Kosambi for your organism
5. Apply to your own data

### Pathway 4: Population Genetics Focus (4-6 hours with genetics background)
1. Skim Modules 1-2 for review
2. Focus entirely on Module 3 (LD)
3. Explore all population scenarios
4. Apply to GWAS interpretation
5. Connect to your research questions

### Pathway 5: Teacher Preparation (4-5 hours)
1. Review MASTER_INDEX.md
2. Complete all three notebooks
3. Select appropriate sections for your students
4. Preview all visualizations
5. Plan assessment strategy

---

## 🤝 Contributing

We welcome contributions! Ways to help:

### Content Contributions:
- Additional organism examples
- Practice problems and solutions
- Translations to other languages
- Corrections and improvements
- Additional LD scenarios

### Technical Contributions:
- Bug fixes
- Code optimization
- New visualizations
- Documentation improvements
- Interactive widget enhancements

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
  title = {Principles of Genetics Interactive: From Poisson Distribution to Linkage Disequilibrium},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive}},
  doi = {10.5281/zenodo.17887470},
  note = {Educational materials for genetic mapping, Kuchinda College, Sambalpur University}
}
```

### APA:
> Kar, S., & Patel, A. (2025). *Principles of genetics interactive: From Poisson distribution to linkage disequilibrium* [Educational software]. Zenodo. https://doi.org/10.5281/zenodo.17887470

### Plain Text:
> Kar, S., & Patel, A. (2025). Principles of Genetics Interactive. DOI: 10.5281/zenodo.17887470

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
Teaching: BSc 5th Semester Genetics  
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
- Interactive exploration
- Open access philosophy

**Vision**: Demonstrate that educational excellence emerges from deep subject expertise and commitment to students, not from institutional prestige or urban location.

---

## 🌍 Impact & Usage

### Student Testimonials:
> *"The visualizations make everything clear. I can finally see what's happening during meiosis."* - BSc 3rd year student

> *"Using Labeo rohita examples makes it feel relevant. This isn't just foreign textbook genetics."* - BSc 2nd year student

> *"I showed the interactive notebook to my cousin at an IIT. He said their genetics course doesn't have anything like this!"* - BSc 3rd year student

> *"The LD notebook finally made me understand the difference between linkage and LD. I've been confused about this for two years!"* - MSc 1st year student ✨

### Adoption:
If you use these materials, please let us know! We're tracking:
- Institutions using materials
- Number of students reached
- Adaptations and improvements
- Translation efforts

Email: aloksu@gmail.com

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
- [Zenodo DOI Record](https://doi.org/10.5281/zenodo.17887470)

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

**Q: What's the difference between linkage and LD?** ✨  
A: That's exactly what Module 3 explains! Linkage = physical location, LD = statistical association.

**Q: Do the interactive sliders work in both Binder and Colab?** ✨  
A: Yes! They work in both environments. Colab is usually faster to load.

---

## 🎯 Roadmap

### Completed ✅
- Core genetic mapping notebook (Module 1)
- Advanced interference notebook (Module 2)
- Linkage Disequilibrium notebook (Module 3) ✨ NEW!
- 10 high-resolution visualizations
- Comprehensive guides
- Academic publications drafted
- Zenodo DOI: 10.5281/zenodo.17887470
- Interactive widgets with real-time manipulation

### In Progress 🔄
- Additional practice problem sets
- Video tutorials (English, Odia, Hindi)

### Planned 📋
- Interactive assessments with auto-grading
- Additional organism examples
- Four-point cross analysis
- QTL mapping extension module
- Haplotype block visualization tool
- Integration with other Pattern Hunters modules
- Multilingual support

---

## 💬 Feedback & Contact

We value your feedback! Contact us:

**General Questions**: aloksu@gmail.com  
**Teaching Implementation**: susama.kar@kuchindacollege.ac.in  
**Technical Issues**: [Open an issue](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive/issues)  
**Collaboration**: Email either author

---

## 🙏 Acknowledgments

- BSc Zoology students at Kuchinda College for feedback and enthusiasm
- Department of Zoology colleagues for support
- Sambalpur University for academic environment
- Open-source community for tools (Python, Jupyter, NumPy, Matplotlib, ipywidgets)
- Western Odisha biodiversity for endless examples
- National Education Policy 2020 for emphasizing OER and equity
- GitHub and Zenodo for hosting and archiving

---

## 📈 Statistics

![GitHub stars](https://img.shields.io/github/stars/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)
![GitHub forks](https://img.shields.io/github/forks/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)

**Impact Metrics** (will be updated regularly):
- 🎓 Students reached: [To be tracked]
- 🏛️ Institutions using: [To be tracked]
- 🌍 Countries: [To be tracked]
- 📥 Downloads from Zenodo: [Auto-tracked via DOI]

---

**⭐ If you find this useful, please star the repository! ⭐**

**🔄 Share with colleagues, students, and fellow educators! 🔄**

---

*Developed with ❤️ at Kuchinda College, Odisha, India*  
*Part of the Pattern Hunters Educational Series*  
*Making world-class mathematical biology education accessible to all*

---

**Last Updated**: December 2025  
**Version**: 1.1 ✨  
**Status**: Active Development & Teaching Use  
**DOI**: 10.5281/zenodo.17887470
