def clearBit(num, k):
    num = num & (~(num << k))

    return num

num = 13
k = 2

print(clearBit(num, k))