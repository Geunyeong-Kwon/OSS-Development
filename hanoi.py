def hanoi(n, a, b, c):
    if n == 1:
        print(a, '->', b)
        return
    
    hanoi(n-1, a, c, b)
    print(a, '->', b)
    hanoi(n-1, c, b, a)

print('n = 3')
hanoi(3, 1, 2, 3)