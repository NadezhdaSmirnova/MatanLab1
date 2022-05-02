import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import *

print("Ожидаемое значение:" + str(12/math.log(4)))

def integral(num_of_points, sposob_osnashenia):
  y = lambda a: 4**a
  a = np.linspace(1, 2, 10000)
  fig = plt.figure(figsize=(16 *2/3, 8*2/3))
  ax = fig.add_subplot()
  plt. plot(a, y(a), color =(0.1, 0.5, 0.9))
  
  x = [0] * num_of_points
  for i in range (num_of_points):
      x[i] = 1 + i/(num_of_points - 1)
  e = [0] * (num_of_points - 1)
  dx = 1/num_of_points
  
  if sposob_osnashenia == 1:
    for i in range (num_of_points - 1):
      e[i] = 1 + (i+1)/(num_of_points - 1)
  if sposob_osnashenia == 0:
    for i in range (num_of_points - 1):
      e[i] = 1 + (i+0.5)/(num_of_points - 1)
  if sposob_osnashenia == -1:
    for i in range (num_of_points - 1):
      e[i] = 1 + i/(num_of_points - 1)
      
  sum = 0
  for i in range (num_of_points - 1):
    sum += 4**e[i] * dx
    rect = Rectangle((x[i], 0), dx, y(e[i]), edgecolor = (1, 0, 0.5), fill=False)
    ax.add_patch(rect)
    
  print("\n")
  print("Сумма:" + str(sum))
  plt.show()

integral(30, 1)
integral(30, 0)
integral(30, -1)
integral(239, -1)
integral(566, 1)
