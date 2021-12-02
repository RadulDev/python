def countNucli(seq):
    
    seq = seq.upper()
    print(seq)
    return{nucli:seq.count(nucli) for nucli in 'ATGC'}

seq = input('enter a nucleotide sequsence : ')

print(countNucli(seq))