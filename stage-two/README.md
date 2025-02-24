# Task Code 2: Data Analysis in Microbiology, Plant Science, and Biochemistry

This repository contains my work on **Task Code 2**, where I analyze different biological datasets across microbiology, botany, and biochemistry using Python. The goal is to process, visualize, and interpret biological data effectively.

## Overview of the Tasks

### 1️⃣ Microbiology: Growth Curve Analysis (Task Code 2.1)
In this part, I analyze bacterial growth data by:
- Plotting **OD600 (optical density) vs. time** for different strains.
- Overlaying the growth curves of **knockout (-) and knock-in (+) strains**.
- Determining the **time to reach carrying capacity** for each strain/mutant.
- Creating **scatter plots and box plots** to compare growth times.
- Performing **statistical analysis** to check if there’s a significant difference between the strains.

### 2️⃣ Botany: Metabolic Response to Pesticide (Task Code 2.3)
Here, I analyze plant metabolism under pesticide treatment by:
- Calculating **metabolic shifts (ΔM)** between control (DMSO) and pesticide-treated plants.
- Creating a **scatter plot** comparing metabolic changes in wild-type (WT) and mutant plants.
- Fitting a **y = x reference line** and analyzing residuals.
- Identifying significantly affected metabolites by highlighting outliers.
- Selecting 6 key metabolites and **tracking their trends over time (0h, 8h, 24h)**.

### 3️⃣ Biochemistry & Oncology: Protein Mutation Impact (Task Code 2.4)
This section focuses on how mutations affect protein structure and function:
- Merging **SIFT** (functional impact) and **FoldX** (structural impact) datasets.
- Identifying **mutations with high functional and structural impact**.
- Analyzing **amino acid substitution patterns** to find the most affected residues.
- Creating **bar plots and pie charts** to visualize amino acid mutation frequencies.
- Discussing the biological significance of highly mutated residues.

## 📌 Key Takeaways
- Growth analysis helps us understand how genetic modifications impact bacterial growth.
- Metabolic shifts reveal how mutant plants adapt to pesticides.
- Protein mutation studies highlight which amino acids are most critical for structure and function.

## 🛠 Tools & Libraries Used
- **Pandas** for data handling
- **Matplotlib & Seaborn** for visualization
- **Scipy & Statsmodels** for statistical analysis

---
This project is a deep dive into biological data analysis using computational tools. Feel free to explore the code and results! 🚀
