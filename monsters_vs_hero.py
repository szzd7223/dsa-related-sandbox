n = int(input("Enter number of monsters"))
exp = int(input("Enter initial experience"))
p = [int(input("Enter power of monster")) for _ in range(n)]
b = [int(input("Enter bonus of monster")) for _ in range(n)]

a = sorted(zip(p,b))

ans = 0

for power, bonus in a:
    if power > exp:
        break
    exp += bonus
    ans += 1

print(ans)