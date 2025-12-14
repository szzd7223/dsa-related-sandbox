def checkSubarraySum(nums, k):
    remainder_index = {0: -1}  # remainder -> index
    prefix_sum = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        remainder = prefix_sum % k

        if remainder in remainder_index:
            if i - remainder_index[remainder] >= 2:
                return True
        else:
            remainder_index[remainder] = i

    return False
