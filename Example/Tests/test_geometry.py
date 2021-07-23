import math

import pytest

from Example.geometry import Geometry


def test_bhaskara_pass():
    x_1, x_2 = Geometry.bhaskara_roots(a=1, b=8, c=-9)

    assert x_1 == 1
    assert x_2 == -9


def test_bhaskara_error():
    x_1, x_2 = Geometry.bhaskara_roots(a=1, b=8, c=-9)

    assert x_1 == 0
    assert x_2 == 0


def test_rad_convert():
    rad_ang = 3*math.pi / 2
    deg = Geometry.rad_to_degrees(rad=rad_ang)

    assert deg == 270
