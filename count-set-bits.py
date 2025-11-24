# Normal brute force
# def countSetBits(num):
#     count = 0
#     while num > 0:
#         if num % 2 == 1:
#             count += 1
#         num = num // 2
        
#     return count

# Bitwise operations
# def countSetBits(num):
#     count = 0
#     while num:
#         count += num & 1
#         num = num >> 1
#     return count

# Even more efficient bitwise
def countSetBits(num):
    count = 0
    while num:
        num = num & (num-1)
        count += 1
    return count

print(countSetBits(31))