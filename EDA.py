from data_def import df_train


#quan sát nhanh 
df_train.describe()

# những giá trị bị thiếu: LotArea and MasVnrea ...
# Có rất nhiều biến có giá trị max lớn hơn 75% -> có thể có nhiều biến ngoại lệ

# Minh họa histogram
df_train.hist(bins=200, figsize=(20, 15));

# Kiểm tra xem có id bị trùng lặp không để đảm bảo rằng không có thông tin bị trùng lặp trong dữ liệu 

idsUnique = len(set(df_train.Id)) #tính số lượng các giá trị duy nhất trong cột Id
idsTotal = df_train.shape[0] #Trả về số lượng hàng trong data
idsDupli = idsTotal - idsUnique # Tính số lượng các giá trị bị trùng lặp

# Loại bỏ cột Id để loại bỏ thông tin dư thừa và tránh bị overfitting
df_train.drop("Id", axis = 1, inplace = True) # axis = 1 là loại bỏ cột, = 0 là hàng. Inplace = True là loại bỏ ngay trên data gốc, nếu không sẽ tạo một bản sao mới mà không ảnh hưởng bản gốc
#Loc ra nhung bien
df_train = df_train[df_train.GrLivArea < 4000]


def 