def hamming_distance(p, q):
    count = 0

    for letters in range(0, len(p) - 1):
        if p[letters] != q[letters]:
            count += 1
    
    return count

#start main
genome_file = open("hamming_distance.txt", "r")

p = genome_file.readline()
q = genome_file.readline()
    
print(hamming_distance(p, q))

genome_file.close()