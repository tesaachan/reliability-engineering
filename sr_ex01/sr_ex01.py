import sys
from . import sr_ex01_utils as ut
from math import exp
from functools import reduce

def validity(val, func):
    try:
        result = func(val)
        return result
    except Exception as err:
        print("\nОшибка --> {}.\nПовторите ввод.\n".format(err))
        raise Exception

def data_parsed(line):
    def get_lambda(strs, path):
        if len(strs) == 0:
            return path 

        return get_lambda(strs[1:], path[strs[0]])

    number_i = int(line[0])
    lambda_i = get_lambda(line[1:], ut.values)

    return (number_i, lambda_i)

def sr_ex01(source):
    try:
        time = validity(source.readline(), int)
        numbers_i_and_lambdas_i = list(map(
            lambda n: validity(n.split(), data_parsed), 
            source.readlines()))
    except:
        return
    print("\nN_i и λ_i:", *numbers_i_and_lambdas_i)
    lambda_average = reduce(
        lambda n, m: n + m[0]*m[1],
        numbers_i_and_lambdas_i, 0)
    print("λ_c = {0:.3f} * 10e-6 1/час".format(lambda_average))
    probability_average = exp(-lambda_average * 10e-7 * time)
    running_time_average = 1 / (lambda_average * 10e-7)
    print(
        "\nПо данным таблицы находим:\
        \nP_c({0}) = e^(-λ_c*t) = e^(-{1} * 10e-6 * {0}) = {2}\
        \nT_ср.c = 1 / λ_c = 1 / ({1} * 10e-6) = {3}\
        \n\nВероятность безотказной работы системы: {2}\
        \nСредняя наработка до первого отказа: {3} часов\n"
        .format(
            time,
            "{0:.3f}".format(lambda_average),
            float("{0:.3f}".format(probability_average)),
            int(running_time_average)))

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="utf8") \
    if len(sys.argv) > 1 else sys.stdin as source:
        sr_ex01(source)
