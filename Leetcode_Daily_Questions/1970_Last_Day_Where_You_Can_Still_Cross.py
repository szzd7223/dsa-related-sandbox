from collections import deque
def latestDayToCross(row, col, cells) -> int:
    left, right = 1, len(cells)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if canCross(row, col, cells, mid):
            ans = mid  # This day is possible, try later
            left = mid + 1
        else:
            right = mid - 1  # Too much water, try earlier

    return ans

def canCross(row, col, cells, day):
    grid = [[0] * col for _ in range(row)]

    # Mark water cells
    for i in range(day):
        r, c = cells[i]
        grid[r - 1][c - 1] = 1

    queue = deque()
    visited = set()

    # Add top row land cells
    for c in range(col):
        if grid[0][c] == 0:
            queue.append((0, c))
            visited.add((0, c))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()
        if r == row - 1:
            return True  # Reached bottom

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < row
                and 0 <= nc < col
                and grid[nr][nc] == 0
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append((nr, nc))

    return False
