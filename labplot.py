from numpy import *
from pylab import *


def length(x, h):
    a = 1.27
    return (a / h) * x ** 2


x = linspace(0, 1.4, 10)  # list of x-values
y1 = length(x, 3)  # list of y-values of grade 1
y2 = length(x, 5)  # list of y-values of grade 1
y3 = length(x, 6)  # list of y-values of grade 1
y4 = length(x, 8)  # list of y-values of grade 1

# plot Graphs
plot(x, y1, 'r-', label="3mm")
plot(x, y2, 'b-', label="5mm")
plot(x, y3, 'g-', label="6mm")
plot(x, y4, 'm-', label="8mm")

# plot Points Length
plot([0.4, 0.5, 0.6, 0.75, 0.8, 0.9, 1, 1.1, 1.2],
     [0.083, 0.066, 0.094, 0.145, 0.164, 0.207, 0.254, 0.305, 0.362],
     'bo',
     label="5mm")

# Thickness
plot(1, 0.421, 'ro', label="3mm")
plot(1, 0.215, 'go', label="6mm")
plot(1, 0.162, 'mo', label="8mm")

xlabel("L(m)")
ylabel("T(s)")
legend(loc='upper left')
grid(True)

title("Svängningstid")
savefig("./plot.png")
