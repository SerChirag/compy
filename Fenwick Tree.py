def get(fen,n,i):
    s = 0
    i+=1 
    while(i > 0):
        s += fen[i]
        i -= i & (-i)
    return s

def update(fen,n,i,val):

    i+=1
    while(i <= n):
        fen[i] += val
        i += i & (-i)

def construct(a):
    fen = [0]*(len(a)+1)
    for i in range(len(a)):
        update(fen,len(a),i,a[i])
    return fen

a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
fen = construct(a)
update(fen,len(a),0,-5)
print get(fen,len(a),6)