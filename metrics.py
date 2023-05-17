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

def compute_min(list_2):
    min_list_2=list_2[0]
    for i in list_2:
        if i < min_list_2:
            min_list_2 = i
    return min_list_2        

def compute_max(list_3):
    max_list_3=list_3[0]
    for i in list_3:
        if i > max_list_3:
            max_list_3 = i
    return max_list_3 

def compute_median50():
    pass

def compute_median25():
    pass

def compute_median75():
    pass

def compute_hiepphuongsai():
    pass 

def compute_phuongsai():
    pass

def compute_correlation():
    pass