from manim import *
import numpy as np


def integer(f, T, dt): # интегрирование по Риману
    h_rim = 0.05  # мелкость разбиения
    N_rim = np.linspace(dt[0], dt[1], num=int(T / h_rim))  # разбиение промежутка длинной T

    coef = [f(i) * h_rim for i in N_rim]  # массив i-x сумм
    return sum(coef)  # итоговая частичная сумма

def c_n(func, T, dt, com_omega): # комплексный коэф
    def f(t): # реализация формулы комплексного коэфа
        return func(t) * np.exp(-com_omega * t) # com_omega = (2pin/T)j
    return (1 / T) * integer(f, T, dt) # окончательное значение


def fourier_1_im(t): #Комплексная функция Фурье
    T = 4  # период
    N = 3  # Предел суммы ряда
    dt = [-1, 3]  # Рассматриваемый промежуток длинной Т

    # func = lambda t: 2 if 1 <= t <= 5 else 10  # 1 функция
    # func = lambda t: abs(t)  # 2 функция
    # func = lambda t: 3*t # 3 функция
    func = lambda t: t**3 - 3*t**2 # 4 функция

    y = 0 #инициализация переменной для суммы
    c = {}
    for n in range(-N, N + 1): #Цикл суммирования
        com_omega = complex(0, (2 * np.pi * n) / T) # Комплексная частота
        y += c_n(func, T, dt, com_omega) * np.exp(com_omega * t) #формула
        c[n] = c_n(func, T, dt, com_omega)
    print('c_n = ', c)
    return y #возврат разложенной в ряд функции


class Example(Scene):

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],  # промежуток по x
            y_range=[-13, 13, 1],  # промежуток по y
            axis_config={'color': GREEN},  # цвет осей
            x_axis_config={
                'numbers_to_include': np.arange(-4, 4.1, 1),  # позиции нумерации для x
                'numbers_with_elongated_ticks': np.arange(-4, 4.1, 2)  # позиции длинных рисок для x
            },
            y_axis_config={  # аналогично
                'numbers_to_include': np.arange(-13, 13.1, 2),
                'numbers_with_elongated_ticks': np.arange(-13, 13.1, 5)
            },
            tips=False
        )
        axes_labels = axes.get_axis_labels() #подписи осей
        title = Text("N = 3", color=WHITE).to_edge(UL).shift([2, 0, 0])

        # graph_1 = axes.plot_line_graph([1, 5, 5, 8], [2, 2, 10, 10])  # 1 функция
        # graph_1 = axes.plot(lambda t: abs(t), color=BLUE)  # 2 функция
        # graph_1 = axes.plot(lambda t: 3*t, color=BLUE)  # 3 функция
        graph_1 = axes.plot(lambda t: t**3 - 3*t**2, color=BLUE)  # 3 функция

        graph_1_fourier = axes.plot(fourier_1_im, color=RED) #график разложенной в ряд функции

        plot = VGroup(axes, title, axes_labels, graph_1, graph_1_fourier) #группировка
        self.add(plot) #добавление на Scene
