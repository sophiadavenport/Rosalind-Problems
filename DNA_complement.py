#Solution to Rosalind Problem #3: Complementing a Strand of DNA

def reverse_complement(dna_string):
    #Intended input is a string of DNA nucleotides
    #Output will be the reverse complement of the input DNA strand
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse = ""

    for nucleotide in reversed(dna_string): #going over the nucleotides input in reversed order
        reverse += complement[nucleotide] #adding to complement to reverse string

    return(reverse)