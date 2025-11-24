def isPowerOf2(num):
    if num & (num-1) == 0:
        return True
    return False

print(isPowerOf2(18))