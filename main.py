import matplotlib.pyplot as plt
import numpy as np
x =np.linspace(0,10)
y =np.sin(x)

#tracer la courbe
plt.plot(x,y)

#ajouter des labels et un titres

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title ('courbe de sin(x)')

plt.show()
