from manim import *
import numpy as np
from scipy.integrate import quad
import time

start = time.time()
def a_n(func, T, dt, omega):
    def f(t):
        return func(t) * np.cos(omega*t)
    a_n = (2/T) * quad(f, dt[0], dt[1])[0]
    return a_n


def b_n(func, T, dt, omega):
    def f(t):
        return func(t)*np.sin(omega*t)
    b_n = (2/T) * quad(f, dt[0], dt[1])[0]
    return b_n


def fourier_1_re(t):
    T = 7
    N = 20
    dt = [1,8]
    func = lambda t: 2 if 1 <= t <= 5 else 10
    y = a_n(func, T, dt, 0)/2 #нулевой коэф

    for n in range(1, N+1):
        omega = (2*np.pi*n)/T
        y += a_n(func, T, dt, omega) * np.cos(omega*t) + b_n(func, T, dt, omega) * np.sin(omega*t)
    return y


class Example(Scene):

    def construct(self):
        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[0, 11, 1],
            axis_config={'color': GREEN},
            x_axis_config={
                'numbers_to_include': np.arange(0, 9, 1),
                'numbers_with_elongated_ticks': np.arange(0, 9, 2)
            },
            y_axis_config={
                'numbers_to_include': np.arange(0, 10.1, 2),
                'numbers_with_elongated_ticks': np.arange(0, 10, 2)
            },
            tips=False
        )
        axes_labels = axes.get_axis_labels()
        graph_1 = axes.plot_line_graph([1, 5, 5, 8], [2, 2, 10, 10])

        graph_1_fourier = axes.plot(fourier_1_re, color=RED)

        plot = VGroup(axes, axes_labels, graph_1, graph_1_fourier)
        self.add(plot)

        finish = time.time()
        print(finish-start)