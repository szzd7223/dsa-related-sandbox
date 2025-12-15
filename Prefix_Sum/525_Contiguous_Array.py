
def findMaxLength(nums):
    prefixSum = 0
    firstIndex = {0: -1}
    maxLen = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            prefixSum -= 1
        else:
            prefixSum += 1

        if prefixSum in firstIndex:
            length = i - firstIndex[prefixSum]
            maxLen = max(maxLen, length)
        else:
            firstIndex[prefixSum] = i

    return maxLen