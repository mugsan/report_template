import numpy as np
import pylab as pl


def length(x, h):
    a = 1.27
    return (a / h) * x ** 2


x = np.linspace(0, 1.4, 10)  # list of x-values
y1 = length(x, 3)  # list of y-values of grade 1
y2 = length(x, 5)  # list of y-values of grade 1
y3 = length(x, 6)  # list of y-values of grade 1
y4 = length(x, 8)  # list of y-values of grade 1

# plot Graphs
pl.figure()
pl.plot(x, y1, 'r-', label="3mm")
pl.plot(x, y2, 'b-', label="5mm")
pl.plot(x, y3, 'g-', label="6mm")
pl.plot(x, y4, 'm-', label="8mm")
pl.savefig("./plot2.png")
pl.close()

# plot Points Length
pl.figure()
pl.plot([0.4, 0.5, 0.6, 0.75, 0.8, 0.9, 1, 1.1, 1.2],
        [0.083, 0.066, 0.094, 0.145, 0.164, 0.207, 0.254, 0.305, 0.362],
        'bo',
        label="5mm")

# Thickness
pl.plot(1, 0.421, 'ro', label="3mm")
pl.plot(1, 0.215, 'go', label="6mm")
pl.plot(1, 0.162, 'mo', label="8mm")

pl.xlabel("L(m)")
pl.ylabel("T(s)")
pl.legend(loc='upper left')
pl.grid(True)
pl.savefig("plot.png")
pl.close()
