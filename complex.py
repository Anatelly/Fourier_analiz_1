from manim import *
import numpy as np


def integer(f, T, dt):  # интегрирование по Риману
    h_rim = 0.05  # мелкость разбиения
    N_rim = np.linspace(dt[0], dt[1], num=int(T / h_rim))  # разбиение промежутка длинной T

    coef = [f(i) * h_rim for i in N_rim]  # массив i-x сумм
    return sum(coef)  # итоговая частичная сумма


def c_n(func, T, dt, com_omega):  # комплексный коэф
    def f(t):  # реализация формулы комплексного коэфа
        Re, Im = func(t)[0:2]  # разделение на вещественную и мнимую части
        return complex(Re, Im) * np.exp(-com_omega * t)  # com_omega = (2pin/T)j

    return (1 / T) * integer(f, T, dt)  # окончательное значение


def fourier_1_im(t):  # Комплексная функция Фурье
    T, R = 6, 3  # заданные значения
    N = 3  # Предел суммы ряда
    dt = [-T / 8, 7 * T / 8]  # Рассматриваемый промежуток длинной Т

    def func(t):
        if -T / 8 <= t < T / 8:
            return np.array((R, (8 * R * t) / T, 0))
        elif T / 8 <= t < 3 * T / 8:
            return np.array((2 * R - (8 * R * t) / T, R, 0))
        elif 3 * T / 8 <= t < 5 * T / 8:
            return np.array((-R, 4 * R - (8 * R * t) / T, 0))
        elif 5 * T / 8 <= t <= 7 * T / 8:
            return np.array((-6 * R + (8 * R * t) / T, -R, 0))

    y = 0  # инициализация переменной для суммы
    # c = {}
    for n in range(-N, N + 1):  # Цикл суммирования
        com_omega = complex(0, (2 * np.pi * n) / T)  # Комплексная частота
        y += c_n(func, T, dt, com_omega) * np.exp(com_omega * t)  # формула
    #     c[n] = c_n(func, T, dt, com_omega)
    # print('c_n =', c)
    return np.array((y.real, y.imag, 0))  # возврат разложенной в ряд функции
    # return y.imag #вещественные и мнимые функции по отдельности

class Example(Scene):
    R = 3
    T = 6

    def func(self, t):
        T = self.T
        R = self.R
        if -T / 8 <= t < T / 8:
            return np.array((R, (8 * R * t) / T, 0))
        elif T / 8 <= t < 3 * T / 8:
            return np.array((2 * R - (8 * R * t) / T, R, 0))
        elif 3 * T / 8 <= t < 5 * T / 8:
            return np.array((-R, 4 * R - (8 * R * t) / T, 0))
        elif 5 * T / 8 <= t <= 7 * T / 8:
            return np.array((-6 * R + (8 * R * t) / T, -R, 0))
        # if -T / 8 <= t < T / 8: #вещественные и мнимые функции по отдельности
        #     return (8 * R * t) / T
        # elif T / 8 <= t < 3 * T / 8:
        #     return R
        # elif 3 * T / 8 <= t < 5 * T / 8:
        #     return 4 * R - (8 * R * t) / T
        # elif 5 * T / 8 <= t <= 7 * T / 8:
        #     return -R

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],  # промежуток по x
            y_range=[-4, 4, 1],  # промежуток по y
            x_length=7,
            y_length=7,
            axis_config={'color': GREEN},  # цвет осей
        ).add_coordinates()

        axes_labels = axes.get_axis_labels(MathTex("Re f(t)"), MathTex("Im f(t)"))  # подписи осей
        # axes_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))  # подписи осей
        title = Text("N = 3", color=WHITE).to_edge(UL).shift([1, 0, 0])

        graph_1 = axes.plot_parametric_curve(self.func, t_range=np.array([-self.T / 8, 7 * self.T / 8]), color=BLUE)
        # graph_1 = axes.plot(self.func, color=BLUE)
        # graph_label = axes.get_graph_label(graph_1, MathTex("Im f(t)"), x_val=-self.T / 8, direction=DL)
        graph_1_fourier = axes.plot_parametric_curve(fourier_1_im, t_range=np.array([-self.T / 8, 7 * self.T / 8]),
                                                     color=RED)

        # graph_1_fourier = axes.plot(fourier_1_im, color=RED)
        # graph_label_fourier = axes.get_graph_label(graph_1_fourier, MathTex("Im G_N(t)"), x_val=5)

        plot = VGroup(axes, axes_labels, graph_1, graph_1_fourier, title)
        # plot = VGroup(axes, axes_labels, graph_1, graph_label, graph_1_fourier, graph_label_fourier, title)  # группировка
        self.add(plot)  # добавление на Scene