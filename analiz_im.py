import numpy as np


def integerate(f, T, dt):  # интегрирование по Риману
    h_rim = 0.05  # мелкость разбиения
    N_rim = np.linspace(dt[0], dt[1], num=int(T / h_rim))  # разбиение промежутка длинной T

    coef = [f(i) * h_rim for i in N_rim]  # массив i-x сумм
    return sum(coef)  # итоговая частичная сумма


def c_n(func, T, dt, com_omega):  # комплексный коэф
    def f(t):  # реализация формулы комплексного коэфа
        return func(t) * np.exp(-com_omega * t)  # com_omega = (2pin/T)j

    return (1 / T) * integerate(f, T, dt)  # окончательное значение


def fourier_1_im(t):  # Комплексная функция Фурье
    T = 6  # период
    N = 20  # Предел суммы ряда
    dt = [-3, 3]  # Рассматриваемый промежуток длинной Т

    # func = lambda t: 2 if 1 <= t <= 5 else 10  # 1 функция
    # func = lambda t: abs(t)  # 2 функция
    func = lambda t: 3 * t  # 3 функция
    # func = lambda t: t**3 - 3*t**2 # 4 функция

    y = 0  # инициализация переменной для суммы
    for n in range(-N, N+1):  # Цикл суммирования
        com_omega = complex(0, (2 * np.pi * n) / T)  # Комплексная частота
        y += c_n(func, T, dt, com_omega) * np.exp(com_omega * t)  # формула
        if len(c) < 2 * N:
            c.append(np.sqrt(c_n(func, T, dt, com_omega).real**2+c_n(func, T, dt, com_omega).imag**2)**2)
            # c.append(c_n(func, T, dt, com_omega)**2)
    return np.sqrt(y.real ** 2 + y.imag**2)**2 # возврат разложенной в ряд функции
    # return y**2

c = []

inti = integerate(fourier_1_im, 6, [-3,3])  # Левая часть

coefs = sum(c) * 6  # Правая часть
print('Левая часть =', round(inti, 3))
print('Правая часть = ', round(coefs,3))
