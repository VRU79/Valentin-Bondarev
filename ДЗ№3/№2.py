def counting_zero(m):
    k = 0
    for i in range(len(m)):
        if m[i] == 0:
            k += 1
            return k

'''Ввод данных'''
m = list()
for i in range(10):
    m.append(int(input()))

print(counting_zero(m))

