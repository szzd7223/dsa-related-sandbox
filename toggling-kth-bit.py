def toggle(num, k):
    if  num & (1 << k) != 0:
        num = num & (~(1 << k))
    else:
        num = num | (1<<k)
    
    return num

print(toggle(13, 2))
