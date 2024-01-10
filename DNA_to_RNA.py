#Solution to Rosalind Problem #2: Transcribing DNA into RNA

def dna_to_rna(dna_string):
    #Intended input is a string of DNA nucleotides
    #Output will be a string of RNA nucleotides
    rna = "" #initializing string for storing RNA sequence
    for nucleotide in dna_string:
        if nucleotide.lower() == "t": #if T then change to U
            rna += "U"
        else: #any others just add to string
            rna += nucleotide
    return(rna)    