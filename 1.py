"""
-------------------------------------------------------------------------------
Dla funkcji cos(x) obliczyć przybliżenie pochodnej w punkcie x = 0.5
zgodnie z następującym wzorem: f' = ( f(x + h) - f(x - h)) / 2h
-------------------------------------------------------------------------------
Obliczenia zacząć od h = 0.4 i w kolejnych krokach (w sumie 20) zmniejszać h
pięciokrotnie w stosunku do kroku poprzedniego (czyli h = 0.4, 0.08, 0.016, . . .).

Wyniki przedstawić w postaci tabeli, gdzie w każdym wierszu wypisana zosta-
nie aktualna wartość h, wartość obliczonej pochodnej, oraz wartość bezwzględna

prawdziwego błędu bezwzględnego wyznaczania pochodnej. Przedstawić na wy-
kresie ten błąd jako funkcję od h
"""

import numpy as np
import matplotlib.pyplot as plt


class Lab:

    def __init__(self, x=0.5):
        self.x = x
        self.table = None
        self.h = None
        self.derivative()

    def derivative(self):
        # Create h
        self.h = 0.4 / (5 ** (np.arange(0., 20)))

        # Derivative
        f_dir = (np.sin(self.x + self.h) - np.sin(self.x - self.h)) / (2 * self.h)
        f_tree_dir = np.cos(self.x)

        # Create table
        self.table = np.ones((20, 3))
        self.table[:, 0] = np.arange(1, 21)
        self.table[:, 1] = f_dir
        self.table[:, 2] = np.abs((f_dir - f_tree_dir))


if __name__ == '__main__':
    # Create new object
    object = Lab()

    # Plot my table
    plt.figure()
    plt.plot(object.h, object.table[:, 2])
    # Table label
    plt.xlabel('h')
    plt.ylabel('tab')
    # Table scale
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
