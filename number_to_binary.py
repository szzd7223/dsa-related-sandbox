# How do you come to binary representation of a number?
# well, you keep dividing the number by 2 until you reach to the quotient of 0
# then you just retrace the sequence made the the quotient wala 1 and the remainders along the way
# for example, take 13
#   13/2 -> q:6, r:1
#   6/2 -> q:3, r:0
#   3/2 -> q:1, r:1
#   1/2 -> q:0, r:1
#   now I will retrace and I will get 1101

# Code
def numberToBinary(num):
    ans = []
    while num:
        r = num%2
        ans.append(r)
        num = num//2
    
    ans.reverse()
    return ans

print(numberToBinary(13))


# Time complexity -> log(base2)n
# Why? because n keeps getting divided by 2 until it reaches 0

# Space complexity -> log(base2)n
# Why? because there would be log(base2)n number of elements in the answer