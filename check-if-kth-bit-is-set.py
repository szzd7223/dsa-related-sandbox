def setOrNot(num, k):
    num = num >> k
    if num & 1 == 1:
        return True
    else:
        return False
    
print(setOrNot(13, 1))