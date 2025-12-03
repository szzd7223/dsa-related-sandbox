import math

tree = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

val = {
    1: 2,
    2: 3,
    3: 6,
    4: 12,
    5: 27
}

def is_square(z):
    r = int(math.isqrt(z))
    return r*r == z

def subtree(u):
    nodes = [u]
    for v in tree[u]:
        nodes += subtree(v)
    return nodes

def beauty(u):
    nodes = subtree(u)
    count = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if is_square(val[nodes[i]] * val[nodes[j]]):
                count += 1
    return count

total = sum(beauty(u) for u in range(1, 6))
print("Total beauty =", total)
