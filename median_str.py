def median_str(dna, k):
    distance = k * len(dna) #make distance as large as possible
    patterns = all_strings(k)
    median = ''

    for i in range(0, len(patterns)):
        patt = patterns[i]
        d = d(patt, dna)
        if distance > d:
            distance = d
            median = patt
    return median

def all_strings(k):
    k_as = ''
    for i in range(0, int(k)):
        k_as = k_as + 'A'
    return neighbors(k_as, k)

def neighbors(pattern, d):
    if d == 0:
        return[pattern]
    elif len(pattern) == 1:
        return['A', 'C', 'G', 'T']
    else:
        neighborhood = []
        suffix = pattern[1:] #suffix = pattern: pattern len - 1
        suffix_neighbors = neighbors(suffix, d)

        for text in suffix_neighbors:
            if hamming_distance(text, suffix) < int(d):
                for x in ['A', 'C', 'G', 'T']:
                    neighborhood.append(x + suffix)
            else:
                neighborhood.append(pattern[0] + text)

        return neighborhood

def d(dna, motifs):
    sum = 0
    for sections in dna:
        sum += hamming_distance(dna[sections], motifs)
    
    return sum


def hamming_distance(p, q):
    count = 0
 
    for letters in range(0, len(p) - 1):
        if p[letters] != q[letters]:
            count += 1
    
    return count

#start main
genome_file = open("motif_enum.txt", "r")

k = genome_file.readline()
next_info = genome_file.readline()
dna = next_info.split()
    
results = ' '.join(median_str(dna, k))
print(results)

genome_file.close()