from matplotlib import pyplot as plt
# import numpy as np

# Draws two functions that show the problem in the same plot

# 100 linearly spaced numbers
x = np.linspace(0,20,100) # should be adjusted flexibly according to different data

# some constants to use
FV = 1000 # face value
C = 50 # coupon payment
P = 900 # current price
n = 10 # number of payments

# We are looking for Y, i.e. yield to maturity
# Which can be expressed as two functions between y and x
# With y = (1+Y)^(-n)
# And x = 1/Y

# function 1
y = (1 + 1/x) ** (-n)
# function 2, using z to represent y
z = (FV-P) / (C*x - FV) + 1

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot function 1
plt.plot(x,y, 'r')
plt.plot(x,z, 'g')

# show the plot
plt.show()
