#Uses hash values to match string and patterns.
#Time Complexity O(m+n) and O(mn)

d = 256 #number of characters allowed
q = 1000000007 #prime numbers
def search(txt,pat):
    h = 0 #hash value
    ph = 0
    num = len(pat)
    count = 0
    lehsun = pow(d,len(pat)-1,q)
    for i in range(len(pat)):
        ph = (d*ph + ord(pat[i]))%q
        h = (d*h + ord(txt[i]))%q
    
    for i in range(len(txt)-len(pat)+1):
        if(ph == h):
            # Start Matching
            flag = 1
            for j in range(len(pat)):
                if(txt[j+i] == pat[j]):
                    pass
                else:
                    flag = 0
                    break
            if(flag):
                print "Found at",i

        
        try:
            h = (d*(h-ord(txt[i])*lehsun) + ord(txt[i+len(pat)]))%q
            if(h < 0):
                h += q
        except:
            pass



txt = "GEEKS FOR GEEKS"
pat = "GEEKS"
search(txt,pat)
