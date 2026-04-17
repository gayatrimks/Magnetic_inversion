import numpy as np
from codes import auxiliars


# -----------------------------------------------------------
# TOTAL FIELD MAGNETIC ANOMALY
# -----------------------------------------------------------

def my_prism_tf(x, y, z, prism, mag, inc, dec, incs=None, decs=None, azim=0.):
    """
    Compute total field magnetic anomaly of a rectangular prism.

    Inputs:
    x, y : observation grid (numpy arrays)
    z    : observation height
    prism: [x0, x1, y0, y1, z0, z1, magnetization]
    mag  : magnetization magnitude
    inc, dec   : inducing field inclination and declination
    incs, decs : source magnetization direction (optional)

    Output:
    tfa : total field anomaly (nT)
    """

    if x.shape != y.shape:
        raise ValueError("x and y must have same shape")

    # constants
    t2nt = 1e9
    cm = 1e-7

    # default source direction = field direction
    if incs is None:
        incs = inc
    if decs is None:
        decs = dec

    # direction cosines
    Ma, Mb, Mc = auxiliars.my_dircos(incs, decs, azim)
    Fa, Fb, Fc = auxiliars.my_dircos(inc, dec, azim)

    MF = [
        Ma * Fb + Mb * Fa,
        Ma * Fc + Mc * Fa,
        Mb * Fc + Mc * Fb,
        Ma * Fa,
        Mb * Fb,
        Mc * Fc
    ]

    # prism geometry
    A = [prism[1] - x, prism[0] - x]
    B = [prism[3] - y, prism[2] - y]
    H = [prism[5] - z, prism[4] - z]

    tfa = np.zeros_like(x)

    # main computation
    for k in range(2):
        mag *= -1
        H2 = H[k] ** 2
        for j in range(2):
            Y2 = B[j] ** 2
            for i in range(2):
                X2 = A[i] ** 2
                AxB = A[i] * B[j]
                R2 = X2 + Y2 + H2
                R = np.sqrt(R2)
                HxR = H[k] * R

                tfa += ((-1.) ** (i + j)) * mag * (
                        0.5 * MF[2] * auxiliars.my_log((R - A[i]) / (R + A[i])) +
                        0.5 * MF[1] * auxiliars.my_log((R - B[j]) / (R + B[j])) -
                        MF[0] * auxiliars.my_log(R + H[k]) -
                        MF[3] * auxiliars.my_atan(AxB, X2 + HxR + H2) -
                        MF[4] * auxiliars.my_atan(AxB, R2 + HxR - X2) +
                        MF[5] * auxiliars.my_atan(AxB, HxR)
                )

    return tfa * t2nt * cm