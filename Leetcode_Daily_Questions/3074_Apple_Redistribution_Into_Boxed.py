
def minimumBoxes(apple, capacity):
    total_apples = sum(apple)
    capacity.sort(reverse=True)
    need = 0
    while total_apples > 0:
        total_apples -= capacity[need]
        need += 1
    return need
