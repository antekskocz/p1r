import matplotlib.pyplot as plt
from math import sin, tan


def frange(a, b, step):
    result = []
    r = a
    while r < b:
        result.append(r)
        r += step
    return result


def plotf(f, a, b, step):
    xs = frange(a, b, step)
    ys = [f(i) for i in xs]

    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graph of f(x)")
    plt.grid(True)
    plt.show()


def _plotsin(a=-3, b=3, step=0.01):
    plotf(lambda x: x * m.sin(x) - x**2, a, b, step)


def _trigplot():
    a = float(input())
    b = float(input())
    step = float(input())

    xs = frange(a, b, step)

    plt.plot(xs, [x for x in xs], label="f(x) = x")
    plt.plot(xs, [sin(x) for x in xs], label="f(x) = x sin x")
    plt.plot(xs, [tan(x) for x in xs])

    plt.xlabel("x")
    plt.xlabel(r"f(x)")
    plt.legend()
    plt.show()


_trigplot()
