def add(n1, n2):
    return n1 + n2


def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation={
    "+" : add,
    "-": sub,
    "*": multiply,
    "/": divide,

}
def calculator():
    n_1=float(input("enter the number"))
    do=True
    while do:
        for operator in operation:
            print(operator)
        operation_performed=input("select the operator")
        n_2=float(input("enter another number"))
        result=(operation[operation_performed](n_1,n_2))
        print(f"{n_1} {operation_performed} {n_2} = {result}")
        repeat=input(f"type 'y' if you want to continue with {result} or type 'n' for new calculation")
        if repeat=="y":
            do =True
            n_1=result
        elif repeat=="n":
            do=False
            print('\n'*20)
            calculator()
calculator()
