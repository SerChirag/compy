from bisect import *
#using binary search is stupid. Coz we already have an O(n) algo for moving elements.
a = [2,3,7,21,42]
b = [1,5,8,12,17,20,35]
if(len(b)>len(a)):
    (a,b) = (b,a)

for i in range(len(b)-1,-1,-1):
    last = a[-1]
    a[-1] = b[i]
    j = len(a)-1
    while(j>0):
        if(a[j]<a[j-1]):
            t = a[j]
            a[j] = a[j-1]
            a[j-1] = t
            j-=1
        else:
            break
    if(j != len(a)-1):
        b[i] = last
    else:
        mini = min(last,b[i])
        maxi = max(last,b[i])
        a[-1] = mini
        b[i] = maxi

print a
print b

