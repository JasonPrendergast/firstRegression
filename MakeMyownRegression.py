from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1,2,3,4,5,6],dtype=np.float64)
ys = np.array([5,4,5,4,6,7],dtype=np.float64)

#plt.scatter(xs,ys)
#plt.show()
#m= mean xs*mean ys - mean xs*ys / mean xs * mean xs - mean x**2 
def best_fit_slope_and_intercept(xs,ys):
    m=(((mean(xs)*mean(ys)) - mean(xs*ys))/
      ((mean(xs)*mean(xs))- mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m

m,b = best_fit_slope_and_intercept(xs,ys)

print(m,b)
