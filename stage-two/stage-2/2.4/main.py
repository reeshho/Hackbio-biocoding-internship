#___________________________________________________________________________________________________________________________________________
# Required Modules
import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
#___________________________________________________________________________________________________________________________________________
# Importing the data and dealing with the column issue
sift_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
response = requests.get(sift_url)
raw_data = response.text
sift_df = pd.read_csv(StringIO(raw_data), delimiter=r"\s+", engine="python")

foldx_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"
response = requests.get(foldx_url)
raw_data = response.text
foldx_df = pd.read_csv(StringIO(raw_data), delimiter=r"\s+", engine="python")
#___________________________________________________________________________________________________________________________________________
# Creating a column specific_Protein_aa which will be a cantenation of the Protein and Amino_acid columns such that If you have Protein A5A607 and Amino_acid E63D, you have specific_Protein_aa A5A607_E63D
sift_df["specific_Protein_aa"] = sift_df["Protein"] + "_" + sift_df["Amino_Acid"]
foldx_df["specific_Protein_aa"] = foldx_df["Protein"] + "_" + foldx_df["Amino_Acid"]
#___________________________________________________________________________________________________________________________________________
# Using the specific_Protein_aa column, We merged sift and foldx dataset into one final dataframe
foldx_dataframe_clean = foldx_df.drop(columns=['Protein', 'Amino_Acid'])
final_dataframe = pd.merge(sift_df, foldx_dataframe_clean, on='specific_Protein_aa')
#___________________________________________________________________________________________________________________________________________
# Using the criteria proposed by the authors, we try to find all mutations that have a SIFT score below 0.05 and FoldX Score above 2.
deleterious_mutations = final_dataframe[(final_dataframe['sift_Score'] < 0.05) & (final_dataframe['foldX_Score'] > 2)]
#___________________________________________________________________________________________________________________________________________
# INVISTIGATION FOR THE AMINO ACID THAT HAS THE MOST FUNCTIONAL AND STRUCTURAL IMPACT:
#___________________________________________________________________________________________________________________________________________
# DATA PREPARATION
# The logic to extract the Amino acid that got mutated : 
final_dataframe['Mutated_AA'] = final_dataframe['Amino_Acid'].str[0]
# We calculated the number of occurence of each amino acid that will be extracted
frequency_table = final_dataframe['Amino_Acid'].str[0].value_counts().reset_index()
# We renamed the table for better understanding : 
frequency_table.columns = ['Original_Amino_Acid', 'Frequency']
# We sorted the frequency_table by number of occurence:
frequency_table = frequency_table.sort_values(by='Frequency', ascending=False)
#___________________________________________________________________________________________________________________________________________
# PLOTTING : ( BARPLOT )
plt.figure(figsize=(10, 6))
sns.barplot(
    data=frequency_table,
    x='Original_Amino_Acid',  
    y='Frequency',
    palette='viridis'
)
plt.title('Frequency of Original Amino Acids')
plt.xlabel('Amino Acid')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
# PLOTTING : ( PIECHART )
plt.figure(figsize=(8, 8))

wedges, texts, autotexts = plt.pie(
    frequency_table['Frequency'],
    labels=frequency_table['Original_Amino_Acid'],
    autopct='%.1f%%', 
    startangle=90,      
    colors=sns.color_palette('tab20b'),  
    wedgeprops={'edgecolor': None},
    pctdistance=0.92,  
    textprops={'fontsize': 10}
)


for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

plt.title('Proportion of Original Amino Acids', fontsize=14)
plt.tight_layout()
plt.show()
#___________________________________________________________________________________________________________________________________________
'''
PLOTS INTERPRETATION :
Alanine (A) emerges as the most frequently mutated residue in high-impact variants (SIFT < 0.05 and FoldX > 2), accounting for 11,828 mutations (15.7%) of the dataset. This emphasizes its crucial role in maintaining protein stability and evolutionary conservation, likely due to its presence in structurally sensitive regions such as hydrophobic cores.  

Valine (V) ranks second, with 6,241 mutations (8.3%), further highlighting the destabilizing effects of mutating hydrophobic residues essential for structural integrity.  

In contrast, Cysteine (C) and Tryptophan (W) show significantly fewer high-impact mutations (584 and 403 cases, respectively). This rarity may be explained by:  

- **Cysteine**: Its involvement in disulfide bond formation, making mutations evolutionarily unfavorable due to strong purifying selection.  
- **Tryptophan**: Its large, rigid side chain, which is rarely substituted without severe structural consequences.

'''
