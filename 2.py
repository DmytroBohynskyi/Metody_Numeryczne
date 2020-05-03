# Dmytro Bohynskyi
# Import python modul
import math as mat
# Import
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fmin


def odp_skokowa(t, data):
    tau, tauz, k, dzeta = data

    buf_1 = (1 - np.exp(-dzeta * t / tau) / mat.sqrt(1 - dzeta ** 2) * np.sin(
        t * mat.sqrt(1 - dzeta ** 2) / tau + mat.acos(dzeta)))

    buf_2 = tauz * 1 / (tau * mat.sqrt(1 - dzeta ** 2)) * np.exp(-dzeta * t / tau) * np.sin(
        t * mat.sqrt(1 - dzeta ** 2) / tau)

    return k * (buf_1 + buf_2)


def najm_kwad(data):  # rozrzut danych przed regresją
    sum = (odp - odp_skokowa(time, data)) ** 2
    return np.sum(sum)


if __name__ == '__main__':
    dane = np.loadtxt('data/aproksymacja.txt')
    time = dane[:, 0]
    odp = dane[:, 1]

    data = [1.1, -1, 0.8, 0.4]
    x = np.arange(250.) / 20
    y = odp_skokowa(x, data)

    plt.plot(time, odp, label="Dane pomiarowe z pliku")
    tau, tauz, k, dzeta = fmin(najm_kwad, data)

    x = np.arange(250.) / 20
    y = odp_skokowa(x, data)

    plt.plot(x, y, "xr", label="Teoretyczna")
    plt.show()
