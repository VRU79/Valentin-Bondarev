l = [int(i) for i in input().split(' ')]

mx = max(l)
mn = min(l)

for i in range(len(l)):
    if l[i] == mx:
        l[i] = mn
    elif l[i] == mn:
        l[i] = mx
print(l)
