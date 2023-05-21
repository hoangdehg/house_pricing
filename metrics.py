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

def compute_hiepphuongsai(L1,L2):
    
  if len(L1)!=len(L2):
    print("Khong the tinh covariance")
  else:
    avr_L1=sum(L1)/len(L1)
    avr_L2=sum(L2)/len(L2)
    new_L1=[(i-avr_L1) for i in L1]
    new_L2=[(j-avr_L2) for j in L2]
    new_L3=[a*b for a,b in zip(new_L1,new_L2)]
    covariance = sum(new_L3)/(len(new_L3)-1)
    return covariance 

def compute_phuongsai(list_1):
  if len(list_1) == 0:
    print("Khong the tinh phuong sai")
  else: 
    avr_list_1 = sum(list_1)/len(list_1)
    new_list = [pow((i-avr_list_1),2) for i in list_1]
    variance =  sum(new_list)/len(new_list)
    return variance
def compute_correlation(L1,L2):
    import statistics
    import numpy as np
    if len(L1)!=len(L2) or len(L1)==0 or len (L2)==0:
        print("Khong the tinh correlation")
    else:
        covariance = np.cov(L1, L2)[0, 1]
        std_dev_L1 = statistics.stdev(L1)
        std_dev_L2 = statistics.stdev(L2)
        correlation = covariance/(std_dev_L1*std_dev_L2)
        return correlation