from functools import reduce

def match(statement, *args):
    (case, then) = (args[0::+2], args[1::+2])
    for i, _ in enumerate(case):
        if statement == case[i]:
            return then[i]
    return None

def print_lambdas(lambdas):
    print()
    for i, la_i in enumerate(lambdas):
        print("λ_{} = {}".format(i + 1, la_i))
    print()

def print_p(p):
    for i, p_i in enumerate(p):
        print("p_{}(t): {}(".format('I'*(i + 1), ' '*(len(p)-i)), end="")
        for j, p_i_j in enumerate(p_i):
            print("{}".format(p_i_j), end=") + (" if j != len(p_i) - 1 else ")\n")

def print_res(res):
    print("\nP(t) = ", end="")
    for i, res_i in enumerate(res):
        for j, res_i_j in enumerate(res_i):
            print("({})".format(res_i_j), end="*" if j < len(res_i) - 1 else "")
        print((" + " if i < len(res) - 1 else ""), end="")
    print("\n")

def print_tcp(res):
    print("T_cp.c = 0∫∞(P(t))dt = ", end="")
    uppers = [reduce(lambda x, y: x * y.coef, i, 1) for i in res]
    for i, res_i in enumerate(res):
        print("{}/(".format(uppers[i] if i == 0 else abs(uppers[i])), end="")
        for j, res_i_j in enumerate(res_i):
            print("{}λ_{}".format(res_i_j.power if res_i_j.power != 1 else "", j + 1), 
                end=" + " if j < len(res_i) - 1 else ")")
        sign = True if i < len(res) - 1 and uppers[i + 1] >= 0 else False
        print(" + " if sign else "", end=" - " if not sign and i < len(res) - 1 else "")
    print("\n")
