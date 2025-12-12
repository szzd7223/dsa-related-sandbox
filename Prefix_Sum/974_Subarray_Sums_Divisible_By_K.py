def subarraysDivByK(nums, k):
        count = {0: 1}  # remainder → frequency
        prefix = 0
        res = 0
        
        for num in nums:
            prefix += num
            # normalize negative remainders
            remainder = prefix % k  
            
            if remainder in count:
                res += count[remainder]
                count[remainder] += 1
            else:
                count[remainder] = 1
        
        return res
