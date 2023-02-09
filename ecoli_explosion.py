from collections import Counter

def find_repeats(sequence, k, window, times):
    sequence_size = len(sequence)
    pattern_length = int(k)
    repeats = []
    
    #to find the repeats in the sequence
    for i in range(0, sequence_size - pattern_length + 1):
        if(sequence[i: i + pattern_length + 1]):
            repeats.append(sequence[i: i + pattern_length])

    #to make dictionary with the counts
    counts = Counter(repeats)
    #print(counts) 
    
    #to add repeats to a new list to return
    repeats = []
    for key, value in counts.items():
        #checking for if it is bigger than time and not already in repeats
      if value >= int(times): #and key not in repeats:
         repeats.append(key)

    return repeats
    
#start main
genome_file = open("ecoli.txt", "r")

sequence = genome_file.readline()

#for ecoli
repeats = ' '.join(find_repeats(sequence, 9, 500, 3))
repeats_len = len(repeats)
print(repeats_len)
f = open("ecoli_results.txt", "w")
f.write(repeats) 
f.close()

genome_file.close()