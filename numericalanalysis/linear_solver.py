from numericalanalysis.matrix_helper import zeros_vector


def solve(l, u, b):
    """
    TODO: Fix that
    """
    n = l.shape[0]

    y = zeros_vector(n)
    x = zeros_vector(n)

    y[0] = b[0] / l[0][0]
    for i in range(1, n):
        sum = 0.0
        for j in range(i):
            sum += l[i][j] * y[j]
        y[i] = (b[i] - sum) / l[i][i]

    x[n - 1] = y[n - 1] / u[n - 1][n - 1]
    for i in range(n - 1, -1, -1):
        sum = y[i]
        for j in range(i + 1, n):
            sum = sum - u[i][j] * x[j]
        x[i] = sum / u[i][i]

    return y, x