def newman_conway(num):
   
    if num <= 0:
        raise ValueError("invalid input")
    sequence = [1,1]
    for i in range(2,num):
        sequence.append(sequence[sequence[i-1]-1]+sequence[i-sequence[i-1]])
    return ' '.join(str(i) for i in sequence[:num])