def skew(sequence):
    count = 0
    count_list = []
    count_list.append(str(count))

    for i in range(0, len(sequence)):
        if sequence[i] == 'G':
            count +=1 
            count_list.append(str(count))
        elif sequence[i] == 'C':
            count -= 1
            count_list.append(str(count))
        else:
            count_list.append(str(count))

    return count_list


#start main
genome_file = open("skew.txt", "r")

pattern = genome_file.readline()
    
counts = ' '.join(skew(pattern))
print(counts)

genome_file.close()