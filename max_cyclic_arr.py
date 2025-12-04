def maxCyclicArr(arr):
    max_sum = 0
    n = len(arr)
    

    for start in range(n):
        res = []
        for i in range(n):
            res.append(arr[(start+i) % n])
        xor = 0
        total = 0
        for num in res:
            xor = xor ^ num
            total += xor

        max_sum = max(max_sum, total)
        
        res = []
        for i in range(n):
            res.append(arr[(start-i) % n])
        xor = 0
        total = 0
        for num in res:
            xor = xor ^ num
            total += xor

        max_sum =  max(max_sum, total)

    return max_sum

print(maxCyclicArr([1,1,1,1]))