def getMaxFromBuiltArray(n):
    arr = [0] * (n+1)
    arr[0] = 0
    arr[1] = 1
    for i in range(1, (n//2)+1):
        if i*2 < len(arr):       
            arr[i*2] = arr[i]
        if (i*2)+1 < len(arr):
            arr[(i*2)+1] = arr[i] + arr[i+1]
    print(arr)
    print(max(arr))

getMaxFromBuiltArray(4)