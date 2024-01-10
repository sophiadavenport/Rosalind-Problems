# Solution to Rosalind Problem #9: Finding a Motif in DNA

def find_substring_locations(s, t):
    locations = []
    t_len = len(t)

    for i in range(len(s) - t_len + 1):
        if s[i:i + t_len] == t:
            locations.append(i + 1)  # Adjusting positions to 1-based index

    return(locations)
