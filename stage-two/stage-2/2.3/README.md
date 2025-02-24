# **Metabolic Response Analysis of Pesticide Treatment in WT and Mutant Cells** 

**HackBio Internship - Stage 2 Task**

---
## **Introduction**
This project investigates the metabolism of wild-type (WT) and mutant cells in response to pesticide treatment using Python. We analyze metabolic shifts (ΔM), visualize differences with scatter plots, and identify significantly varying metabolites. Additionally, we track metabolite changes over time to observe pathway disturbances. By comparing WT and mutant responses, we aim to gain insights into pesticide effects, metabolic adaptation, and potential resistance mechanisms.

## **Required Module**
This analysis used the following Python libraries:
```
pip install pandas numpy matplotlib seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
`pandas`: For data loading, manipulation, and preprocessing.
`numpy`: For numerical operations, such as computing metabolic differences (ΔM).
`matplotlib`: For creating visualizations, such as scatter and line plots.
`seaborn`: For enhanced statistical plotting and styling.

## **Dataset**
The dataset is sourced from HackBio-Internship 
```
# Importing data
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"
```
## **Extracting Metabolite Concentrations in WT and Mutant Cells**
We extract wild-type (WT) and mutant cell metabolite intensity values before and after treatment with a pesticide.
The dataset’s first column is assigned a name, and we filter rows on conditions like`df["Unnamed: 0"] == "WT_DMSO_1".`
`.iloc[:, 1:]` selects all metabolite columns, and `.values.flatten()` converts them into 1D arrays.

## **Analysis steps**

### **1. Computing Metabolic Differences (ΔM)**
`metabolites = df.columns[1:]` is keeping track of names of all the metabolites in store.
ΔM (Delta M) is determined by subtracting post-treatment and pre-treatment metabolite intensities: 
  - For WT: `WT_24h - WT_DMSO`
  - For Mutants: `Mutant_24h - Mutant_DMSO`

### **2. Scatter Plot of ΔM (WT vs. Mutant)**
- We visualize each metabolite's metabolic shift (ΔM) by plotting ΔM in WT against ΔM in the mutant on a scatter plot.  
- The dashed horizontal black line (y = x) indicates a uniform metabolic response between the two strains.  
- Points above the line signify an increase in the metabolite in the mutant.  
- Points below the line indicate a greater decrease in the metabolite in the mutant.
```
plt.xlabel("ΔM Wild Type")
plt.ylabel("ΔM Mutant")
plt.title("Comparisons of Metabolic response WT vs Mutant")
plt.legend()
plt.show()
```

![Comparisons of Metabolic response WT vs Mutant](figures/scatter_plot.png)

This plot graphically shows differences in metabolism in WT and mutant strains.

ANSWERING THE QUESTION: What do the trends on either side of the graph represent?
The reference line y = x acts as a baseline to assess whether metabolic shifts (ΔM) in WT and MUT follow a similar pattern.  
Points clustering along this line indicate a strong positive correlation between ΔM in both conditions.  
However, as ΔM increases, a higher concentration of points suggests that the treatment affects metabolism in both WT and MUT similarly.  
This implies that while the treatment induces metabolic changes, its overall impact remains comparable across both conditions.

### **3. Residuals & Outlier Detection**
We calculate residuals to measure the difference:
```
residuals = deltaM_Mutant - deltaM_WT
```
Threshold = 0.3:
- Grey points: Within threshold (low variation).
- Salmon points: Beyond threshold (high variation, key outliers).
```
plt.plot(x_vals, x_vals, color='black', linestyle='--', label="y = x")
plt.xlabel("ΔM Wild Type")
plt.ylabel("ΔM Mutant")
plt.title("Metabolic difference between WT vs Mutant with residuals threshold at 0,3")
plt.legend()
plt.show()
```

![Metabolic difference between WT vs Mutant with residuals threshold at 0,3](figures/residuals_plot.png)

Outliers represent metabolites with a strong differential response, highlighting key biological changes.  

**ANSWERING THE QUESTION: What are these metabolites?**  
After running `len(outliers)`, we find that 65 out of 108 metabolites are classified as outliers based on the 0.3 threshold.  
The density of outliers increases as ΔM grows, indicating that metabolic variations become more pronounced with larger changes.  
Despite continuous metabolic activity, these outliers exhibit a significant ΔM difference, suggesting they are particularly sensitive to the treatment.

### **4. Extracting Outlier Metabolites**
We filter and extract the names of metabolites where residuals exceed the 0.3 threshold.
The output is a list of key metabolites that undergo significant metabolic shifts.
```
outliers = metabolites[np.abs(residuals) > threshold].tolist()
```
### **5. Time Series Analysis of Selected Metabolites**
This section explores how metabolite levels fluctuate over time after pesticide treatment.  
Instead of focusing on a single time point (24h), we monitor metabolic changes at 0h, 8h, and 24h.  

First, we select specific metabolites for the time series plot, as plotting all 65 outliers simultaneously isn't feasible.  
Next, we prepare the time series data, ensuring the figure size allows for clear visualization, while distinct colors help differentiate metabolite trends.<br/>
And on step 3, we plot metabolic changes over time, by looping over the selected metabolites, then we extract the metabolites values at different time points for WT and mutant cells, this let us compare how WT and mutant cells metabolize over time and track trends in metabolic responses.<br/>
On the last step, we Format and diplay the plot 
```
plt.xlabel("Time")
plt.ylabel("Metabolic Intensity")
plt.title("Metabolic Evolution Over 24h for 6 Selected Metabolites (WT vs MUT)")

plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.tight_layout()  
plt.show()
```

![Metabolic Evolution Over 24h for 6 Selected Metabolites (WT vs MUT)](figures/metabolic_evolution.png)

## Interpretation 
### **1. Graphic 1 : Scatter Plot (Metabolic Difference Between WT vs Mutant)**
This plot visualizes the metabolic shifts (ΔM) in wild-type (WT) and mutant (MUT) conditions.  
The black dashed line (y = x) represents an ideal scenario where both conditions exhibit identical metabolic changes.  
Points deviating above or below this line highlight metabolic differences between WT and MUT.

### **2. Graphic 2 : Second Scatter Plot (Metabolic Difference Highlighting Residuals)**
This plot expands on the first by highlighting points based on a residual threshold of 0.3.  
Salmon-colored points represent metabolites with significant differences between WT and MUT, while gray points align more closely with the expected y = x trend.  
This visualization helps pinpoint metabolites that show distinct behavior between the two conditions.

### **3. Graphic 3 : Second Scatter Plot (Metabolic Difference Highlighting Residuals)**
This graph illustrates the metabolic intensity of six selected metabolites over 24 hours for both WT and MUT.  
Solid lines depict WT, while dashed lines represent MUT.  
While some metabolites remain stable, others fluctuate over time, revealing differences in metabolic processing.  
This provides insights into how metabolism evolves differently in mutant cells compared to the wild type.
