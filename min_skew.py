def min_skew(sequence):
    count = 0
    minimum = 0
    count_index = []
    finished_indices = []

    for i in range(0, len(sequence)):
        if sequence[i] == 'G':
            count +=1 
        elif sequence[i] == 'C':
            count -= 1

        if count < minimum:
            minimum = count
        count_index.append(count)

    
    for j in range(0, len(count_index)):
        if count_index[j] == minimum:
            finished_indices.append(str(j + 1))
        
    return finished_indices

#start main
genome_file = open("min_skew.txt", "r")

sequence = genome_file.readline()


indices = ' '.join(min_skew(sequence))
print(indices)
#print(min_skew(sequence))

genome_file.close()