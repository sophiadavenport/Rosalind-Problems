# Solution to Rosalind Problem #7: Introduction to Mendelian Inheritance

def mendel_first_law(k, m, n): 
    #Intended input is k, m, and n all being integers. K representing homozygous dominant, m as heterozygous, and n as homozygous recessive individuals. 
    #Output is the probability that an offspring resulting from a cross of these individuals contains a dominant allele. 
    probabilities = [k * (k - 1),  # AA and AA 
                     (k * m)*2,  # AA and Aa 
                     (k * n)*2,  # AA and aa  
                     m * (m - 1) * 0.75, # Aa and Aa 
                     (m * n * 0.5)*2, # Aa and aa 
                     0,  # aa and aa
                    ]
    total = k + m + n #total possible parents
    prob_dominant = sum(probabilities)/total/(total - 1) #probabilities of a dominant offspring
    return round(prob_dominant, 5) 