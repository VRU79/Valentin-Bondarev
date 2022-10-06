def stairs(m):
    for i in range(1, m + 1):
        l = ''
        for j in range(1, i + 1):
            l = l + str(j)
        print(l)
    return 'End'

'''Ввод данных'''
m = 0
m = int(input())

print(stairs(m))

