def frequency(n_delta, N_0, delta):
    return n_delta / (N_0 * delta)


def intensity_1(n_delta, N_avr, delta):
    return n_delta / (N_avr * delta)


def intensity_2(a_t, P_t):
    return a_t / P_t


def uptime_probability(N_0, n_t):
    return (N_0 - n_t) / N_0

def sr_ex02():
    try:
        #N_0, t, delta, n_t, n_delta = 1000, 21000, 1000, 840, 50
        N_0 = int(input('Введите N0: '))
        t = int(input('Введите t: '))
        delta = int(input('Введите delta: '))
        n_t = int(input('Введите nt: '))
        n_delta = int(input('Введите n delta: '))
        print()

        # PART 1
        P_begin = uptime_probability(N_0, n_t)
        P_end = uptime_probability(N_0, n_t + n_delta)
        N_avr = (N_0 - n_t + N_0 - (n_t + n_delta)) / 2
        n_middelta = N_0 - N_avr
        P_mid = uptime_probability(N_0, n_middelta)
        print(f'1. Вероятность безотказной работы:\n\tначало интервала - {P_begin}\n\tконец интервала - {P_end}\n\tсередина интервала - {P_mid}')

        # PART 2
        failure_frequency = frequency(n_delta, N_0, delta)
        print(f'2. Частота отказа - {failure_frequency}')

        # PART 3
        failure_intensity_1 = intensity_1(n_delta, N_avr, delta)
        failure_intensity_2 = intensity_2(failure_frequency, P_mid)
        print(f'3. Интенсивность отказа:\n\tчерез N - {failure_intensity_1}\n\tчерез частоту - {failure_intensity_2}\n')
    except:
        print("\033[93mwrong input.\033[39m\n")
        return

if __name__ == "__main__":
    sr_ex02()