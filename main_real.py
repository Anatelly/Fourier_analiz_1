from manim import *
import numpy as np


def integer(f, T, dt):  # интегрирование по Риману
    h_rim = 0.05  # мелкость разбиения
    N_rim = np.linspace(dt[0], dt[1], num=int(T / h_rim))  # разбиение промежутка длинной T

    coef = [f(i) * h_rim for i in N_rim]  # массив i-x сумм
    return sum(coef)  # итоговая частичная сумма


def a_n(func, T, dt, omega):  # первый коэф
    def f(t):  # реализация формулы первого коэфа
        return func(t) * np.cos(omega * t)  # omega = 2pin/T

    return (2 / T) * integer(f, T, dt)  # окончательное значение


def b_n(func, T, dt, omega):  # второй коэф (все аналогично)
    def f(t):
        return func(t) * np.sin(omega * t)

    return (2 / T) * integer(f, T, dt)


def fourier_1_re(t):  # Вещественная функция Фурье
    T = 6  # период
    N = 10  # Предел суммы ряда
    dt = [-3, 3]  # Рассматриваемый промежуток длинной Т

    # func = lambda t: 2 if 1 <= t <= 5 else 10  # 1 функция
    # func = lambda t: abs(t) # 2 функция
    func = lambda t: 3*t # 3 функция
    # func = lambda t: t**3 - 3*t**2 # 4 функция

    y = a_n(func, T, dt, 0) / 2  # нулевой коэф
    a, b = {0:2 * y}, {}
    for n in range(1, N + 1):  # Цикл суммирования
        omega = (2 * np.pi * n) / T  # Частота
        y += a_n(func, T, dt, omega) * np.cos(omega * t) + b_n(func, T, dt, omega) * np.sin(omega * t)  # формула
        a[n] = a_n(func, T, dt, omega)
        b[n] = b_n(func, T, dt, omega)
    print(r'a_n = ', a, '\n', r'b_n = ',b)
    return y  # возврат разложенной в ряд функции


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
        axes_labels = axes.get_axis_labels()  # подписи осей
        title = Text("N = 10", color=WHITE).to_edge(UL).shift([2,0,0])

        # graph_1 = axes.plot_line_graph([1, 5, 5, 8], [2, 2, 10, 10], color = BLUE)  # 1 функция
        # graph_1 = axes.plot(lambda t: abs(t), color = BLUE) # 2 функция
        graph_1 = axes.plot(lambda t: 3*t, color=BLUE)  # 3 функция
        # graph_1 = axes.plot(lambda t: t**3 - 3*t**2, color=BLUE)  # 3 функция

        line_1= axes.get_vertical_line(axes.i2gp(3, graph_1), color = YELLOW) #вертикальные линии - границы
        line_2 = axes.get_vertical_line(axes.i2gp(-3, graph_1), color=YELLOW)

        graph_1_fourier = axes.plot(fourier_1_re, color=RED)  # график разложенной в ряд функции

        plot = VGroup(axes, title, line_1, line_2, axes_labels, graph_1, graph_1_fourier)  # группировка
        self.add(plot)  # добавление на Scene
