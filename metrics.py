import math

def compute_rmse(y_pred,y):
    rmse = math.sqrt(sum((y_pred - y)**2)/len(y))
    return rmse

#TODO
def compute_mean():
    pass