def patternCount(sequence, pattern):
    sequence_size = len(sequence)
    pattern_size = len(pattern)
    count = 0
    for i in range(0,sequence_size-pattern_size+1):
        if sequence[i:i+pattern_size] == pattern:
            count+=1
    return count
 
#start main
genome_file = open("pattern_count.txt", "r")

sequence = genome_file.readline()
pattern = genome_file.readline()


print(patternCount(sequence, pattern))

genome_file.close()
