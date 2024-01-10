# Solution to Rosalind Problem #10: Calculating Protein Mass


def protein_mass(protein):
    #Intended input is a string of amino acids in a protein.
    #Output is the mass of the protein rounded to 3.
    weighted_alphabet = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
                         "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
                         "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
                         "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}
    
    mass = 0 #intializing mass
    for key in weighted_alphabet.keys(): #looping over the keys in the alphabet
        weight = weighted_alphabet[key] 
        mass += protein.count(key)*weight #each instance of a protein adding its weight to the total mass
    return(round(mass, 3))