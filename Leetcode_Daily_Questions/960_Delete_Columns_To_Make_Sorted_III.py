
def minDeletionSize(A):
    W = len(A[0])
    # dp[i] is the length of LIS ending at index i (conceptually)
    # Here we iterate backwards, so it's starting at i.
    dp = [1] * W

    for i in range(W - 2, -1, -1):
        for j in range(i + 1, W):
            # Check if column i <= column j for all rows
            for row in A:
                if row[i] > row[j]:
                    break
            else:
                # If the inner loop didn't break, columns are compatible
                dp[i] = max(dp[i], 1 + dp[j])

    return W - max(dp)
