def removeNum(num, k):
    nums = []

    for i in range(len(num)):
        if num[i] == k:
            temp = num[:i] + num[i+1:]
            nums.append(temp)
    
    return str(max(nums))

num = "21232"
k = "3"

print(removeNum(num, k))