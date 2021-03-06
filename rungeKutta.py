import matplotlib.pyplot as plt

# Equation
def f(x, y):
#    return ((0.1*x) - (0.02*x*y))
    return x

def t4(x, y, h):
    k1 = f(x, y)
    k2 = f(x + (h / 2.0), y + k1*(h/2.0))
    k3 = f(x + (h / 2.0), y + k2*(h/2.0))
    k4 = f(x + h, y + (k3*h))
    return ((1/6.0)*(k1 + 2*k2 + 2*k3 + k4))

#def t4(x, y, h):
#    k1 = f(x, y)*h
#    k2 = f(x + (h/2.0), y + (k1/2.0))*h
#    k3 = f(x + (h/2.0), y + (k2/2.0))*h
#    k4 = f(x + h, y + k3)*h
#    return (x + ((1/6.0)*(k1 + 2*k2 + 2*k3 + k4)))



def rungeKutta(x0, y0, h, iter):
    result = [(x0, y0)]

    x = x0
    y = y0

    for i in range(0, iter):
        yn = y + (h * t4(x, y, h))
        x = x + h
        y = yn
        result.append((x, y))
    return result

if __name__ == '__main__':
    x0 = -4
    y0 = 8
    h = 0.05
    iters = 300
    result = rungeKutta(x0, y0, h, iters)
    print(result)

    axes = plt.gca()
    # X axis range
    axes.set_xlim([-10, 10])
    # Y axis range
    axes.set_ylim([0, 10])

    plt.grid()
    plt.plot([i[0] for i in result], [j[1] for j in result])
    plt.show()