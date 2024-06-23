import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


class MyStableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


data = torch.Tensor([1, 2, 3])

my_softmax = MySoftmax()
output = my_softmax(data)
print(output)

my_stable_softmax = MyStableSoftmax()
output = my_stable_softmax(data)
print(output)
