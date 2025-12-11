
def subarraySum(nums, k):
    count = 0
    preSum = 0
    prefixSums = {0: 1}

    for n in nums:
        preSum += n
        diff = preSum - k

        count += prefixSums.get(diff, 0)
        prefixSums[preSum] = prefixSums.get(preSum, 0) + 1

    return count