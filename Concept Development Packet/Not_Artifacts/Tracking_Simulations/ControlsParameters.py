'''
Controls Parameters

'''
import numpy as np

# values that can be changed
linspace_size = 5000   # largest value for linspace
x_center = 1395 # x-coordinate for center of airplane's path
y_center = 960  # y-coordinate for center of airplane's path
radius = 500    # radius of our current path for the airplane
t_begin = 0     # start time for the while loop in main function
t_end = 5000     # stop time for the while loop in main function
plot_width = 2790
plot_height = 1920
# parameters for shape of airplane
long_l = 100
med_l = 80
small_l = 20


# values that cannot be changed
fov_len = 127   # this is the width of the square for the field of view (fov)
center_of_rect = int(fov_len/2) # this allows us to know where the center of the fov is

# values that help to create the airplane's path
N = np.linspace(0, linspace_size, 5001) # number of points
theta = (2*N*np.pi)/linspace_size

# path of airplane
x = 2*radius*np.cos(theta) + x_center
y = radius*np.sin(theta) + y_center

'''
How often does this happen?
How are you fixing it now? As we understand the positioner will just scan.
Would it be weird to have the user take over when the power goes out? (i.e. an interactive GUI from which to control the positioner)
Spoke with Nathan, Mark hurt his back... poor guy
Mark's cell:385 375 0884 
How fast are your drone's flying?
'''