import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def cal_sigmoid_function(x):
    return 1 / (1 + math.e ** (-x))


def cal_relu_function(x):
    if x <= 0:
        return 0
    return x


def cal_elu_function(x):
    alpha = 0.01
    if x <= 0:
        return alpha * (math.e ** x - 1)
    return x


def cal_activation_function():
    x = input("Input x = ")
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)

    func = input("Input activation Function (sigmoid|relu|elu): ")
    if function != "sigmoid" and func != "relu" and func != "elu":
        print(f"{func} is not supported")
        return

    if func == "sigmoid":
        print(f"{func}: f({x}) = {cal_sigmoid_function(x)}")
    elif func == "relu":
        print(f"{func}: f({x}) = {cal_relu_function(x)}")
    else:
        print(f"{func}: f({x}) = {cal_elu_function(x)}")



while (True):
    cal_activation_function()
