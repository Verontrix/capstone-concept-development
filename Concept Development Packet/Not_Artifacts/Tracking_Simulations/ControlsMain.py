'''
    controls main
    - this code runs with the DrawSystem class and ControlsParameters.py
'''
import hwcounter as counter
import time
from DrawSystem import DrawSystem
import ControlsParameters as cp
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

if __name__ == '__main__':

    ds = DrawSystem()

    # initialize target and home coordinates
    target = [cp.x[0],cp.y[0]]
    home = [cp.x[0],cp.y[0]]

    t = cp.t_begin
    clock_cycles = 8e10
    # draw initial plane and fov
    ds.draw_airplane(home)
    ds.draw_fov(target)
    ds.init_flag = False
    t_temp = 0
    start_time = counter.count()
    while t < cp.t_end :
        # Add the patch to the Axes
        plt.pause(.005) 
        t = t + 1
        t_temp = t_temp + 1
        # update home coordinates (tracking plane)
        home[0] = cp.x[t] + 105
        # print("Theta is equal to: ", (180/np.pi)*cp.theta[t], "at: ", t)
        home[1] = cp.y[t] - 15

        # update target coordinates (tracking target)
       

        # update plane and fov with new coordinates
        ds.draw_airplane(home)
        #12.5 is about half a second
        if t_temp > 12.5:
            t_temp = 0
            target[0] = cp.x[t]
            target[1] = cp.y[t]
            ds.draw_fov(target)

    elapsed_time = counter.count_end()-start_time
    print(elapsed_time)
    plt.show()
    
    