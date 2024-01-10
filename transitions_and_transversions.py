# Solution to Rosalind Problem #12: Transitions and Transversions


def transversion_transition_ratio(s1, s2):
    #Intended input is two strings of DNA nucleotides of equal length.
    #Output is the ratio of transitions to transversions in the two sequences (transitions/transversions).
    
    transitions = 0 #initializing transition count
    transversions = 0 #initializing transversion count
    for nuc_1, nuc_2 in zip(s1, s2): #looping over both sequences
        if nuc_1 != nuc_2: #not a match
            if (nuc_1 in 'AG' and nuc_2 in 'AG') or (nuc_1 in 'CT' and nuc_2 in 'CT'): #if each matches transition
                transitions += 1
            else: #not a transition so a transversion
                transversions += 1
    try: #try except block for situation if transversion count is 0
        ratio = transitions/transversions
    except ZeroDivisionError:
        return(0)
    
    return(round(ratio, 11))