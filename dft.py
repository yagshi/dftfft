import cmath
N = 8                                # number of data
x = [i for i in range(N)]            # dummy data to be transformed
W = cmath.rect(1, -2 * cmath.pi / N) # twiddle factor
X = [sum([x[n] * W ** (k * n) for n in range(N)]) for k in range(N)]
print(X)
