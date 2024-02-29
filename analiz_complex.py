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
    N = 20  # Предел суммы ряда
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
    for n in range(-N, N + 1):  # Цикл суммирования
        com_omega = complex(0, (2 * np.pi * n) / T)  # Комплексная частота
        y += c_n(func, T, dt, com_omega) * np.exp(com_omega * t)  # формула
        if len(c) < 2 * N:
            c.append(np.sqrt(c_n(func, T, dt, com_omega).real**2+c_n(func, T, dt, com_omega).imag**2)**2)

    return np.sqrt(y.real ** 2 + y.imag**2)**2  # возврат разложенной в ряд функции
    # return y.imag #вещественные и мнимые функции по отдельности


c = []

inti = integer(fourier_1_im, 6, [-6 / 8, 7 * 6 / 8])  # Левая часть

coefs = sum(c) * 6  # Правая часть
print('Левая часть =', round(inti, 3))
print('Правая часть = ', round(coefs,3))