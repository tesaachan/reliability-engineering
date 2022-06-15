from functools import reduce
from itertools import product
from . import sr_ex03_utils as ut

class Data:
    def __init__(self, coef, index, power):
        self.coef = coef
        self.index = index
        self.power = power

    def __str__(self):
        return "{}*(p_{})^{}".format(self.coef, self.index, self.power)

def equation(num, power):
    return ut.match( power,
        1, [Data(1, num, 1)],
        2, [Data(2, num, 1), Data(-1, num, 2)],
        3, [Data(1, num, 3), Data(-3, num, 2), Data(3, num, 1)])

def evaluate_answer(res, lambdas):
    parts = [
        (reduce(lambda x, y: x * y.coef, i, 1) / 
         reduce(lambda x, y: x + y[0]*y[1], zip([x.power for x in i], lambdas), 0)) 
         for i in res]
    return reduce(lambda x, y: x + y, parts, 0)

def sr_ex03():
    try:
        print("Input all λ using exp notation: ", end="")
        lambdas = [reduce(lambda x, y: x*float(y), i.split("*"), 1) for i in input().split()]
        print("Input the scheme (number of nodes in columns): ", end="")
        scheme = [int(i) for i in input().split()]
    except:
        print("\033[93mwrong input.\033[39m\n")
        return
    ut.print_lambdas(lambdas)
    p = [equation(i + 1, col_height) for i, col_height in enumerate(scheme)]
    ut.print_p(p)
    res = list(product(*p))
    ut.print_res(res)
    ut.print_tcp(res)
    ans = evaluate_answer(res, lambdas)
    print("T_cp.c = {}\n".format(int(ans)))

if __name__ == "__main__":
    sr_ex03()
