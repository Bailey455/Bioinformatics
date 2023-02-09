def reverse(text):
    sequence_size = len(text)
    reversed_sequence = []

    for i in range(0, sequence_size):
        if text[i] == 'A':
            reversed_sequence.append('T')
        elif text[i] == 'T':
            reversed_sequence.append('A')
        elif text[i] == 'C':
            reversed_sequence.append('G')
        else:
            reversed_sequence.append('C')

        reverse = ''.join(reversed_sequence)

    return reverse

def complement(text):
    return text[::-1]

#start main
genome_file = open("reverse.txt", "r")

sequence = genome_file.readline()

reversed = reverse(sequence)
print(complement(reversed))

genome_file.close()
