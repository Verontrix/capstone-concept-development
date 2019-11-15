'''
    DrawSystem class
    - draws airplane, fov square, and point in the middle of the fov square
'''

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import ControlsParameters as cp

class DrawSystem :

    def __init__(self):
        self.init_flag = True
        self.airplane = 0
        self.rect = 0
        self.circle = 0
        self.fig, self.ax = plt.subplots() # PLOT

        plt.axis([0, cp.plot_width, 0, cp.plot_height])
        plt.plot(cp.x,cp.y,'--')

    def draw_airplane(self, home):
        pts =np.matrix([
            [home[0],home[1]],
            [home[0]-cp.long_l,home[1]],
            [home[0]-cp.long_l,home[1]-cp.small_l],
            [home[0]-cp.long_l-cp.small_l,home[1]-cp.small_l],
            [home[0]-cp.long_l-cp.small_l,home[1]],
            [home[0]-cp.long_l-cp.small_l-cp.long_l,home[1]],
            [home[0]-cp.long_l-cp.med_l+cp.small_l*2,home[1]+(cp.small_l*1.5)],
            [home[0]-cp.long_l-cp.small_l,home[1]+(cp.small_l*1.5)],
            [home[0]-cp.long_l-cp.small_l,home[1]+(cp.small_l*2)],
            [home[0]-cp.long_l,home[1]+(cp.small_l*2)],
            [home[0]-cp.long_l,home[1]+(cp.small_l*1.5)],
            [home[0]-(cp.small_l),home[1]+(cp.small_l*1.5)],
            [home[0],home[1]+(cp.small_l*3)]]).T

        xy = np.array(pts.T)

        if self.init_flag :
            self.airplane = mpatches.Polygon(xy, facecolor = 'black', edgecolor = 'black')
            self.ax.add_patch(self.airplane)
        else :
            self.airplane.set_xy(xy)

    def draw_fov(self, target) :
        rectangle_start_point = [target[0] - cp.center_of_rect, target[1] - cp.center_of_rect]

        if self.init_flag :
            self.rect = mpatches.Rectangle(rectangle_start_point, cp.fov_len, cp.fov_len,linewidth=1,edgecolor='r',facecolor='none')
            self.circle = mpatches.CirclePolygon(target,radius=15, color='r')
            self.ax.add_patch(self.circle)
            self.ax.add_patch(self.rect)
        else :
            self.rect.set_xy(rectangle_start_point)
            self.circle._xy = target
