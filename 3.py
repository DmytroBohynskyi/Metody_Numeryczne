"""
Dmytro Bohynskyi 171699: 9+9 = 18
__version__ = Lab_10
"""
from math import exp


def function(y, t):
    return y * (1 - y) * (t - 2)


def euler_method(time_start: int, time_end: int, f, h_: int):
    for t in range(time_start, time_end, h_):
        yield f
        f = f + function(f, t) * h_


def heun_method(time_start: int, time_end: int, f, h_: int):
    for t in range(time_start, time_end, h_):
        yield f
        f_o = function(f, t)
        f_1 = f + f_o * h_
        f = f + (f_o + function(f_1, t + h)) * (h / 2)


def start_point(time_start: int, time_end: int, f, h_: int):
    for t in range(time_start, time_end, h_):
        yield f
        f_0 = f + function(f, t) * (h_ / 2)
        f = f + function(f_0, t + (h_ / 2)) * h


if __name__ == '__main__':
    # Input
    h = int(input('Podaj wartość kroku : '))  #
    t_end = int(input('Podaj końcową : '))  # end time
    # Static data
    f = 0.5  # y(0)
    t_st = 1  # start time
    c_1 = 0.223130  # constant

    analitic = (exp((t ** 2) / 2) / (c_1 * exp(2 * t) + exp((t ** 2) / 2)) for t in range(t_st, t_end, h))
    euler = euler_method(t_st, t_end, f, h)
    heun = heun_method(t_st, t_end, f, h)
    point = start_point(t_st, t_end, f, h)

    # Print data
    print(f'\n|{"Analitycznie":<15}|{"Elera ":<15}|{"Heuna":<15}|{"P. środkowego":<15}|\n{"-":-^65}')
    for a, e, h, p, in zip(analitic, euler, heun, point, ):
        print(f'|{a:<15,.5}|{e:<15,.5}|{h:<15,.5}|{p:<15,.5}|')
