def findSeq(a):
    
    seqList = ['ATTTA','GTGTGT','GCTACT']
    a = a.upper()
    return{check:a.count(check) for check in seqList}

seq = input("enter sequence: ")

print(findSeq(seq))