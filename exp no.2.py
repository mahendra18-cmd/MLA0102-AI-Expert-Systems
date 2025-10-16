def hanoi(n, src, aux, dst):
    if n == 1:
        print(src, "→", dst)
    else:
        hanoi(n-1, src, dst, aux)
        print(src, "→", dst)
        hanoi(n-1, aux, src, dst)

hanoi(3, 'A', 'B', 'C')
