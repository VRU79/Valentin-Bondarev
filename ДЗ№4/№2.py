s = [int(i) for i in input().split()]
a = list()
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        a.append(s[i])
print(" ".join(str(i) for i in a))


