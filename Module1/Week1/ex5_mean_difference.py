def mean_differnce_of_nth_root_error(y, y_hat, n, p):
    print((y ** (1 / n) - y_hat ** (1 / n)) ** p)


mean_differnce_of_nth_root_error(y=100, y_hat=99.5, n=2, p=1)
mean_differnce_of_nth_root_error(y=50, y_hat=49.5, n=2, p=1)
mean_differnce_of_nth_root_error(y=20, y_hat=19.5, n=2, p=1)
mean_differnce_of_nth_root_error(y=0.6, y_hat=0.1, n=2, p=1)
