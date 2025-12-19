
def findAllPeople(n, meetings, firstPerson):
    from collections import defaultdict
    from heapq import heappush, heappop
    from math import inf

    # Build graph
    graph = defaultdict(list)
    for x, y, t in meetings:
        graph[x].append((t, y))
        graph[y].append((t, x))

    # Earliest time a person learns the secret
    earliest = [inf] * n
    earliest[0] = 0
    earliest[firstPerson] = 0

    # Min-heap instead of queue: (time, person)
    heap = []
    heappush(heap, (0, 0))
    heappush(heap, (0, firstPerson))

    # Dijkstra-style traversal
    while heap:
        time, person = heappop(heap)

        # Skip outdated states
        if time > earliest[person]:
            continue

        for t, next_person in graph[person]:
            if t >= time and earliest[next_person] > t:
                earliest[next_person] = t
                heappush(heap, (t, next_person))

    # Return all people who learned the secret
    return [i for i in range(n) if earliest[i] != inf]
