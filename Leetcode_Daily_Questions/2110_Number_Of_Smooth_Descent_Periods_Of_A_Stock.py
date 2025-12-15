
def getDescentPeriods(prices):
    n = len(prices)
    res = 1  # total number of smooth descending periods, initial value is dp[0]
    prev = 1  # total number of smooth descending periods ending with the previous element

    # traverse the array starting from 1, and update prev and total res
    for i in range(1, n):
        if prices[i] == prices[i - 1] - 1:
            prev += 1
        else:
            prev = 1
        res += prev

    return res
