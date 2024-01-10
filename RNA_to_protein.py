# Solution to Rosalind Problem #8: Translating RNA into Protein

def rna_to_protein(rna_string):
    #Intended input being RNA nucleotides in string format
    #Output will be a string of amino acids corresponding to the input RNA.
    
    #Dictionary below has RNA codon as key and protein as value
    protein_codes = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 
                     'CUG': 'L','AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M','GUU': 'V', 'GUC': 'V', 
                     'GUA': 'V', 'GUG': 'V','UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S','CCU': 'P', 
                     'CCC': 'P', 'CCA': 'P', 'CCG': 'P','ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                     'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A','UAU': 'Y', 'UAC': 'Y', 'UAA': '', 
                     'UAG': '','CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q','AAU': 'N', 'AAC': 'N', 
                     'AAA': 'K', 'AAG': 'K','GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E','UGU': 'C', 
                     'UGC': 'C', 'UGA': '', 'UGG': 'W','CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                     'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R','GGU': 'G', 'GGC': 'G', 'GGA': 'G', 
                     'GGG': 'G'}

    protein_string = "" #initialize empty protein string
    for i in range(0, len(rna_string), 3): #looping in groups of three
        codon = rna_string[i:i + 3]
        amino_acid = str(protein_codes[codon])
        if amino_acid != '': #since stop codon is set to ''
            protein_string += amino_acid
        else: #get out of loop if stop codon
            break

    return protein_string