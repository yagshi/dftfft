import cmath


# bitwise reverse order 01234567 -> 04261537
def initial_sort(x: list) -> list:
    binlen = len(f'{len(x):b}')
    i = sorted(range(len(x)), key=lambda a: int(f'{a:0{binlen}b}'[::-1]))
    return [x[j] for j in i]


# bottom-up ward butterfly computation
def fft(xn: list) -> list:
    xk = initial_sort(xn)
    bs = 1  # block size 1, 2, 4, 8, ...
    while bs < len(xk):
        xk2 = []
        wn = cmath.rect(1, -2 * cmath.pi / (bs * 2))
        for i in range(len(xk) // (bs * 2)):  # block index
            for j in range(bs * 2):
                xe0 = bs * i * 2  # index of Xe[0]
                xo0 = xe0 + bs    # index of Xo[0]
                xk2.append(xk[xe0 + j % bs] + wn**j * xk[xo0 + j % bs])
        xk = xk2
        bs *= 2
    return xk


x = [i for i in range(8)]  # sample data to be FFT-ed
print(fft(x))
