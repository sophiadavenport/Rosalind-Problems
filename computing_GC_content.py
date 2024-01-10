# Solution to Rosalind Problem #5: Computing GC Content

#Creating a dictionary of FASTA file contents with keys being sequence ID information and values being DNA strings 
file_path = "rosalind_trial1.fasta"
fasta_dict = {} #initializing dictionary to store fasta file info
with open(file_path, "r") as file: 
    for line in file: #reading in file line by line
        line = line.strip()
        if line.startswith('>'): #keys as IDs
            current_key = line[1:]
            fasta_dict[current_key] = ""
        else: #sequence as values
            fasta_dict[current_key] += line
file.close()

def gc_content(fasta_dict):
    #Intended input being a dictionary with FASTA file contents. IDs as keys and DNA sequences in string format as values.
    #Output is highest GC content string with sequence ID listed on the first line and rounded GC content on the second line.
    high_score = 0 #initializing high score to 0
    for i in fasta_dict:
        #line below gets gc percent by counting G or C occurrences, dividing by length of the seq and *100
        gc_percent = (sum(1 for base in fasta_dict[i] if base.upper() in ('G', 'C')))/(len(fasta_dict[i]))*100
        if gc_percent > high_score: #if percentage is the current highest then store
            high_score = gc_percent
            high_seq = i
    return(print(f"{high_seq}\n{round(high_score, 6)}"))