# def seqOverlap(seq1,seq2):
#     seq1 = seq1.upper()
#     seq2 = seq2.upper()

    
li = ['a','b','c','d']
a = []
for i in li:
    if len(a) == 0:
        a.extend(i)
        # print(a)
    else:
        var = ''.join([a[0],i])
        a.insert(0,var)
        # print(var)
    
print(a)