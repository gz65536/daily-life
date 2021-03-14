from matplotlib import pyplot as plt
import numpy as np
import math

# Draws two functions that show the problem in the same plot

# some constants to use
FV = 1000 # face value
C = 50 # coupon payment
P = 900 # current price
n = 10 # number of payments

# 100 linearly spaced numbers
x = np.linspace(0,math.ceil(FV/C),num=500) # should be adjusted flexibly according to different data

# We are looking for Y, i.e. yield to maturity
# Which can be expressed as two functions between y and x
# With y = (1+Y)^(-n)
# And x = 1/Y

# function 1
y = (1 + 1/x) ** (-n)
# function 2, using z to represent y
z = (FV-P) / (C*x - FV) + 1

fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['bottom'].set_position('zero')

# plot functions
plt.plot(x,y, 'r')
plt.plot(x,z, 'g')
plt.ylim([0, 1])

# plot intersection
# Find the index at which `y-z` is nearest to 0
ind_cross = np.argmin(np.fabs(y-z))
# Plot vertical line there
plt.axvline(x[ind_cross], color='0.5', ls=':', label='Y='+'{:.2f}'.format(100/x[ind_cross])+'%')

# show the plot
plt.grid()
plt.legend()
plt.show()
