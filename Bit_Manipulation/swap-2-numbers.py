# Swapping two numbers is pretty easy
# take a temp variable, store value of a in it, then a = b, b = temp and done
# but it uses extra space
# what if there is a way to not use extra space?
# XOR operator comes here
# basically if you xor a number by itself, it results in 0
# so 5 ^ 5 = 0
# now let's say we have to swap two number a and b,
# a = a ^ b
# b = a ^ b = (a ^ b) ^ b = a ^ (b ^ b) = a
# a = a ^ b = (a ^ b) ^ a = b

# code
def swapNumbers(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a, b

a = 5
b = 7
print("before swap: " + "a is " + str(a) + " and b is " + str(b))

a, b = swapNumbers(a,b)

print("after swap: " + "a is " + str(a) + " and b is " + str(b))