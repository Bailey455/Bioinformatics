def patterns_with_mis(sequence, pattern, errors):
    pattern_len = len(pattern)
    seq_len = len(sequence)
    indices = []

    for i in range(0,seq_len-pattern_len+1):
        if hamming_distance(sequence[i:i + pattern_len], pattern) <= int(errors):
            indices.append(i)

    return indices

def hamming_distance(p, q):
    count = 0

    for letters in range(0, len(p) - 1):
        if p[letters] != q[letters]:
            count += 1
    
    return count

#start main
genome_file = open("patterns_with_mis.txt", "r")

pattern = genome_file.readline()
sequence = genome_file.readline()
errors = genome_file.readline()
    
#print(patterns_with_mis(sequence, pattern, errors))
pat_list = " ".join(str(n) for n in patterns_with_mis(sequence, pattern, errors))
print(pat_list)

genome_file.close()