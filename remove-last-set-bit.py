def clearLastSetBit(num):
    num = num & (num-1)
    return num

print(clearLastSetBit(16))