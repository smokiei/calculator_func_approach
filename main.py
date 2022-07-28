import operator

operation_dict = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul,
                  "/": operator.truediv}

esc_sym = "X"

def calc(a,b,oper):
    return operation_dict.get(oper)(a, b)
    pass

def input_operator():
    while True:
        o = input(f"Please input one of the operators {operation_dict.keys()}: ")
        if o == esc_sym:
            return False
        if operation_dict.get(o) is None:
            print(f"Sorry, its not an operator. If you want to exit write {esc_sym}")
        else:
            return o


def input_num(seq):
    while True:
        try:
            f = input(f"Please input {seq} number: ")
            if f == esc_sym:
                return False
            return (float(f))
        except:
            print(f"Sorry, its not a number. If you want to exit write {esc_sym} \n")

if __name__ == '__main__':
    a = input_num("first")
    if not a: exit(0)

    b = input_num("second")
    if not b: exit(0)

    operand = input_operator()
    if not operand: exit(0)

    print(calc(a, b, operand))
