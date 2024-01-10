#Solution to Rosalind Problem #1: Counting DNA Nucleotides

def count_nucleotides(dna_string):
    #Function input is intented to be a string of DNA nucleotides
    #Output will be in order 'A', 'C', 'G', and 'T'
    a_count = 0 #intializing variables
    c_count = 0
    g_count = 0
    t_count = 0
    for nucleotide in dna_string: #looping over each item in the sample
        if nucleotide.lower() == "a": #if a add to a count
            a_count +=1
        elif nucleotide.lower() == "c": #if c add to c count
            c_count +=1
        elif nucleotide.lower() == "g": #if g add to g count
            g_count +=1
        elif nucleotide.lower() == "t": #if t add to t count
            t_count +=1
        else: #non-nucleotides will be skipped
            continue
            
    result = f"{a_count} {c_count} {g_count} {t_count}" #adding strings together with spaces
    return(result)

