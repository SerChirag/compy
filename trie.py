_end = '_end_'

    

def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root



def insert(t,word):
    current_dict = t
    for letter in word:
        try:
            current_dict = current_dict[letter]
        except:
            current_dict[letter]={}
            current_dict = current_dict[letter]
            
    current_dict[_end] = _end


def in_trie(t, word):
    current_dict = t
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict:
            return True
        else:
            return False

def delete(t,word):
    if(len(word)==0):
        t.pop(_end)

        if(len(t)==0):
            t.clear()

    else:
        delete(t[word[0]],word[1:])
      
        if(len(t[word[0]]) == 0):
            t.pop(word[0])
        
        
  

def view_all(t,s,a):
    for i in t:
        if(i == _end):
            a.append(s)
        else:  
            view_all(t[i],s+i,a)
            
        



t = make_trie('foo', 'bar', 'baz', 'barz')
a = []
s = ""
view_all(t,s,a)
print a
