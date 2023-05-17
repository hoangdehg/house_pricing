from metrics import compute_rmse, compute_mean, compute_min, compute_max, compute_hiepphuongsai, compute_phuongsai, compute_correlation, compute_median25, compute_median50, compute_median75
import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error

def test_compute_rmse():
    y_pred = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array([1,2,3,4,5,6,7,8,9,11])
    rmse = compute_rmse(y, y_pred)
    assert rmse == sqrt(0.1)

    y_pred = np.array([1,2])
    y = np.array([3, 4])
    rmse = compute_rmse(y, y_pred)
    assert rmse == sqrt(4)

    y_pred = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array([1,2,3,4,5,6,7,8,9,11])
    mse = mean_squared_error(y, y_pred)
    rmse = sqrt(mse)
    assert rmse == sqrt(0.1)

def test_mean():
    arr = [1, 2, 3 ,4, 5]
    mean = compute_mean(arr)
    assert mean == 3

def test_min():
    arr = [1, 2, 3, 4, 5]
    min = compute_min(arr)
    assert min == 1

def test_max():
    arr = [1, 2, 3, 4, 5]
    min = compute_max(arr)
    assert max == 5

def test_median50():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    median50 = compute_median50(arr)
    assert median50 == 5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    median50 = compute_median50(arr)
    assert median50 == 5.5

def test_median25():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    median25 = compute_median25(arr)
    assert median25 == 2.5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    median25 = compute_median25(arr)
    assert median25 == 2.5

def test_median75():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    median75 = compute_median75(arr)
    assert median75 == 7.5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    median75 = compute_median75(arr)
    assert median75 == 8.5