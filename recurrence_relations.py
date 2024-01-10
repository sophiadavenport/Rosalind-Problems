# Solution to Rosalind Problem #4: Rabbits and Recurrence Relations

def rabbit_pairs(sample):
    #Intended input is: n k
    #Output returns the total number of rabbit pairs present after n months
    s = sample.split(" ") #s[0] being months and s[1] being litter number
    n = int(s[0])
    k = int(s[1])
    if n == 1:
        return(1) #Month one would be different

    pairs = [1, 1] #Start with two pairs (1 pair for 1st month, 1 pair for 2nd month)

    for i in range(2, n): #start at month 2 and finish at last month
        new_pairs = pairs[-1] + k * pairs[-2]  # Fibonacci sequence formula with a factor of k
        pairs.append(new_pairs) #add to list

    return(pairs[-1]) #return final pair