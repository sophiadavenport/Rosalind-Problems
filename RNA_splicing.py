# Solution to Rosalind Problem #11: Finding a Motif in DNA

from Bio import SeqIO
from Bio.Seq import Seq

def process_dna_with_introns(dna, introns):
    #Intended input is a string of DNA nucleotides and a list of strings of introns. (FASTA format)
    #Output is a string with the protein sequence of the input dna sequence.
    
    for intron in introns: #Remove introns from DNA sequence
        dna = dna.replace(intron, '')

    rna = Seq(dna).transcribe() #DNA to RNA
    protein = rna.translate(to_stop=True) #RNA to protein

    return protein