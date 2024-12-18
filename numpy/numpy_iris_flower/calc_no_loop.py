# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    m = len(new_points)
    n = len(points)
    return np.sum(np.square(points.reshape(1, n, 4) - new_points.reshape(m, 1, 4)), axis=2)
