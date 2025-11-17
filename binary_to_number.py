# How to convert binary to number?
# Take an example, 1101
# each place is 2 to the power
# so here, 1   1   0   1
#          2^3 2^2 2^1 2^0
# and the umber would be:
# number = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 13
# the formula is, number = (binary digit) * 2^(place starting from 0) + ...

# code
def binaryToNum(num):
    ans = 0
    i = 0
    while num:
        last_digit = num % 10
        ans += (last_digit) * (2 ** i)
        i += 1
        num = num//10
    
    return ans

print(binaryToNum(1101))

# Time complexity -> O(log(base10)n)
# Why? Because loop runs until n=0 and each time n is divided by 10. That means it is log(base10)n

# Space complexity -> O(1)
# Why? Because I am using an integer (and 2 other variables) for answer, which would take constant space