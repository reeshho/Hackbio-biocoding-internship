
### QUESTION 1 
def dna_to_protein(dna_seq):
    # Define the codon-to-amino-acid mapping table
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
    }

    # Initialize an empty string to store the protein sequence
    protein_seq = ""

    # Iterate over the DNA sequence in steps of 3 (codons)
    for i in range(0, len(dna_seq) - 2, 3):
        # Extract the current codon (3 nucleotides)
        codon = dna_seq[i:i+3]
        
        # Look up the codon in the codon table to get the corresponding amino acid
        # If the codon is not found in the table, use '-' as a placeholder
        if codon in codon_table:
            amino_acid = codon_table[codon]
        else:
            amino_acid = '-'
        
        # If a STOP codon ('*') is encountered, stop translation
        if amino_acid == '*':
            break
        
        # Append the amino acid to the protein sequence
        protein_seq += amino_acid
    
    # Return the final protein sequence
    return protein_seq

# Example Usage
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
print("Protein Sequence:", dna_to_protein(dna_sequence))


### QUESTION 2 


def logistic_growth_curve(time_range, L=100, k=0.2, x0=50, lag_variation=5, growth_variation=0.05):
    """
    Simulates logistic growth mathematically.
    """
    lag_shift = (lag_variation * 2 * ((1.57 % 1) - 0.5))  
    k_modified = k + (growth_variation * 2 * ((3.14 % 1) - 0.5))  

    population_values = []
    for t in time_range:
        exponent = -k_modified * (t - (x0 + lag_shift))
        exp_value = 2.718 ** exponent  # Approximate e^x
        population = L / (1 + exp_value)
        population_values.append(population)

    return population_values

def generate_growth_curves(num_curves=5, time_points=100):
    """
    Generates multiple logistic growth curves and stores them in a table-like list.
    """
    time_range = list(range(time_points))
    all_curves = []

    for i in range(num_curves):
        x0_varied = 50 + i * 0.5  # Slightly shifting midpoint for each curve
        growth_curve = logistic_growth_curve(time_range, L=100, k=0.2, x0=x0_varied)
        all_curves.append(growth_curve)

    # Creating a table-like structure
    header = ["time"] + [f"curve_{i+1}" for i in range(num_curves)]
    table_data = [header]

    for t_index in range(time_points):
        row = [time_range[t_index]]
        for curve_index in range(num_curves):
            row.append(all_curves[curve_index][t_index])
        table_data.append(row)

    return table_data, all_curves

def time_to_80_percent(population_values, L=100):
    """
    Determines the time step at which the population first reaches 80% of the carrying capacity.
    """
    threshold = 0.8 * L  # 80% of carrying capacity
    for time_step, population in enumerate(population_values):
        if population >= threshold:
            return time_step  # Return the first time step where it reaches 80%
    return None  # If never reaches 80%

# Generate growth curves
num_curves = 5
time_points = 100  # Increased time range for proper growth
table_data, all_curves = generate_growth_curves(num_curves, time_points)

# Find time to reach 80% of L for each curve
times_to_80 = [time_to_80_percent(curve, L=100) for curve in all_curves]

# Display the first 10 rows to check structure
print("\nFirst 10 Rows of Growth Data:")
for row in table_data[:10]:
    print(row)

# Display time steps when each curve reaches 80% of carrying capacity
print("\nTime to reach 80% of carrying capacity for each curve:")
for i, time in enumerate(times_to_80):
    print(f"Curve {i+1}: {time} time steps")


### QUESTION 3 
def hamming_distance(str1, str2):
    """
    Calculates the Hamming distance between two strings, `str1` and `str2`.
    If the strings are of unequal length, the shorter string is padded with spaces
    to match the length of the longer string.
    """
    
    # Determine the maximum length of the two strings
    max_length = max(len(str1), len(str2))
    
    # Pad the shorter string with spaces on the right to make both strings equal in length
    str1 = str1.ljust(max_length)  # Adds spaces to the right of `str1` if needed
    str2 = str2.ljust(max_length)  # Adds spaces to the right of `str2` if needed
    
    # Initialize a counter to keep track of the Hamming distance
    distance = 0
    
    # Iterate through each character position in the strings
    for i in range(max_length):
        # Compare the characters at the current position in both strings
        if str1[i] != str2[i]:
            # If the characters are different, increment the Hamming distance
            distance += 1
    
    # Return the calculated Hamming distance
    return distance

# Example usernames
slack_username = "@Priyanjali"
twitter_handle = "@reesho"

# Calculate the Hamming distance between the two usernames
distance = hamming_distance(slack_username, twitter_handle)

# Print the result
print("Hamming Distance:", distance)
