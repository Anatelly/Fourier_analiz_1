import numpy as np

flag = False


def integerate(f, T, dt):  # интегрирование по Риману
    h_rim = 0.05  # мелкость разбиения
    N_rim = np.linspace(dt[0], dt[1], num=int(T / h_rim))  # разбиение промежутка длинной T

    coef = [f(i) * h_rim for i in N_rim]  # массив i-x сумм
    return sum(coef)  # итоговая частичная сумма


def a_n(func, T, dt, omega):  # первый коэф
    def f(t):  # реализация формулы первого коэфа
        return func(t) * np.cos(omega * t)  # omega = 2pin/T

    return (2 / T) * integerate(f, T, dt)  # окончательное значение


def b_n(func, T, dt, omega):  # второй коэф (все аналогично)
    def f(t):
        return func(t) * np.sin(omega * t)

    return (2 / T) * integerate(f, T, dt)


def fourier_1_re(t):  # Вещественная функция Фурье
    T = 4  # период
    N = 20  # Предел суммы ряда
    dt = [-1, 3]  # Рассматриваемый промежуток длинной Т

    # func = lambda t: 2 if 1 <= t <= 5 else 10  # 1 функция
    # func = lambda t: abs(t) # 2 функция
    # func = lambda t: 3 * t  # 3 функция
    func = lambda t: t**3 - 3*t**2 # 4 функция

    y = a_n(func, T, dt, 0) / 2  # нулевой коэф

    if len(ab) == 0: ab.append((a_n(func, T, dt, 0) ** 2) / 2)

    for n in range(1, N + 1):  # Цикл суммирования
        omega = (2 * np.pi * n) / T  # Частота
        y += a_n(func, T, dt, omega) * np.cos(omega * t) + b_n(func, T, dt, omega) * np.sin(omega * t)  # формула

        if len(ab) < N + 1: ab.append(a_n(func, T, dt, omega) ** 2 + b_n(func, T, dt, omega) ** 2)
    return y ** 2  # возврат разложенной в ряд функции


ab = []

inti = integerate(fourier_1_re, 4, [-1, 3]) * (2 / 4)  # Левая часть

coefs = sum(ab)  # Правая часть
print('Левая часть =', round(inti, 3))
print('Правая часть = ', round(coefs, 3))
