import matplotlib.pyplot as plt
import numpy as np
import GetData as GD
import pandas as pd 
 
# create data
x=range(1,41)
values=np.random.uniform(size=40)
 
# stem function
plt.stem(x, values)
plt.ylim(0, 1.2)
plt.show()
 
# stem function: If x is not provided, a sequence of numbers is created by python:
plt.stem(values)
plt.show()