import numpy as np


# -----------------------------------------------------------
# BASIC UTILITIES REQUIRED FOR MAGNETIC FORWARD MODELLING
# -----------------------------------------------------------

def my_deg2rad(angle):
    """Convert degrees to radians."""
    return (angle / 180.0) * np.pi


def my_dircos(inc, dec, azm=0.0):
    """
    Compute direction cosines from inclination and declination.

    Returns:
    xdir, ydir, zdir
    """
    Inc = my_deg2rad(inc)
    Dec = my_deg2rad(dec)
    Azm = my_deg2rad(azm)

    xdir = np.cos(Inc) * np.cos(Dec - Azm)
    ydir = np.cos(Inc) * np.sin(Dec - Azm)
    zdir = np.sin(Inc)

    return xdir, ydir, zdir


def my_log(x):
    """
    Safe logarithm: log(0) handled as 0.
    """
    x = np.asarray(x)
    out = np.log(x)
    out[x == 0] = 0
    return out


def my_atan(x, y):
    """
    Stable arctan function using arctan2 with corrections.
    """
    x = np.asarray(x)
    y = np.asarray(y)

    arctan = np.arctan2(x, y)

    arctan[x == 0] = 0
    arctan[(x > 0) & (y < 0)] -= np.pi
    arctan[(x < 0) & (y < 0)] += np.pi

    return arctan