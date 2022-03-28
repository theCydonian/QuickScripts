import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

dims = np.array([2560,1600])
diag = 337.84

obj_size = [200,100]

conv_factor = np.linalg.norm(dims)/diag

obj_size = conv_factor * np.array(obj_size)

image = np.zeros(dims[::-1])

def f(x, y, fill = False, tolerance = 1):
    vc_dist = abs(y - dims[1] // 2)
    h_line = abs(vc_dist - obj_size[1] // 2) <= tolerance
    v_bound = vc_dist <= obj_size[1] // 2 + tolerance

    hc_dist = abs(x - dims[0] // 2)
    v_line = abs(hc_dist - obj_size[0] // 2) <= tolerance
    h_bound = hc_dist <= obj_size[0] // 2 + tolerance

    if fill:
        return 255 if (h_bound and v_bound) else 0
    return 255 if (h_line and h_bound or v_line and v_bound) else 0

for x in range(dims[0]):
    for y in range(dims[1]):
        image[y][x] = f(x,y)


cv.imwrite("out.png", image)
