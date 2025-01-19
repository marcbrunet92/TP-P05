import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('donnees.csv', delimiter=';', decimal=',')
subset = data[data['y'] == 0]
x, phi = subset['x'].values, subset['V'].values
phi_fit = 0.194*x
plt.plot(x, phi, 'bo-', label="$f(x)=\\varphi$")
plt.plot(x, phi_fit, 'r-', label=f"f(x)=0.194*$\\varphi$")
plt.xlabel("Position $x$ (cm)")
plt.ylabel("$\\varphi(x)$ (V)")
plt.title("Potentiel électrique f(x)=$\\varphi$")
plt.legend()
plt.grid()
plt.show()

x_centers, Ex = (x[:-1] + x[1:]) / 2, -np.diff(phi) / np.diff(x)
plt.plot(x_centers, Ex, 'ro-', label="$E_x(x)$")
plt.xlabel("Position $x$ (cm)")
plt.ylabel("$E_x(x)$ (V/cm)")
plt.title("Champ électrique $E_x(x)$")
plt.legend()
plt.grid()
plt.show()
