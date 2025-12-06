n, k = map(int, input().split())

revenues = list(map(int, input().split()))

def delAnalytics(revenues, k):
    prefix_count = {0: 1}
    prefix_sum = 0
    total_periods = 0

    for value in revenues:
        prefix_sum += value

        if (prefix_sum - k) in prefix_count:
            total_periods += prefix_count[prefix_sum - k]

        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    
    return total_periods

print(delAnalytics(revenues, k))