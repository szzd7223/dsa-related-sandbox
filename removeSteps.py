def func(arr):
    count = 0


    if len(arr) > 1:
        arr.sort()
        l = 0
        r = len(arr)

        while arr:
            if arr[0] != arr[-1]:
                arr.pop()
                arr.pop(0)
                count+=1
            else:
                arr.pop(0)
                count+=1

    return count

print(func([1, 2, 2, 1, 1, 1]))
                