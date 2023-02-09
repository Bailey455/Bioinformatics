def find_repeats(sequence, pattern):
    sequence_size = len(sequence)
    pattern_length = int(k)
    repeats = []
    count = 0
    
    #to find the repeats in the sequence
    for i in range(0, sequence_size - pattern_length):
        if(sequence[i + 1: i + pattern_length + 1]):
            repeats.append(sequence[i + 1: i + pattern_length + 1])
    repeats.sort()

    #to get the max counts of repeats
    run = 0
    count_list = []
    while run < len(repeats) - 1:
        copies = 0
        while repeats[run] == repeats[run + copies]:
            count += 1
            copies += 1
        count_list.append(count)
        run += 1
        count = 0
    
    #to find the indices of the most repeated
    max_indices = []
    max_index = max(count_list)
    for counts in range(0, len(count_list) - 1):
       if count_list[counts + 1] >= max_index:
            #max_indices.append(count_list[counts + 1])
            max_indices.append(repeats[counts + 1])
            max_index = count_list[counts + 1]

    return max_indices
        
#start main
genome_file = open("hidden.txt", "r")

sequence = genome_file.readline()
k = genome_file.readline()

print(find_repeats(sequence, k))


genome_file.close()