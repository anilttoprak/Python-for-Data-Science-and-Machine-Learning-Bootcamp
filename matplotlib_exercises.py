# Follow the instructions to recreate the plots using this data:

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**

import matplotlib.pyplot as plt
# plt.show()

"""Exercise 1"""

# Follow along with these steps:
# Create a figure object called fig using plt.figure()
# Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
# Plot (x,y) on that axes and set the labels and titles to match the plot below:

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
# plt.show()

"""Exercise 2"""

# Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
# ** Now plot (x,y) on both axes. And call your figure object to show it.**

fig = plt.figure()

axes1 = fig.add_axes([0,0,1,1]) 
axes2 = fig.add_axes([0.2,0.5,.2,.2])
axes1.plot(x, y,"red")
axes2.plot(x, y,"red")
axes2.set_xlabel('x')
axes2.set_ylabel('y')
# plt.show()

"""Exercise 3"""

# Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
# Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:

fig = plt.figure()

axes1 = fig.add_axes([0,0,1,1]) 
axes2 = fig.add_axes([0.2,0.5,.4,.4])
axes1.plot(x, z,"blue")
axes2.plot(x, y,"blue")
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_xlim(20,22)
axes2.set_ylim(30,50)



"""Exercise 4"""

# Use plt.subplots(nrows=1, ncols=2) to create the plot below.
# Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style
# See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue", lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
