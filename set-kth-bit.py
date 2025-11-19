def setBit(num, k):
        
    num = num | (1 << k)
    
    return num

num = 13

print(setBit(num, 2))