def numberOfWays(corridor) -> int:
    # Store 1000000007 in a variable for convenience
    MOD = 1_000_000_007

    # Cache the result of each sub-problem
    cache = [[-1] * 3 for _ in range(len(corridor))]

    def count(index, seats):
        # If we have reached the end of the corridor
        if index == len(corridor):
            return 1 if seats == 2 else 0

        # Return cached result if available
        if cache[index][seats] != -1:
            return cache[index][seats]

        # If the current section has exactly 2 "S"
        if seats == 2:
            if corridor[index] == 'S':
                # Must close section, start new one with 1 seat
                result = count(index + 1, 1)
            else:
                # Current is "P", two options:
                # 1. Close section (start new with 0 seats)
                # 2. Keep growing (keep 2 seats)
                result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
        else:
            # Less than 2 seats, keep growing
            if corridor[index] == 'S':
                result = count(index + 1, seats + 1)
            else:
                result = count(index + 1, seats)

        cache[index][seats] = result
        return result

    return count(0, 0)
