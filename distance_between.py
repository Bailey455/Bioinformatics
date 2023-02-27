def DistanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0

    for section in dna:
        hamming_distance = k
        for i in range(0, len(section) - k):
            pat_prime = section[i:i + k]
            if hamming_distance >  hamming_distance(pattern, pat_prime):
                hamming_distance = hamming_distance(pattern, pat_prime)
        distance = distance + hamming_distance

    return distance

def hamming_distance(p, q):
    count = 0
 
    for letters in range(0, len(p) - 1):
        if p[letters] != q[letters]:
            count += 1
    
    return count

#start main
genome_file = open("motif_enum.txt", "r")

pattern  = genome_file.readline()
input = genome_file.readline()
dna = input.split()

    
print(DistanceBetweenPatternAndStrings(pattern, dna))

genome_file.close()