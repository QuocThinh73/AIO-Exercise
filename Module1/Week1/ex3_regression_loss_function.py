import random
import math


def cal_mae(samples, number):
    result = 0
    for i in range(number):
        result += abs(samples[i][0] - samples[i][1])
    return result


def cal_mse(samples, number):
    result = 0
    for i in range(number):
        result += (samples[i][0] - samples[i][1]) ** 2
    return result


def cal_rmse(samples, number):
    return math.sqrt(cal_mse(samples, number))


def regression_loss_function():
    n = input("Input number of samples (integer number) which are generated: ")
    if not n.isnumeric():
        print("number of samples must be an integer number")
        return
    func = input("Input loss name: ")

    n = int(n)
    samples = []
    for i in range(n):
        current_sample = [(random.uniform(0, 10), random.uniform(0, 10))]
        samples.extend(current_sample)
        loss = 0
        if func == "MAE":
            loss = cal_mae(current_sample, 1)
        elif func == "MSE":
            loss = cal_mse(current_sample, 1)
        else:
            loss = cal_rmse(current_sample, 1)
        print(
            f"loss name: {func}, sample: {i}, pred: {current_sample[0]}, target: {current_sample[1]}, loss: {loss}")

    final_loss = 0
    if func == "MAE":
        final_loss = cal_mae(samples, n)
    elif func == "MSE":
        final_loss = cal_mse(samples, n)
    else:
        final_loss = cal_rmse(samples, n)
    print(f"final {func}: {final_loss}")


while (True):
    regression_loss_function()
