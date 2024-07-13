import numpy as np
import pandas as pd

df = pd.read_csv('Module2/Week1/advertising.csv')
data = df.to_numpy()

# Question 15
max_value_sales = data[:, 3].max()
max_index_sales = data[:, 3].argmax()
print("max_value_sales:", max_value_sales)
print("max_index_sales:", max_index_sales)

# Question 16
mean_TV = data[:, 0].mean()
print("mean_TV:", mean_TV)

# Question 17
indices_sales = np.where(data[:, 3] >= 20)
count_sales = len(indices_sales[0])
print("count_sales:", count_sales)

# Question 18
indices_radio = np.where(data[:, 3] >= 15)
mean_radio = np.mean(data[indices_radio[0], 1])
print("mean_radio:", mean_radio)

# Question 19
mean_newspaper = np.mean(data[:, 2])
indices_newspaper = np.where(data[:, 2] > mean_newspaper)
sum_sales = np.sum(data[[indices_newspaper[0]], 3])
print("sum_sales:", sum_sales)

# Question 20
mean_sales = np.mean(data[:, 3])
scores = np.where(data[:, 3] > mean_sales, 'Good', np.where(
    data[:, 3] < mean_sales, 'Bad', 'Average'))
print(scores[7:10])

# Question 21
mean_sales = np.mean(data[:, 3])
A = np.min(abs(data[:, 3] - mean_sales)) + mean_sales
scores = np.where(data[:, 3] > A, 'Good', np.where(
    data[:, 3] < A, 'Bad', 'Average'))
print(scores[7:10])
