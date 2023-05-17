import math

def compute_rmse(y_pred,y):
    rmse = math.sqrt(sum((y_pred - y)**2)/len(y))
    return rmse

#TODO
def compute_mean(list_1):
    a=len(list_1)
    sum_list_1 = 0
    for i in list_1:
        sum_list_1+=i
    return sum_list_1/a

def compute_min():
    pass

def compute_max():
    pass

