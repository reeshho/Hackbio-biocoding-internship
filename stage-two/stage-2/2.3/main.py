#___________________________________________________________________________________________________________________________________________
# Required Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#___________________________________________________________________________________________________________________________________________
# Importing data
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"
df = pd.read_csv(url, sep="\t")  
#___________________________________________________________________________________________________________________________________________
# Calculating the ΔM :
WT_DMSO = df[df["Unnamed: 0"] == "WT_DMSO_1"].iloc[:, 1:].values.flatten()
WT_24h = df[df["Unnamed: 0"] == "WT_pesticide_24h_1"].iloc[:, 1:].values.flatten()

Mutant_DMSO = df[df["Unnamed: 0"] == "mutant_DMSO_1"].iloc[:, 1:].values.flatten()
Mutant_24h = df[df["Unnamed: 0"] == "mutant_pesticide_24h_1"].iloc[:, 1:].values.flatten()

metabolites = df.columns[1:]  

deltaM_WT = WT_24h - WT_DMSO
deltaM_Mutant = Mutant_24h - Mutant_DMSO
#___________________________________________________________________________________________________________________________________________
# Plotting a scatter plot showing the difference for ΔM for WT and Mutants Fitting a line that satifies a y-intercept of 0 and a slope of 1.
plt.figure(figsize=(8,6))
sns.scatterplot(x=deltaM_WT, y=deltaM_Mutant)

x_vals = np.linspace(min(deltaM_WT), max(deltaM_WT), 100)
plt.plot(x_vals, x_vals, color='black', linestyle='--', label="y = x")

plt.xlabel("ΔM Wild Type")
plt.ylabel("ΔM Mutant")
plt.title("Metabolic difference between WT vs Mutant")
plt.legend()
plt.show()
#___________________________________________________________________________________________________________________________________________
'''
ANSWERING THE QUESTION : How do you explain the trends you see on either direction of the plot? 
The reference line y = x acts as a benchmark to evaluate whether metabolic changes (ΔM) in WT and MUT conditions follow a similar trend.  
The clustering of points along this line suggests a strong positive correlation between ΔM in both conditions.  
However, as ΔM increases, the density of points also rises, indicating that the treatment influences metabolism similarly in both WT and MUT.  
This implies that while the treatment has a clear impact, its overall effect remains comparable across both conditions.
'''
#___________________________________________________________________________________________________________________________________________
# Calculating Residuals and setting a threshold of 0.3 when giving a color in the scatter plot

residuals = deltaM_Mutant - deltaM_WT

threshold = 0.3  

colors = np.where(np.abs(residuals) <= threshold, "grey", "salmon")

plt.figure(figsize=(8,6))
sns.scatterplot(x=deltaM_WT, y=deltaM_Mutant, hue=colors, palette={"grey": "grey", "salmon": "salmon"})

plt.plot(x_vals, x_vals, color='black', linestyle='--', label="y = x")
plt.xlabel("ΔM Wild Type")
plt.ylabel("ΔM Mutant")
plt.title("Metabolic difference between WT vs Mutant with residuals threshold at 0,3")
plt.legend()
plt.show()
# Separating the outliers respecting the 0.3 threshold and converting them into a list
outliers = metabolites[np.abs(residuals) > threshold].tolist()  # Convert to list
#___________________________________________________________________________________________________________________________________________
'''
ANSWERING THE QUESTION : What are these metabolites ?
After running `len(outliers)`, we find that 65 out of 108 metabolites are classified as outliers based on the 0.3 threshold.  
As ΔM increases, the density of these outliers also rises, indicating that metabolic variations become more pronounced with larger changes.  
Despite the overall metabolic activity, these outliers likely show a significant difference in ΔM, suggesting they are particularly sensitive to the treatment..
 
 In order to know these metablites we just display outliers.
 The output is the list of the metabolites : 
 
['acetylcarnitine',
 'adenine',
 'adenosine_cyclic_monophosphate',
 'adenosine_monophosphate',
 'adipic_acid',
 'alpha_ketoglutaric_acid',
 'aminoadipic_acid',
 'arabitol',
 'arginine',
 'argininosuccinic_acid',
 'asparagine',
 'aspartic_acid',
 'butyrylcarnitine',
 'carnitine',
 'citramalic_acid',
 'citrulline',
 'creatine',
 'creatine_phosphate',
 'creatinine',
 'cystathionine',
 'cystine',
 'deoxyadenosine_triphosphate',
 'deoxythymidine_triphosphate',
 'deoxyuridine',
 'dihydroxyisovalerate',
 'gamma_glu_cys',
 'glutamine',
 'glycine',
 'guanosine',
 'hexose',
 'hexose_6_phosphate',
 'histidine',
 'hydroxy_glutamic_acid',
 'hydroxyglutaric_acid',
 'hypoxanthine',
 'isoleucine',
 'itaconic_acid',
 'lactic_acid',
 'leucine',
 'maleic_acid',
 'methionine',
 'myristoylcarnitine',
 'n_acetylglutamic_acid',
 'n_carbamyl_glutamic_acid',
 'o_phosphorylethanolamine',
 'orotic_acid',
 'oxamic_acid',
 'phenylalanine',
 'phospho_serine',
 'pyridoxal_hydrochloride',
 'pyruvic_acid',
 'riboflavin',
 'ribose_5_phosphate',
 'serine',
 'succinic_acid',
 'thiamine',
 'threonine',
 'tryptophan',
 'uracil',
 'uridine',
 'uridine_diphosphohexose',
 'uridine_monophosphate',
 'uridine_triphosphate',
 'valine',
 'xylulose_5_phosphate']
'''
#___________________________________________________________________________________________________________________________________________
# Generating the Line plot that spans from 0h treatment to 8h and 24hr of 6 randomly selected metabolites from the outliers list.
# FIRST : We define the time points we want to plot. 
wt_timepoints = ["WT_DMSO_1", "WT_pesticide_8h_1", "WT_pesticide_24h_1"]
mut_timepoints = ["mutant_DMSO_1", "mutant_pesticide_8h_1", "mutant_pesticide_24h_1"]
time_labels = ["0h", "8h", "24h"]

# THEN : Ensure we have at least some metabolites to select
if len(outliers) == 0:
    print("No outliers detected above the threshold. Skipping plot.")
    selected_metabolites = []
elif len(outliers) < 6:
    selected_metabolites = outliers  # If the outliers are less than 6 items in the list then we take them all
else:
    selected_metabolites = np.random.choice(outliers, 6, replace=False).tolist() 

# FINALLY : Proceed with plotting only if we have metabolites to plot
if len(selected_metabolites) > 0:
    plt.figure(figsize=(10, 6))

    # Assign a unique color for each selected metabolite
    colors = plt.cm.get_cmap("tab10", len(selected_metabolites))

    for idx, metabolite in enumerate(selected_metabolites):
        color = colors(idx)  

        # WT
        wt_values = df[df["Unnamed: 0"].isin(wt_timepoints)][["Unnamed: 0", metabolite]]
        wt_values = wt_values.set_index("Unnamed: 0").T
        plt.plot(time_labels, wt_values.iloc[0], marker='o', linestyle='-', color=color, label=f"{metabolite} (WT)")

        # MUT
        mut_values = df[df["Unnamed: 0"].isin(mut_timepoints)][["Unnamed: 0", metabolite]]
        mut_values = mut_values.set_index("Unnamed: 0").T
        plt.plot(time_labels, mut_values.iloc[0], marker='s', linestyle='--', color=color, label=f"{metabolite} (MUT)")

    plt.xlabel("Time")
    plt.ylabel("Metabolic Intensity")
    plt.title("Metabolic Evolution Over 24h for 6 Selected Metabolites (WT vs MUT)")

    plt.legend(loc="upper left", bbox_to_anchor=(1,1))
    plt.tight_layout()  # Prevent layout issues
    plt.show()
#___________________________________________________________________________________________________________________________________________
'''
PLOT LINE INTERPRETATION :
After randomly selecting six metabolites and plotting their evolution under WT and MUT conditions, we observe that their overall behavior follows a similar trend.  
While slight differences appear around the 8th hour mark, the metabolic responses tend to converge as the treatment progresses to 24 hours.  
This suggests that, despite initial variations, the long-term metabolic adaptation in both conditions exhibits comparable patterns, indicating that the engineering of these mutants does not have a significant impact.
'''
