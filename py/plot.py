import numpy as np
import pylab as pl
import math as m


def time(l, d, e, roh):
    '''
    @param l length in m
    @param d height in m
    @param e e-module in Pa
    @param roh density in kg / m^3
    '''
    const = 6.447
    return const * (l**2 * m.sqrt(roh)) / (d * m.sqrt(e))


l = np.linspace(0, 1.4, 90)  # list of lengths
d = np.linspace(0.001, .01, 90)  # list of heights

# Linearization tables
ln_l = [-0.693147181,
        -0.510825624,
        -0.287682072,
        -0.223143551,
        -0.105360516,
        0,
        0.09531018,
        0.182321557]

ln_t = [-2.7181,
        -2.36446,
        -1.93102,
        -1.80789,
        -1.57504,
        -1.37042,
        -1.18744,
        -1.01611]

# Time as function of Length.
# E   = 200 GPa (steel)
# roh = 7761 kg/m^3 (steel)
pl.figure()
# plot time(l)
pl.plot(l,
        time(l, .005, 200 * 10 ** 9, 7761),
        'b-',
        label=r'$T(l) = 6.45\cdot\frac{l^2\sqrt{7761kg/m^3}}{5mm\cdot\sqrt{200GPa}}$')

# plot meassured points
pl.plot([0.5, 0.6, 0.75, 0.8, 0.9, 1, 1.1, 1.2],
        [0.066, 0.094, 0.145, 0.164, 0.207, 0.254, 0.305, 0.362],
        'ro')

pl.xlabel("l(m)")
pl.ylabel("T(s)")
pl.legend(loc='upper left')
pl.grid(True)
pl.savefig("../png/length.png")

# Plot Linearization tables
pl.figure()
pl.plot(ln_l, ln_t, 'r^')
z = np.polyfit(ln_l, ln_t, 1)
p = np.poly1d(z)
pl.plot(ln_l, p(ln_l), 'b--')
pl.xlabel("ln l")
pl.ylabel("ln t")
pl.legend(loc='upper left')
pl.grid(True)
pl.savefig("../png/ln_t_ln_l.png")


# plot Time as function of Height
pl.figure()
pl.plot(d,
        time(1, d, 200 * 10 ** 9, 7761),
        'b-',
        label=r'$T(d) = 6.45\cdot\frac{1m\cdot\sqrt{7761kg/m^3}}{d\cdot\sqrt{200GPa}}$')

# plot meassured points
pl.plot([.003, .005, .006, .008],
        [.421, .254, .215, .165],
        'ro')

pl.xlabel("d(m)")
pl.ylabel("T(s)")
pl.legend(loc='upper right')
pl.grid(True)
pl.savefig("../png/height.png")

# Different materials.
pl.figure()
l = np.linspace(.98, 1.025, 100)
pl.plot(l, time(l, .005, 69 * 10 ** 9, 2747.6), 'b-', label="Aluminum")
pl.plot(l, time(l, .008, 102 * 10 ** 9, 8487.5), 'g-', label="Brass")
pl.plot(l, time(l, .005, 200 * 10 ** 9, 7761), 'r-', label="Steel")
pl.plot(1, .252, 'bo')
pl.plot(1, .232, 'go')
pl.plot(1, .254, 'ro')
pl.xlabel("l(m)")
pl.ylabel("T(s)")
pl.legend(loc='upper left')
pl.grid(True)
pl.savefig("../png/plot.png")
