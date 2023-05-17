import numpy as np
import math
import pandas as pd
from pandas_profiling import ProfileReport

pd.set_option('display.float_format', lambda x: '%.3f' % x) #set số thực chỉ hiện 3 số sau dấu phẩy

from matplotlib import pyplot as plt

#cho phép vẽ đồ thị ngay trên notebook 

import seaborn as sns

# thư viẹn để vẽ biểu đồ
# nhập data
df_train = pd.read_csv("/home/hoainam/Desktop/house-prices-advanced-regression-techniques/train.csv")
df_train.shape


def col_to_drop (data):
    null=data.isnull().sum()/data.shape[0]*100
    col_to_drop = null[null>50].keys()
    data = data.drop(col_to_drop, axis = 1)
    return data

def  simple_clean (data):
train_df['LotFrontage'] = train_df['LotFrontage'].fillna(train_df['LotFrontage'].mean())
train_df['MasVnrArea']  = train_df['MasVnrArea'].fillna(train_df['MasVnrArea'].mean())  
train_df['GarageYrBlt'] = train_df['GarageYrBlt'].fillna(train_df['GarageYrBlt'].median())

train_df['MasVnrType']   = train_df['MasVnrType'].fillna(train_df['MasVnrType'].mode()[0])  
train_df['BsmtQual']     = train_df['BsmtQual'].fillna(train_df['BsmtQual'].mode()[0])  
train_df['BsmtCond']     = train_df['BsmtCond'].fillna(train_df['BsmtCond'].mode()[0])  
train_df['BsmtExposure'] = train_df['BsmtExposure'].fillna(train_df['BsmtExposure'].mode()[0])  
train_df['BsmtFinType1'] = train_df['BsmtFinType1'].fillna(train_df['BsmtFinType1'].mode()[0])  
train_df['BsmtFinType2'] = train_df['BsmtFinType2'].fillna(train_df['BsmtFinType2'].mode()[0])  
train_df['Electrical']   = train_df['Electrical'].fillna(train_df['Electrical'].mode()[0])  
train_df['FireplaceQu']  = train_df['FireplaceQu'].fillna(train_df['FireplaceQu'].mode()[0])  
train_df['GarageType']   = train_df['GarageType'].fillna(train_df['GarageType'].mode()[0])  
train_df['GarageFinish'] = train_df['GarageFinish'].fillna(train_df['GarageFinish'].mode()[0]) 
train_df['GarageQual']   = train_df['GarageQual'].fillna(train_df['GarageQual'].mode()[0])  
train_df['GarageCond']   = train_df['GarageCond'].fillna(train_df['GarageCond'].mode()[0])  
    
test_df.fillna(test_df.mode().iloc[0],inplace=True)

   