# Using right shift
def setOrNotRs(num, k):
    num = num >> k
    if num & 1 == 1:
        return True
    else:
        return False
    
def setOrNotLs(num, k):
    if num & (1 << k) != 0:
        return True
    else:
        return False
    
num = 13
k = 2

print(setOrNotRs(num, k))
print(setOrNotLs(num, k))