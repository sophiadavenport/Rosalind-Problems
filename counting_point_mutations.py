# Solution to Rosalind Problem #6: Counting Point Mutations

def hamming_distance(s, t):
    #Intended input (s and t) being two strings of DNA nucleotides of equal length.
    #Output is the number of point mutations between the two sequences. 
    if len(s) != len(t): #if of unequal lengths
        return(print("DNA sequences must be of equal length"))
    else:
        count = 0 #initalizing count of point mutations
        for i in range(len(s)): #for the length of each string
            if s[i] != t[i]: #if the nucleotides do not match
                count +=1
    return(count)