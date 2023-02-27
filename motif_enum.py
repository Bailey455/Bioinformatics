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

def hamming_distance(p, q):
    count = 0
 
    for letters in range(0, len(p) - 1):
        if p[letters] != q[letters]:
            count += 1
    
    return count

def motif_enum(dna, k, d):
    patterns = []
    text = dna[0]

    for i in range(0, len(text) - int(k)):
        kmer = text[i: i + int(k)]
        kmer_neighbors = neighbors(kmer, d)
        #print(kmer_neighbors)
        for j in range(0, len(kmer_neighbors)):
            for rest in range(1, len(dna)):
                next_section = dna[rest]
                for length in range(0, len(next_section)):
                    if kmer_neighbors[j] == next_section[length: length + int(k)]:
                        if hamming_distance(kmer_neighbors[j], next_section[length: length + int(k)]) < int(d):
                            if kmer_neighbors[j] not in patterns:
                                patterns.append(kmer_neighbors[j])

    return patterns
    #for each k-mer window in dna with at most d mismatches
        #use neighborhood + hamming distance to check for mismatches

#start main
genome_file = open("motif_enum.txt", "r")

info = genome_file.readline()
k, d = info.split()
next_info = genome_file.readline()
dna = next_info.split()
    
results = ' '.join(motif_enum(dna, k, d))
print(results)

genome_file.close()
#read and split both lines
#split the sections of DNA into an array which the function runs with