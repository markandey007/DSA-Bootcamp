def pairWiseConsecutive(l):
    
    #add code here
    if len(l) % 2 != 0:
        l.pop()
    
    for i in range(len(l)-1):
        if abs(l[i] - l[i+1]) > 1:
            return False
    if len(l) > 1 and abs(l[-1] - l[-2]) > 1:
        return False
    
    return True
