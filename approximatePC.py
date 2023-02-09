def approximatePC(sequence, pattern, errors):
    pattern_len = len(pattern)
    seq_len = len(sequence)
    count = 0

    for i in range(0,seq_len-pattern_len+1):
        if hamming_distance(sequence[i:i + pattern_len], pattern) <= int(errors):
            count += 1

    return count

def hamming_distance(p, q):
    count = 0

    for letters in range(0, len(p) - 1):
        if p[letters] != q[letters]:
            count += 1
    
    return count

#start main
genome_file = open("approximatePC.txt", "r")

pattern = genome_file.readline()
sequence = genome_file.readline()
errors = genome_file.readline()
    
print(approximatePC(sequence, pattern, errors))

genome_file.close()