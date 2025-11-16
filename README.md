# Principles of Genetics: Interactive Notebooks 🧬

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/The-Pattern-Hunter/principles-of-genetics-interactive/HEAD?labpath=notebooks)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Interactive visualizations and simulations to bridge the gap between Mendelian genetics and population genetics**

---

## 🎯 Overview

These Jupyter notebooks provide **hands-on, interactive learning experiences** for undergraduate and graduate students studying genetics. Each notebook uses Python visualizations and interactive widgets to make complex genetic concepts intuitive and engaging.

### **Why These Notebooks?**

Traditional genetics education often creates an artificial divide between:
- **Family-level (Mendelian) genetics** - Punnett squares, inheritance patterns
- **Population-level genetics** - Hardy-Weinberg, allele frequencies, evolution

These notebooks show that **it's all the same mechanism operating at different scales!**

---

## 📚 Notebooks

### 1. **From Family to Population Bridge** 🌉
**File:** `family_to_population_bridge.ipynb`

[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/The-Pattern-Hunter/principles-of-genetics-interactive/HEAD?labpath=notebooks/family_to_population_bridge.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/family_to_population_bridge.ipynb)

**Learning Objectives:**
- Understand how population patterns emerge from individual Mendelian inheritance
- Visualize the transition from family crosses to population-level allele frequencies
- Explore Hardy-Weinberg equilibrium through simulation
- See how natural selection changes allele frequencies over generations

**Key Features:**
- Interactive Punnett square visualization
- Zoom-out simulation: from 1 family to 10,000 families
- Real-time Hardy-Weinberg calculations
- Multi-generational evolution simulator with selection

**Perfect for:** Understanding the conceptual bridge between classical and population genetics

---

### 2. **Linkage vs Linkage Disequilibrium** 🔗
**File:** `linkage_vs_LD_tutorial.ipynb`

[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/The-Pattern-Hunter/principles-of-genetics-interactive/HEAD?labpath=notebooks/linkage_vs_LD_tutorial.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/linkage_vs_LD_tutorial.ipynb)

**Learning Objectives:**
- Distinguish between **linkage** (physical proximity) and **linkage disequilibrium** (allelic association)
- Visualize LD decay over generations
- Understand factors affecting LD persistence
- Apply concepts to GWAS and evolutionary genetics

**Key Features:**
- Side-by-side comparison of linkage and LD
- Interactive LD decay simulation
- D' and r² calculation and visualization
- Real-world applications in genetics research

**Perfect for:** Graduate students and researchers working with genomic data

---

### 3. **Interactive Linkage Mapping** 🗺️
**File:** `linkage_mapping_interactive.ipynb`

[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/The-Pattern-Hunter/principles-of-genetics-interactive/HEAD?labpath=notebooks/linkage_mapping_interactive.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/The-Pattern-Hunter/principles-of-genetics-interactive/blob/main/notebooks/linkage_mapping_interactive.ipynb)

**Learning Objectives:**
- Calculate recombination frequencies and map distances
- Perform two-point cross analysis
- Determine gene order using three-point crosses
- Visualize crossover events and chromosomal arrangements

**Key Features:**
- Interactive two-point cross calculator
- Three-point cross gene order determination
- Chromosome map visualization
- Double crossover detection and correction

**Perfect for:** Classical genetics courses covering genetic mapping

---

## 🚀 Quick Start

### Option 1: Launch in Browser (Easiest!) 🌐

**No installation needed!** Click any of the launch badges above to run notebooks directly in your browser:

#### **Binder** (Recommended)
- Click the **"launch binder"** badge for any notebook
- Wait 1-2 minutes for the environment to build
- All dependencies are pre-installed
- Your changes won't be saved (download notebook to save work)

#### **Google Colab**
- Click the **"Open in Colab"** badge
- Requires Google account
- Changes are automatically saved to your Google Drive
- Slightly different interface than Jupyter

---

### Option 2: Run Locally 💻

#### **Prerequisites:**
- Python 3.7 or higher
- pip package manager

#### **Installation Steps:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive.git
   cd principles-of-genetics-interactive/notebooks
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv genetics_env
   source genetics_env/bin/activate  # On Windows: genetics_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install jupyter ipywidgets matplotlib numpy pandas seaborn plotly
   ```

4. **Enable Jupyter widgets:**
   ```bash
   jupyter nbextension enable --py widgetsnbextension
   ```

5. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

6. **Open any notebook** from the file browser

---

### Option 3: Use Anaconda 🐍

If you have Anaconda installed:

```bash
# Create environment
conda create -n genetics_interactive python=3.9
conda activate genetics_interactive

# Install packages
conda install jupyter ipywidgets matplotlib numpy pandas seaborn
pip install plotly

# Launch
jupyter notebook
```

---

## 📦 Dependencies

All notebooks use the following Python packages:
- `jupyter` - Interactive notebook environment
- `ipywidgets` - Interactive controls and sliders
- `matplotlib` - Plotting and visualization
- `numpy` - Numerical computations
- `pandas` - Data manipulation
- `seaborn` - Statistical visualization
- `plotly` - Interactive plots (used in some notebooks)

**Note:** Each notebook installs its own dependencies automatically when run on Binder or Colab!

---

## 🎓 Who Is This For?

### **Students:**
- Undergraduate biology majors studying genetics
- Graduate students in genetics, genomics, or bioinformatics
- Medical students learning population genetics
- Anyone struggling with the conceptual jump from Mendelian to population genetics

### **Educators:**
- University instructors teaching genetics courses
- Teaching assistants preparing lab sessions
- Curriculum developers creating interactive content
- Anyone looking for engaging teaching demonstrations

### **Researchers:**
- Those needing a refresher on fundamental concepts
- Scientists transitioning between research areas
- Computational biologists learning genetics

---

## 🎯 Learning Path

We recommend working through the notebooks in this order:

1. **Start here:** `family_to_population_bridge.ipynb`
   - Builds intuition for how individual inheritance creates population patterns
   - Essential foundation for understanding population genetics

2. **Then:** `linkage_mapping_interactive.ipynb`
   - Applies recombination concepts to gene mapping
   - Classical genetics meets molecular biology

3. **Finally:** `linkage_vs_LD_tutorial.ipynb`
   - Advanced concepts connecting to modern genomics
   - Bridges to GWAS and evolutionary genetics

**Total time:** 2-3 hours to work through all notebooks

---

## 🧑‍🏫 For Instructors

### **Classroom Use:**

These notebooks are designed for:
- **Live demonstrations** during lectures
- **Lab sessions** with hands-on exploration
- **Homework assignments** with guided questions
- **Flipped classroom** pre-lecture activities

### **Customization:**

All notebooks are provided with **MIT License** - feel free to:
- Modify content for your course
- Add your own examples
- Create derivative works
- Use in commercial educational settings

### **Suggested Discussion Questions:**

Each notebook includes built-in pedagogical questions, but consider adding:
- Population-specific examples relevant to your students
- Current research applications
- Connections to medical genetics
- Historical context and development of ideas

---

## 🌍 Regional Context

These notebooks were developed with a focus on making genetics education accessible using **regional examples from Western Odisha, India**, but the concepts and simulations are universally applicable. The materials are designed to work equally well in any educational context worldwide.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### **Report Issues:**
- Found a bug? [Open an issue](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive/issues)
- Have suggestions? We'd love to hear them!

### **Contribute Content:**
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-notebook`)
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### **Types of Contributions We're Looking For:**
- Additional notebooks on related topics
- Translations to other languages
- Bug fixes and improvements
- Additional interactive visualizations
- Real-world dataset examples

---

## 📖 Educational Philosophy

These notebooks are built on several key principles:

1. **Show, Don't Tell:** Visualizations over equations
2. **Interactive Discovery:** Let students explore parameter space
3. **Bridge Building:** Connect familiar concepts to new ones
4. **Scale Awareness:** Explicitly show how mechanisms work at different scales
5. **Real Examples:** Use actual genetic scenarios and data

---

## 🔧 Troubleshooting

### **Binder Issues:**
- **Taking too long to load?** This is normal for first launch (2-3 minutes)
- **Failed to build?** Try refreshing or use the Colab option
- **Lost your work?** Remember to download notebooks before closing

### **Colab Issues:**
- **Widgets not displaying?** Run the first cell that installs packages
- **Import errors?** Make sure all installation cells complete
- **Slow performance?** Colab free tier has limitations; consider local installation

### **Local Installation Issues:**
- **Widgets not interactive?** Run: `jupyter nbextension enable --py widgetsnbextension`
- **Import errors?** Ensure all packages are installed: `pip install -r requirements.txt`
- **Plots not showing?** Try: `%matplotlib inline` in a cell

---

## 📝 Citation

If you use these notebooks in your research or teaching, please cite:

```bibtex
@misc{principles_genetics_interactive,
  author = {Pattern Hunter},
  title = {Principles of Genetics: Interactive Notebooks},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive}
}
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- ✅ Use for education and research
- ✅ Modify and adapt
- ✅ Commercial use allowed
- ✅ Distribution allowed
- ⚠️ Attribution required
- ⚠️ No warranty provided

---

## 🙏 Acknowledgments

- Developed as part of genetics education initiatives at Kuchinda College, Odisha
- Inspired by students who asked, "Why does this feel like different subjects?"
- Built with open-source tools from the scientific Python community
- Special thanks to the Jupyter, matplotlib, and ipywidgets teams

---

## 📬 Contact

- **Repository:** [github.com/The-Pattern-Hunter/principles-of-genetics-interactive](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive)
- **Issues:** [Report bugs or request features](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive/issues)
- **Discussions:** [Ask questions or share ideas](https://github.com/The-Pattern-Hunter/principles-of-genetics-interactive/discussions)

---

## 🌟 Star This Repository!

If you find these notebooks useful, please **⭐ star this repository** to help others discover it!

---

## 📊 Repository Statistics

![GitHub stars](https://img.shields.io/github/stars/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)
![GitHub forks](https://img.shields.io/github/forks/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/The-Pattern-Hunter/principles-of-genetics-interactive?style=social)

---

**Happy Learning! 🧬🔬📊**

*Making genetics education accessible, interactive, and intuitive - one notebook at a time.*
