# pattern searching

S='JBABCABCABHJHGJABCABCABCABCABABCABCABCABCAC'
p='ABCAB'
for i in range(len(S)):
    if p in S:
        e=(S.index(p))
        print(e)
        if(S[e]==p[0]):
                S=list(S)
                S[e]=" "
                e=e+1
        S=''.join(S)
