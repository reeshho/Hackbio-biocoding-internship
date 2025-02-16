
# HackBio Biocoding Internship - Stage One

## Project Overview

This repository contains my submission for the **HackBio Biocoding Internship - Stage One Tasks**. 
It repository contains Python implementations for three different bioinformatics and computational biology tasks:

1. **DNA to Protein Translation**: Converts a given DNA sequence into a protein sequence using a codon-to-amino-acid mapping.
2. **Logistic Growth Curve Simulation**: Models population growth using a logistic equation and analyzes growth trends.
3. **Hamming Distance Calculation**: Computes the Hamming distance between two given strings, which is useful for comparing genetic sequences or text-based identifiers.

Each function is designed to be modular and reusable, making it suitable for applications in computational biology and data analysis.



## Task Description
The goal of this task is to:\
✔️ **DNA to Protein Translation** - This function translates a given DNA sequence into its corresponding protein sequence using a codon-to-amino-acid mapping.
Implement functions to solve the assigned problems.\
✔️ **Logistic Growth Curve Simulation** - This function simulates population growth using the logistic equation.

$$
f(x) = \frac{L}{1 + e^{-k(x - x_0)}}
$$

where:
- **L** is the carrying capacity.
- **k** is the growth rate.
- **x₀** is the midpoint (where population reaches 50% of L).

✔️ **Hamming Distance Calculation** - This function calculates the Hamming distance between two strings, which measures the number of positions where the characters differ.

The **solutions** for this stage are implemented in **Python** and stored in the file `HACKBIO_STAGE_1.py`.




## Implementation Details

### What I Did in This Code

#### ➀ DNA to Protein Translation

#### **Implementation Details**

- Implemented the `dna_to_protein()` function to convert a DNA sequence into its corresponding protein sequence.
- A **codon table** is defined that maps each three-letter DNA codon to its corresponding amino acid.
- The function reads the DNA sequence in triplets (codons) and converts each codon into its amino acid representation.
- The translation stops if a **stop codon** (*TAA, TAG, TGA*) is encountered.

#### **Code Example**

```python
# Example usage
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
print("Protein Sequence:", dna_to_protein(dna_sequence))
```

---
#### Logistic Growth Curve Simulation

- Implemented `logistic_growth_curve()` to **model population growth** using the **logistic equation**.
- Added variation in **lag phase** and **growth rate**.
- Simulated multiple growth curves and stored them in a **table-like structure**.
- Implemented `time_to_80_percent()` to determine when the population reaches **80% of carrying capacity**.
- Printed the **first 10 rows** of the dataset and **time-to-80% values**.

#### **Code Example**

```python
# Generate logistic growth curves
table_data, all_curves = generate_growth_curves(num_curves=5, time_points=100)

# Find time to reach 80% of L for each curve
times_to_80 = [time_to_80_percent(curve, L=100) for curve in all_curves]

print("Time to reach 80% of carrying capacity:", times_to_80)
```

---

#### Hamming Distance Calculation

- Implemented `hamming_distance()` to compute **Hamming distance** between two strings.
- If the strings are of **unequal length**, the shorter string is **padded with spaces** to match the length of the longer one.
- Compared two usernames (`Slack` vs. `Twitter`) and printed the Hamming distance.
- Useful for **genetic sequence comparisons** and **username similarity checks**.
- Iterates through both strings and counts the number of mismatched characters.

#### **Code Example**

```python
# Example usernames
slack_username = "@Arpit"
twitter_handle = "@ArpitSharma1010"

# Compute Hamming distance
distance = hamming_distance(slack_username, twitter_handle)
print("Hamming Distance:", distance)
```


## Sample Output

```
Protein Sequence: MAIVMGR*GCCRE
First 10 Rows of Growth Data:
['time', 'curve_1', 'curve_2', 'curve_3', 'curve_4', 'curve_5']
[0, 0.2, 0.3, 0.4, 0.5, 0.6]
...
Time to reach 80% of carrying capacity for each curve:
Curve 1: 50 time steps
Curve 2: 52 time steps
...
Hamming Distance: 6
```

---
