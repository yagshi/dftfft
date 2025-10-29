import cmath
N0 = 8                       # number of data
x = [i for i in range(N0)]   # dummy data to be transformed

def fft(x: list) -> list:
    N = len(x)
    if N == 1:
        return [x[0]]
    W = cmath.rect(1, -2 * cmath.pi / N) # twiddle factor
    xe = x[0::2] # even index data
    xo = x[1::2] # odd index data
    Xe = fft(xe)
    Xo = fft(xo)
    X = [Xe[k % (N // 2)] + W ** k * Xo[k % (N // 2)] for k in range(N)]
    return X

print(fft(x))
